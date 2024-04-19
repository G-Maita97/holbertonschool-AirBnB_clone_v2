#!/usr/bin/python3
"""Creacion de rutas con flask"""

# Importamos clase Flask y la funcion render_template.
from flask import Flask, render_template


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


# Create route with int variable.
@app.route("/number/<int:n>", strict_slashes=False)
def display_int(n):
    return f'{n} is a number'


# Crea ruta que muestra un archivo html con la funcion render_template.
@app.route("/number_template/<int:n>", strict_slashes=False)
def display_HTML(n):
    return render_template('5-number.html', n=n)


# Crea ruta que muestra un archivo html con la funcion render_template.
@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def display_HTML_odd_even(n):
    # verifica si es par o impar para dar parametro a la variable.
    if n % 2 == 0:
        return render_template('6-number_odd_or_even.html', num=n, o_e='even')
    else:
        return render_template('6-number_odd_or_even.html', num=n, o_e='odd')


if __name__ == '__main__':
    # Configurar la aplicación para escuchar en 0.0.0.0 en el puerto 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
    """
    debug=Tru para que Flask muestre mensajes
    detallados de error en caso de que ocurra
    un problema.
    """
