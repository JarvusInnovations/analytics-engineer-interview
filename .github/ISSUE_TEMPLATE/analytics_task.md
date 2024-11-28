---
name: Analytics Engineering Task
about: Technical evaluation task for Analytics Engineering candidates
title: 'Analytics Engineering Task: SEPTA GTFS Analysis'
labels: 'evaluation'
assignees: ''
---

# Analytics Engineering Task

## Background

As part of our evaluation process, we'd like you to work on a real-world data analysis task. For this task, assume that we are working on a project for SEPTA (Southeastern Pennsylvania Transportation Authority), and they request that we pull together some data to inform a visualization of the number of routes for each mode within the system. This task requires that we have access to their GTFS (General Transit Feed Specification) data.

## Task Description

1. Download the [bus and rail GTFS feeds for SEPTA](https://github.com/septadev/GTFS/releases) and import the routes and agency tables for both into DuckDB
2. Clean up the imported tables, adding a text version of [`route_type`](https://gtfs.org/documentation/schedule/reference/#routestxt) (i.e. mode name)
3. Produce a view showing the total routes per mode: agency_name, mode_name, route_count
4. Open a pull request for us to review just as you would working on a team

## Expected Time

You are expected to spend 1–2 hours on this task. Feel free to extend the idea of the exercise as you see fit as long as you are meeting the core requirements.

## Getting Started

1. Clone this repository
2. Install dependencies using Poetry: `poetry install`
3. Run the existing pipeline to verify setup: `docker compose run analytics`

## Development Workflow

1. Create a new branch for your work
2. Implement your solution following these steps:
   - Add data ingestion script for GTFS feeds
   - Create staging models for routes and agency tables
   - Implement the mode name mapping
   - Create the final view with route counts
3. Test your changes locally
4. Open a pull request with your solution

## Evaluation Criteria

We will evaluate your submission based on:

- Code quality and organization
- SQL/dbt best practices
- Documentation
- Git workflow
- Problem-solving approach

## Resources

- [GTFS Reference](https://gtfs.org/documentation/schedule/reference/)
- [dbt Documentation](https://docs.getdbt.com/)
- [DuckDB Documentation](https://duckdb.org/docs/)

## Questions?

If you have any questions about the task or requirements, please don't hesitate to ask by commenting on this issue.

Good luck!
