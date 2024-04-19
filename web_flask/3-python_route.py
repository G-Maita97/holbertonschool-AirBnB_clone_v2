#!/usr/bin/python3
"""Creacion de rutas con flask"""

from flask import Flask  # importamos la clase Flask.


app = Flask(__name__)  # instanciamos la clase Flask.


# Definir ruta con "strict_slashes=False"
@app.route("/", strict_slashes=False)
# funcion atada a la ruta
def Hello_HBNB():
    # Retorna codigo html
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    return "HBNB"


# Definimos ruta con variables(texto)
@app.route("/c/<text>", strict_slashes=False)
def C_TEXT(text):
    """
    La función replace() es un método de cadena en Python
    que se utiliza para reemplazar todas las ocurrencias de
    un determinado substring (subcadena) dentro de una cadena
    con otra subcadena.
    """
    text = text.replace('_', ' ')
    """
    la función devuelve una cadena que comienza con la
    letra "C" seguida por el valor de la variable text
    """
    return f'C {text}'


# Ruta /python/ tiene valor predeterminado para la variable text 'is_cool'.
@app.route("/python/", strict_slashes=False)
# definiendo funcion con variable
@app.route("/python/<text>", strict_slashes=False)
def python_text_value_default(text='is cool'):
    text = text.replace('_', ' ')
    return f'Python {text}'


if __name__ == '__main__':
    # Configurar la aplicación para escuchar en 0.0.0.0 en el puerto 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
    """
    debug=Tru para que Flask muestre mensajes
    detallados de error en caso de que ocurra
    un problema.
    """
