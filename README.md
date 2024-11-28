# Analytics Engineer Interview Project

This repository contains a technical evaluation project for Analytics Engineering candidates at Jarvus. It provides a structured environment for working with data pipelines using dbt and DuckDB.

## Project Structure

```
.
├── data/               # Data directory (gitignored except for .gitkeep)
│   └── raw/           # Raw data storage
├── models/            # dbt models
│   ├── staging/       # Staging models
│   ├── intermediate/  # Intermediate models
│   └── marts/         # Mart models
├── scripts/           # Data ingestion scripts
├── tests/            # dbt tests
└── macros/           # dbt macros
```

## Prerequisites

- Docker and Docker Compose
- Git

## Local Development Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-org/analytics-engineer-interview.git
   cd analytics-engineer-interview
   ```

2. Start the development environment:

   ```bash
   docker compose build
   docker compose run dev
   ```

3. Run the full pipeline:

   ```bash
   docker compose run analytics
   ```

## Development Workflow

### Running Individual Components

1. Data Ingestion:

   ```bash
   docker compose run ingest
   ```

2. dbt Commands:

   ```bash
   docker compose run dbt deps    # Install dbt dependencies
   docker compose run dbt debug   # Test connection
   docker compose run dbt build   # Run models, tests, and snapshots
   ```

### Making Changes

1. Create a new branch:

   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes to the models, scripts, or configurations

3. Test your changes:

   ```bash
   docker compose run analytics
   ```

4. Open a pull request on GitHub

## Deployment Process

The project includes a GitHub Actions workflow that:

1. Runs on push to main branch and pull requests
2. Executes the full pipeline
3. Uploads the DuckDB database and dbt artifacts as workflow artifacts

## Project Components

### Data Pipeline

- Downloads example data from public sources
- Loads data into a local DuckDB database
- Processes data through dbt models:
  - Staging models for initial data cleaning
  - Intermediate models for data transformation
  - Mart models for final analysis

### dbt Models

- `stg_bus_shelters`: Initial cleaning and column renaming
- `int_shelter_locations`: Geographic clustering analysis
- `mart_shelter_distribution`: High-level shelter distribution metrics

### Configuration Files

- `pyproject.toml`: Python dependencies managed by Poetry
- `dbt_project.yml`: dbt project configuration
- `profiles.yml`: dbt connection profiles
- `docker-compose.yml`: Container configuration
- `Dockerfile`: Development environment definition

## Contributing

See our [Contributing Guidelines](CONTRIBUTING.md) for development practices and standards.

## Support

If you encounter any issues or have questions, please:

1. Check the existing GitHub issues
2. Create a new issue if needed
3. Comment on your assigned evaluation task

## License

This project is proprietary and confidential. All rights reserved.
