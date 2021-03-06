#!/usr/bin/python3
""" 7-states_list.py
Module that starts a Flask web application
and lists all State instances from a database
"""
from flask import Flask, render_template
from models.state import State
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def shutdown_session(response_or_exc):
    """Close the current SQLAlchemy Session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def display_states_list():
    """Displays HTML page with list of states"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
