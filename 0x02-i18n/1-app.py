#!/usr/bin/env python3
"""
This is a basic Flask app with Flask-Babel integration.
"""
from flask import Flask, render_template
from flask_babel import Babel

# Instantiate Flask app
app = Flask(__name__)

# Instantiate Babel object
babel = Babel(app)

# Configure available languages
class Config:
    LANGUAGES = ["en", "fr"]

# Set Flask app config using Config class
app.config.from_object(Config)

# Set Babel default locale and timezone
babel.default_locale = 'en'
babel.default_timezone = 'UTC'

@app.route('/')
def index():
    """Render index.html template."""
    return render_template('index.html', title='Welcome to Holberton', header='Hello world')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
