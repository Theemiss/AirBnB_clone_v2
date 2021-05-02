#!/usr/bin/python3
"""
flask model
"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)
storage.all()


@app.teardown_appcontext
def teardown_data(self):
    """
        refrech data
    """
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """ return all citie in the db  """
    states = storage.all(State)

    return render_template('8-cities_by_states.html', states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """
        list state by id if found
    """
    states = storage.all(State).values()
    for x in states:
        if x.id == id:
            found = x
            break
        else:
            found = None
    return render_template('9-states.html', state=found)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
