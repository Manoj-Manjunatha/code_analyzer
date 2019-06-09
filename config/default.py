"""Code Analyzer default configuraion file."""

import os

SECRET_KEY = 'code_analyzer_secret_key'

APP_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

CSRF_ENABLED = True

DEBUG = True

STATIC_FOLDER = os.path.abspath(os.path.join(APP_ROOT_DIR, "static"))

MEDIA_FOLDER = os.path.join(STATIC_FOLDER, "media")

TEMP_FOLDER = os.path.join(MEDIA_FOLDER, "temp")
