from flask import Flask
app = Flask(__name__)

@app.route('/')
def inicio():
    return 'hola, mundo este es mi primer servidor backend '
if __name__=='__main__':
    app.run(debug=True)