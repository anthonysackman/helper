# app/__init__.py
from sanic import Sanic
from app.routes import setup_routes
from config import Config

def create_app():
    app = Sanic("Helper")
    app.config.update(Config.as_dict())
    setup_routes(app)
    return app
