import sys
import os

# Add the project root directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..', '..', '..', '..'))
sys.path.insert(0, project_root)


from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context
# Interpret the config file for Python logging.
fileConfig(context.config.config_file_name)

# Import the Flask app's db and models
from libs.postgres.db import db
from libs.postgres.models import QA


# this is the Alembic Config object
config = context.config

# Set the target metadata for 'autogenerate' support
target_metadata = db.metadata

def get_database_url():
    # Get the database URL from the app config
    from app.config import Config
    return Config.SQLALCHEMY_DATABASE_URI

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = get_database_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations in 'online' mode."""
    # Get the database URL from your configuration
    url = get_database_url()
    
    # Create an engine using the database URL
    connectable = engine_from_config(
        configuration=config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        url=url,
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
