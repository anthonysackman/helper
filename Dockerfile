# Use an official lightweight Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Install build tools and dependencies for PostgreSQL and Redis
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies using uv
RUN pip install uv && uv sync

# Copy the application code into the container
COPY . .

# Expose the Sanic default port
EXPOSE 8000

# Run the Sanic app with uv
CMD ["uv", "run", "sanic", "app.create_app", "--dev"]
