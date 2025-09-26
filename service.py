from model import db, Producto,Proveedor,RecepcionProductos
from app import app

def guardar_producto(nombre_producto,descripcion_producto,nombre_laboratorio):
    with app.app_context():
        try:
            new_producto=Producto(
                nombre=nombre_producto,
                descripcion=descripcion_producto,
                nombre_laboratorio=nombre_laboratorio
            )
            db.session.add(new_producto)
            db.session.commit()
            return "Producto creado exitosamente"
        except Exception as e:
            return ("El Producto no pudo crear "+ e)
        
def obtener_productos():
    Productos=Producto.query.all()
    return Productos