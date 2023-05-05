from flask import Flask, flash, redirect, render_template, request, url_for
from auth import auth_bp
import mysql.connector


app = Flask(__name__)
app.register_blueprint(auth_bp)
app.secret_key = '117394S@n'


@app.route('/')
def home():
    return render_template('inicio.html')

# Configuración de la conexión a la base de datos
conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Qcwzhv123456789',
    database='cristnarts'
)

@app.route('/productos')
def productos():
    cursor = conexion.cursor()
    cursor.execute('SELECT id, nombreprod, descripcion, categoria, precio, imagen FROM productos')
    productos = cursor.fetchall()
    cursor.close()
    return render_template('productos.html', productos=productos)

@app.route('/productos/crear', methods=['GET', 'POST'])
def crear_producto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        categoria = request.form['categoria']
        precio = request.form['precio']
        imagen = request.files['imagen']
        # Aquí deberás insertar el nuevo producto en la base de datos
        flash('El producto ha sido creado exitosamente')
        return redirect(url_for('productos'))
    return render_template('crear-producto.html')

if __name__ == '__main__':
    app.run(debug=True)