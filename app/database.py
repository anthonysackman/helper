from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.pool import NullPool

# Declarative base for models
Base = declarative_base()

# Engine and session factory will be initialized later
engine = None
SessionFactory = None

async def setup_database(database_url: str, echo: bool = False):
    """Setup the SQLAlchemy engine and session factory."""
    global engine, SessionFactory

    # Create the async engine
    engine = create_async_engine(
        database_url,
        echo=echo,
        poolclass=NullPool  # Adjust pool settings as needed
    )

    # Create the session factory
    SessionFactory = sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False
    )

    # Create tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def shutdown_database():
    """Dispose of the SQLAlchemy engine."""
    global engine
    if engine:
        await engine.dispose()
        engine = None
