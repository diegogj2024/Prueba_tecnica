from flask import Flask,request,render_template,redirect, url_for,session,flash
from model import db 
import service

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin12345@localhost/prueba_tecnica'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/productos')
def productos():
    productos=service.obtener_productos()
    return render_template('/productos.html',productos=productos)

@app.route('/new_product')
def new_product():
    return render_template('newproduct.html')

@app.route('/guardar_producto', methods=['POST'])
def guardar_producto():
    nombre_producto=request.form['nombre_p']
    descripcion_producto=request.form['descripcion_p']
    nombre_laboratorio=request.form['nombre_lab']
    aviso=service.guardar_producto(nombre_producto,descripcion_producto,nombre_laboratorio)
    return render_template('newproduct.html',aviso=aviso)


if __name__ == '__main__':
    app.run(debug=True)