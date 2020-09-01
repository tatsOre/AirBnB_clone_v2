#!/usr/bin/python3
"""
Module that starts a Flask web application: 6-number_odd_or_even
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
    all_states = storage.all(State).values()
    return render_template('7-states_list.html', states=all_states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
