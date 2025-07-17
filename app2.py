from flask import Flask, jsonify

app = Flask(__name__)

# Lista simulada de productos (como si fuera una base de datos en memoria)
productos = [
    {'id': 1, 'nombre': 'Camisa blanca', 'precio': 25000},
    {'id': 2, 'nombre': 'Pantalón negro', 'precio': 45000},
    {'id': 3, 'nombre': 'Chaqueta azul', 'precio': 80000}
]

# Ruta para ver todos los productos
@app.route('/productos')
def obtener_productos():
    return jsonify(productos)

# Ruta para ver un producto específico por su ID
@app.route('/producto/<int:producto_id>')
def obtener_producto_por_id(producto_id):
    # Buscar el producto por su ID
    for producto in productos:
        if producto['id'] == producto_id:
            return jsonify(producto)
    return jsonify({'mensaje': 'Producto no encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)
