#!/usr/bin/python3
""" 9-states.py
Module that starts a Flask web application and lists all States by ID
"""
from flask import Flask, render_template
from models.state import State
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def shutdown_session(response_or_exc):
    """Close the current SQLAlchemy Session"""
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def display_states(id=None):
    """Displays HTML page with list of states/states by ID"""
    states = storage.all(State).values()
    state = None
    if id:
        for item in states:
            if id == item.id:
                state = item
    return render_template('9-states.html', **locals())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
