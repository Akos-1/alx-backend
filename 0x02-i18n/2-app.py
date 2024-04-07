#!/usr/bin/env python3

from flask import request
from babel import Locale
from babel.support import Translations

SUPPORTED_LANGUAGES = ['en_US', 'fr_FR', 'es_ES']


def get_locale():
    @babel.localeselector
    def select_locale():
        # Get the list of accepted languages from the request
        accepted_languages = request.accept_languages

        # Iterate through accepted languages and select the best match
        for lang, _ in accepted_languages:
            if lang in SUPPORTED_LANGUAGES:
                return lang

        # If no match found, fallback to default language
        return 'en_US'  # Default language

    return select_locale()
