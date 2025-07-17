from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/')
def inicio():
    return "hola mundo este es mi primer servidor backend"
@app.route('/producto')
def obtener_producto():
    producto = {
        'nombre': 'Camisa blanca',
        'precio': 25000,
        'stock': 15
    }
    return jsonify(producto)

if __name__ == '__main__':
    app.run(debug=True)
