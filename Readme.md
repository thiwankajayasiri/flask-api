# Employee Management API

An easy-to-use, RESTful API for managing employees, built with Flask and Pydantic.

## Table of Contents

- [Description](#description)
- [Design Considerations](#design-considerations)
- [Dependencies](#dependencies)
- [Installation](#installation)
  - [Poetry](#poetry)
  - [Conda](#conda)
- [Usage](#usage)
  - [API Endpoints](#api-endpoints)
- [Testing](#testing)
  - [Unit Testing](#unit-testing)
  - [Performance Testing](#performance-testing)
- [Contact](#contact)

---

## Description

Manage a list of employees with CRUD operations. Each employee has an `id`, `first_name`, `last_name`, and `position`. Data is temporarily stored in an in-memory list.

---

## Design Considerations

- The API is designed to be RESTful, using appropriate HTTP methods.
- Utilizes Pydantic for data validation.
- Uses an in-memory list as a mock database.
- Supports both ```Poetry``` and ```Conda``` for dependency management.
- Tested with ```pytest```, ```pytest-flask```, and Locust.
- Includes a CI/CD pipeline via GitHub Actions.
- Code quality assured by ```flake8``` and ```mypy```.

---

## Dependencies

- Python 3.10
- Flask
- Pydantic
- Pytest
- Locust

---

## Installation

### Poetry

Install dependencies:

```bash
poetry install
```

Activate the virtual environment:

```bash
poetry shell
```

### Conda

Create and activate a new environment:

```bash
conda env create -f environment.yml
conda activate flask-app-employee
```

---

## Usage

To start the Flask app:

**UNIX and macOS:**

```bash
export FLASK_APP=app.py
flask run
```

**Windows:**

```bash
set FLASK_APP=app.py
flask run
```

### API Endpoints

- **Add**: `POST /employees`
- **Read All**: `GET /employees`
- **Read One**: `GET /employees/<id>`
- **Update**: `PUT /employees/<id>`
- **Delete**: `DELETE /employees/<id>`

Examples

- Add an employee:

```bash
curl -X POST http://127.0.0.1:5000/employees \
     -H "Content-Type: application/json" \
     -d '{"id": 2, "first_name": "Jane", "last_name": "Doe", "position": "Manager"}'

```

- Read all employees:

```bash
curl -X GET http://127.0.0.1:5000/employees
```

- Read employee by ID:

```bash
curl -X GET http://127.0.0.1:5000/employees/1
```


- Update an employee:

```bash
curl -X PUT http://127.0.0.1:5000/employees/1 \
     -H "Content-Type: application/json" \
     -d '{"first_name": "John", "last_name": "Smith", "position": "Senior Engineer"}'
```

- Delete an employee:

```bash
curl -X DELETE http://127.0.0.1:5000/employees/1

```

---

## Testing

### Unit Testing

Run unit tests:

**Poetry:**

```bash
poetry run pytest
```

**Conda:**

```bash
python -m pytest
```

Check coverage:

```bash
python -m pytest --cov=. test_app.py
```

### Performance Testing

We use [Locust](https://locust.io/) for performance tests. After installing Locust:

```bash
locust
```

Navigate to `http://localhost:8089` to start the test.