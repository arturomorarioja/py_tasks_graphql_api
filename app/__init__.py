from flask import Flask
from .routes.tasks import tasks_bp

def create_app() -> Flask:
    app = Flask(__name__)

    @app.get('/health')
    def health():
        return {'status': 'ok'}

    app.register_blueprint(tasks_bp)

    return app