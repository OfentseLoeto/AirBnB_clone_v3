#!/usr/bin/python3

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)

@app.route('/states', strict_slashes=False)

def states():
    """Display an HTML page listing all State objects
        present in DBStorage sorted by name.
    """
    states = storage.all(State)
    sorted_states = sorted(states.value(), key=lambda state: state.name)
    return render_template('9-states.html', states=sorted_states)

@app.route('/states/<id>', strict_slashes=False)

def states_cities(id):
    """Display an HTML page with State and linked City objects sorted by name."""
    state = storage.get(States, id)
    if state is None:
        return render_template('not_found.html')
    else:
        cities = sorted(state.cities, key=lambda city: city.name)
        return render_template('state_cities.html', state=state, cities=cities)

@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session after each request."""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
