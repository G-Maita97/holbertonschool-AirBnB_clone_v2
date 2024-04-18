#!/usr/bin/python3
"""Creacion de rutas con flask"""

from flask import Flask  # importamos la clase Flask.


app = Flask(__name__)  # instanciamos la clase Flask.


@app.route("/", strict_slashes=False)  # Definir ruta sin strict_slashes=False (por defecto es True)
def Hello_HBNB():                    # funcion atada a la ruta(un nombre de funcion solo puedes estar atada a una)
    return "<p>Hello HBNB!</p>"        # Retorna codigo html


if __name__ == '__main__':
    # Configurar la aplicación para escuchar en 0.0.0.0 en el puerto 5000
    app.run(host='0.0.0.0', port=5000, debug=True)  # debug=True para que Flask muestre mensajes detallados de error en caso de que ocurra un problem.
