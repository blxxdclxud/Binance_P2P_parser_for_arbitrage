from flask import Flask


def create_app(**config):

    app = Flask(__name__)

    from views import p2p_parser
    app.register_blueprint(p2p_parser)

    return app
