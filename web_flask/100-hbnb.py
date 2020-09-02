#!/usr/bin/python3
""" 100-hbnb.py
Module that starts a Flask web application and renders HBNB main page
"""
from flask import Flask, render_template
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def shutdown_session(response_or_exc):
    """Close the current SQLAlchemy Session"""
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb_filters():
    """Displays HTML page with list of states/states by ID"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
    return render_template('100-hbnb.html', **locals())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
