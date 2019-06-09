"""Code Analyzer RUN."""


from flask import Flask
from flask.ext.restful import Api
from flask_wtf.csrf import CsrfProtect

from views import main
from api import configure_api

app = Flask(__name__)
app.config.from_object('config.default')
csrf_protect = CsrfProtect(app)
app.register_blueprint(main)
api_manager = Api(app)
configure_api(api_manager)


if __name__ == '__main__':
    app.run()
