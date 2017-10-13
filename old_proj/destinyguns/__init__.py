from flask import Flask



def create_app():
    app = Flask(__name__)
    # todo: app.config.from_object('config')

    app.register_blueprint()

