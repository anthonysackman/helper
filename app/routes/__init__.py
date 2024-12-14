from sanic import Blueprint
from .ping import ping_bp

# version 1 group, all new route bps need to be added here
bp_v1 = Blueprint.group([ping_bp], version=1)

def setup_routes(app):
    """Register blueprints to app."""
    app.blueprint([bp_v1])