#!/usr/bin/python3
"""
flask model
"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False

@app.teardown_appcontext
def teardown_data(self):
        storage.close()

@app.route('/states_list')
def states_list():
    """
        list state
    """
    data_state = storage.all(State)
    states = []
    for i in data_state:
        states.append(data_state)
    return render_template('7-states_list.html', states=states)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
