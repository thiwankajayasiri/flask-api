[![codecov](https://codecov.io/github/thiwankajayasiri/flask-api/graph/badge.svg?token=C1YSBULP4C)](https://codecov.io/github/thiwankajayasiri/flask-api)

# Employee Management API

A RESTful API for managing employees, built with Flask and Pydantic.

## Table of Contents

- [Description](#description)
- [Design Considerations](#design-considerations)
- [Dependencies](#dependencies)
- [Installation](#installation)
  - [Poetry](#poetry)
  - [Conda](#conda)
- [Testing](#testing)
  - [Unit Testing](#unit-testing)
  - [Performance Testing](#performance-testing)
- [Contact](#contact)

---

## Description

Manage a list of employees with CRUD operations. Each employee has an `id`, `first_name`, `last_name`, and `position`. Data is temporarily stored in an in-memory list.

> [!NOTE]
> Data is not persisted and will be lost once the server is stopped.

---

## Design Considerations

### Project Considerations

- RESTful API design
- Pydantic for data validation
- In-memory list as a mock database
- Supports both Poetry and Conda for dependency management
- Tested with pytest, pytest-flask, and Locust
- CI/CD pipeline via GitHub Actions
- Code quality assured by flake8 and mypy

> [!IMPORTANT]
> Always review code quality reports and test results in the CI/CD pipeline.

### Flask API Design Considerations

Detailed below are the design considerations for the API.

#### General Considerations

1. Versioning
2. Pagination
3. Filtering and Sorting
4. Rate Limiting
5. Caching
6. Throttling
7. Logging and Monitoring

#### Endpoint-Specific Considerations

- Add (POST /employees)
- Read All (GET /employees)
- Read One (GET /employees/<id>)
- Update (PUT /employees/<id>)
- Delete (DELETE /employees/<id>)

> [!WARNING]
> Always check for a valid `id` before performing update or delete operations to prevent accidental data loss.

---

## Dependencies

- Python 3.10
- Flask
- Pydantic
- Pytest
- Locust

## Installation

Detailed installation steps for both Poetry and Conda are provided.

### Poetry

```bash
poetry install
poetry shell
```

### Conda

```bash
conda env create -f environment.yml
conda activate flask-app-employee
```

- Running the API

conda
```bash
flask run
```

poetry
```bash
poetry run flask run
```

For more comprehensive details, please refer to the [API Documentation](https://thiwankajayasiri.github.io/flask-api/app.html).

For detailed examples of API usage, please refer to the [usage documentation](api_usage.md).

---

## Testing

### Unit Testing

```bash
# For Poetry
poetry run pytest

# For Conda
python -m pytest
```

### Performance Testing

navigate to ```api-perf-testing``` directory
conda 

```bash
python -m locust
```

> [!NOTE]
> Navigate to `http://localhost:8089` to start the Locust performance test.
Sample performance test results can be found on the [performance_results](https://thiwankajayasiri.github.io/flask-api/docs/performance/report.html).


> [!WARNING]
> Due to some issues with Poetry, the performance test is not working with Poetry. Please use Conda for performance testing.
poetry
```bash
poetry run python -m locust
```

---

## Contact

For any further queries, feel free to reach out[^1].

---

[^1]: My reference. For more elaborate issues or technical questions, please refer to the [API Documentation](https://thiwankajayasiri.github.io/flask-api/app.html).
