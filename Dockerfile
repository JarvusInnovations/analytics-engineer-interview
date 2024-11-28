FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry and add to PATH
ENV POETRY_HOME=/opt/poetry
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry --version

# Set working directory
WORKDIR /app

# Copy project files
COPY pyproject.toml poetry.lock* ./
COPY dbt_project.yml profiles.yml ./
COPY models/ models/
COPY scripts/ scripts/
COPY macros/ macros/
COPY tests/ tests/

# Configure Poetry
RUN poetry config virtualenvs.create false

# Install dependencies
RUN poetry lock
RUN poetry install --no-interaction --no-ansi

# Make scripts executable
RUN chmod +x scripts/ingest_data.py

# Set environment variables
ENV DBT_PROFILES_DIR=.

# Default command
CMD ["bash"]
