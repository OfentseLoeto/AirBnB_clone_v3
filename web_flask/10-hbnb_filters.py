#!/usr/bin/python3

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)

@app.route('/hbnb_filters', strict_slashes=False)

def hbnb_filters():
    """"Display an HTML page"""
    states = storage.all(states)
    sorted_states = sorted(states.values(), key=lambda state: state.name)
    aminities = storage.all(Amenity)

    sorted_amenities = sorted(amnenities.valuess(), key=lambda amenity: amenity.name)
    return render_template('10-hbnb_filters.html', states=sorted_states, amenities=sorted_amenities)

@app.teardown_appcontext
def teardown_db(exception):
     """Remove the current SQLAlchemy Session after each request."""
     storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
