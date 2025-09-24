from flask import Flask
from .routes.graphql import graphql_bp

def create_app() -> Flask:
    app = Flask(__name__)

    @app.get('/health')
    def health():
        return {'status': 'ok'}

    app.register_blueprint(graphql_bp)

    return app