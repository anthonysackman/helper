import os

class Config:
    """Configuration with defaults for local development."""
    DEBUG = os.getenv("DEBUG", "true").lower() == "true"
    TESTING = os.getenv("TESTING", "false").lower() == "true"
    SECRET_KEY = os.getenv("SECRET_KEY", "local-secret-key")
    DATABASE_URL = os.getenv(
        "DATABASE_URL",
        "postgresql+asyncpg://user:password@db:5432/helper"
    )  # Default PostgreSQL connection
    LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG")  # DEBUG, INFO, WARNING, ERROR
    HOST = os.getenv("HOST", "127.0.0.1")  # Default local host
    PORT = int(os.getenv("PORT", "8000"))  # Default Sanic port
    SQLALCHEMY_ECHO = os.getenv("SQLALCHEMY_ECHO", "false").lower() == "true"
    REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")  # Default Redis connection

    @classmethod
    def as_dict(cls):
        """Return configuration as a dictionary."""
        return {
            key: getattr(cls, key)
            for key in dir(cls)
            if not key.startswith("__") and not callable(getattr(cls, key))
        }
