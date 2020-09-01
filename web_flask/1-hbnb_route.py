#!/usr/bin/python3
"""
Module that starts a Flask web application: 1-hbnb_route.py
"""
from flask import Flask, escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!' as response"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays 'HBNB' as response"""
    return 'HBNB'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
