from flask import Flask
import sys
from logging import config
from .extensions import db
from .routes import blueprint


# reload(sys)
# sys.setdefaultencoding('utf-8')

# config.fileConfig('logstash.conf')


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config')
    app.config.from_pyfile('config.py')
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    db.init_app(app)


def register_blueprints(app):
    app.register_blueprint(blueprint)


app = create_app()
