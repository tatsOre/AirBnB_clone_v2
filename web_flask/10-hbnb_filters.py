#!/usr/bin/python3
""" 9-states.py
Module that starts a Flask web application and lists all States by ID
"""
from flask import Flask, render_template
from models.state import State
from models.amenity import Amenity
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def shutdown_session(response_or_exc):
    """Close the current SQLAlchemy Session"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Displays HTML page with list of states/states by ID"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', **locals())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
