#!/usr/bin/python3

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.route('/city_by_states', strict_slashes=False)

def city_by_states():
    """Display an HTML page listing all State objects
       and their linked City objects.
    """
    states = storage.all(States)
    sorted_states = sorted(states.value(), key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=sorted_states)

@app.teardown_appcontext
def teardown(exception):
    """Remove the current SQLAlchemy Session after each request."""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
