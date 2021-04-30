#!/usr/bin/python3
"""
"""
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hbnb():
    """
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def index():
    """
    """
    return 'HBNB'


@app.route('/c/<text>')
def C_is(text):
    """
    """
    return 'C is {:s}'.format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python(text):
    """
    """
    return 'Python {:s}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number(n):
    """
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """
    """
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
