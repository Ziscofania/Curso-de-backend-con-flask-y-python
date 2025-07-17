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