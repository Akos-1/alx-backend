#!/usr/bin/env python3

from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)
babel = Babel(app)

SUPPORTED_LANGUAGES = ['en', 'fr']
app.config['BABEL_DEFAULT_LOCALE'] = 'en'


@babel.localeselector
def get_locale():
    # Check if 'locale' parameter is present in the request URL
    locale_param = request.args.get('locale')
    
    if locale_param and locale_param in SUPPORTED_LANGUAGES:
        return locale_param
    else:
        # Resort to the default behavior
        return request.accept_languages.best_match(SUPPORTED_LANGUAGES)


@app.route('/')
def home():
    return render_template('home.html',
                           title=_('home_title'),
                           header=_('home_header'))


if __name__ == '__main__':
    app.run()
