# Curso-de-backend-con-flask-y-python

## ruta de aprendizaje para ser desarrollador de backend con flask y python

En este Readme.md encontraras toda la informacion de mi ruta de desarrollo para convertirme en desarrollador de backend 

### 1 crear tu primer servidor de python usando flask
Crear tu primer servidor en Python usando Flask, que responda un mensaje cuando visitemos una ruta 

## Paso 1: Crear el entorno de trabajo

1. Inicia tu editor de codigo.
2. Crea una nueva carpeta con el nombre: `mi_primer_backend`.
3. Dentro de esa carpeta, crea un archivo llamado: `app.py`.

## Paso 2: Crear un entorno virtual (opcional pero recomendado)

Esto es para instalar las librerías sin afectar el resto de tu computadora.

Abre la terminal en tu editor de codigo (`Ctrl + ñ` o desde "Terminal > Nueva Terminal") y escribe:

```bash
python -m venv venv
```

Para activar el entorno virtual:

En Windows:

```bash
venv\Scripts\activate
```
En Linux/macOS:
```bash
source venv/bin/activate
```
Una vez activado, verás algo así en la terminal:

```(venv) C:\Users\TuUsuario\mi_primer_backend>```

## Paso 3: Instalar Flask

En esa misma terminal, instala Flask con:
```bash
pip install flask
```
Ejecutar la aplicación

Después de configurar tu archivo app.py, ejecuta:
```bash
python app.py
```


### 2 crear una api que devuelva datos (JSON)

# Mi Primer API con Flask

Guía para crear tu primera API que devuelve respuestas JSON con Flask.

## 🚀 Ejecutar el servidor

1. Asegúrate de estar en el entorno virtual
2. Ejecuta en la terminal:

```bash
python app.py
```
Probar la API

Abre tu navegador y visita:
"http://127.0.0.1:5000/producto"

Deberías ver la siguiente respuesta JSON:
json

{
  "nombre": "Camisa blanca",
  "precio": 25000,
  "stock": 15
}

¡Felicidades! Acabas de crear tu primera API.
¿Qué aprendiste hoy?

    Qué es JSON y por qué es importante

    Cómo usar Flask para enviar respuestas en formato JSON

    Cómo crear múltiples rutas en tu servidor (/ y /producto)

# Parte 3: Lista de productos y rutas dinámicas con Flask

## Objetivos de aprendizaje

- Mostrar todos los productos en la ruta `/productos`
- Mostrar un producto específico usando rutas dinámicas como `/producto/2`

## Ejecutar el servidor

En la terminal, ejecuta:

```bash
python app2.py
```
🌐 Probar los endpoints
Todos los productos:

http://localhost:5000/productos
Producto específico (ejemplo ID 2):

http://localhost:5000/producto/2
Producto inexistente (ejemplo ID 99):

http://localhost:5000/producto/99

Respuesta esperada para producto no encontrado:
json

{
  "mensaje": "Producto no encontrado"
}

### Conceptos aprendidos

- Uso de listas en memoria como base de datos temporal
- Creación de rutas dinámicas con <int:producto_id>
- Manejo de respuestas 404 Not Found en Flask
- Estructuración de APIs RESTful básicas