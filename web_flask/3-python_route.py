#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)

def hello_hbnb():
    """Display 'Hello HBNB!'"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)

def hbnb():
    """Display 'HBNB!'"""
    return 'HBNB!'

@app.route('/python/(<text>)', strict_slashes=False)

def python_text(python, text):
    """ display “Python ”, followed by the value of the text variable
        (replace underscore _ symbols with a space )
    """
    python = python.replace('_', ' ')
    text = text('is cool')
    return 'python.text {}'.format(python, text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
