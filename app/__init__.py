from sanic import Sanic
from app.routes import setup_routes
from config import Config
import redis.asyncio as redis


def create_app():
    """Create Sanic App Instance."""
    app = Sanic("Helper")
    app.config.update(Config.as_dict())
    setup_routes(app)
    setup_app_redis(app)

    return app


def setup_app_redis(app):
    """Setup Redis lifecycle events for the app."""

    @app.before_server_start
    async def connect_to_redis(app, _):
        """Connect to Redis."""
        redis_url = app.config.get("REDIS_URL", "redis://localhost:6379/0")
        app.ctx.redis = redis.from_url(redis_url)

    @app.after_server_stop
    async def disconnect_from_redis(app, _):
        """Disconnect Redis."""
        if hasattr(app.ctx, "redis"):
            await app.ctx.redis.close()
