#!/usr/bin/python3
"""Creacion de rutas con flask"""

from flask import Flask  # importamos la clase Flask.


app = Flask(__name__)  # instanciamos la clase Flask.


# Definir ruta sin "strict_slashes=False"
@app.route("/", strict_slashes=False)
# funcion atada a la ruta
def Hello_HBNB():
    # Retorna codigo html
    return "Hello HBNB!"


if __name__ == '__main__':
    # Configurar la aplicación para escuchar en 0.0.0.0 en el puerto 5000
    app.run(host='0.0.0.0', port=5000, debug=True)
    """
    debug=Tru para que Flask muestre mensajes
    detallados de error en caso de que ocurra
    un problema.
    """
