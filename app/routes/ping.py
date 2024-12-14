from sanic import Blueprint, response, text

ping_bp = Blueprint("ping", url_prefix="/ping")

@ping_bp.route("", methods=["GET"])
async def ping(request):
    """Test Ping Endpoint."""
    return text("Pong")