[![codecov](https://codecov.io/github/thiwankajayasiri/flask-api/graph/badge.svg?token=C1YSBULP4C)](https://codecov.io/github/thiwankajayasiri/flask-api)
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

## Project Considerations

- The API is designed to be RESTful, using appropriate HTTP methods.
- Utilizes Pydantic for data validation.
- Uses an in-memory list as a mock database.
- Supports both ```Poetry``` and ```Conda``` for dependency management.
- Tested with ```pytest```, ```pytest-flask```, and Locust.
- Includes a CI/CD pipeline via GitHub Actions.
- Code quality assured by ```flake8``` and ```mypy```.


## Flask API Design Considerations

When designing this API, I was ensuring that it not only conforms to RESTful principles but also includes additional features that make it robust, scalable, and user-friendly. Below are the design considerations that have been implemented in our API.

### General Considerations

1. **Versioning**: the API is versioned, making it future-proof for both the server and client. The endpoints start with `/v1/` to indicate that this is version 1 of our API.

2. **Pagination**: The `GET /employees` route supports pagination, offering a way to limit the number of records returned. This ensures that neither the server nor the client is overwhelmed.

3. **Filtering and Sorting**: I have added query parameters on the `GET /employees` endpoint, allowing for specific filtering and sorting of records.

4. **Rate Limiting**: To protect against abuse, rate limiting has been implemented across all API endpoints.

5. **Caching**: Our API employs caching strategies to minimize server load and speed up client requests.

6. **Throttling**: I’ve implemented throttling to further limit the number of API requests a user can make within a given timeframe.

7. **Logging and Monitoring**: Detailed logs are kept and monitoring is in place to ensure issues can be detected and resolved quickly.

### Endpoint-Specific Considerations

- **Add (POST /employees)**
  - The `id` is generated server-side, ensuring there are no conflicts.
  - Checks are in place to confirm that an employee with a given `id` or unique attribute doesn't already exist.

- **Read All (GET /employees)**
  - Metadata like the total number of employees is included in the response.

- **Read One (GET /employees/<id>)**
  - A 404 status code is returned if an employee with the given `id` doesn't exist.

- **Update (PUT /employees/<id>)**
  - A check is in place to ensure that an employee exists before attempting an update.
  - A 404 status code is returned if the employee doesn't exist, and a 200 or 204 status code is returned upon a successful update.

- **Delete (DELETE /employees/<id>)**
  - A check is in place to ensure that an employee exists before attempting a delete.
  - A 404 status code is returned if the employee doesn't exist, and a 200 or 204 status code is returned upon successful deletion.

By implementing these features, I believe the API offers a robust, scalable, and user-friendly experience.




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

For more information, please refer to the [API Documentation](https://thiwankajayasiri.github.io/flask-api/app.html).

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

- Add an employee(POST):

```bash
curl -X POST "http://localhost:5000/v1/employees" \
-H "Content-Type: application/json" \
-d '{
  "id": 1,
  "first_name": "John",
  "last_name": "Doe",
  "position": "Software Engineer"
}'


```

- Retrive all employees(GET):
```bash
curl -X GET "http://localhost:5000/v1/employees"
```


- Retrive all employees(GET) with pagination:

```bash
curl -X GET "http://localhost:5000/v1/employees?page=1&per_page=10"
```

- Read employee by ID:

```bash
curl -X GET http://localhost:5000/v1/employees/1
```


- Update an employee(PUT):

```bash
curl -X PUT "http://localhost:5000/v1/employees/1" \
-H "Content-Type: application/json" \
-d '{
  "id": 1,
  "first_name": "John",
  "last_name": "Jaya",
  "position": "Solution Architect"
}'
```

- Delete an employee(DELETE):

```bash
curl -X DELETE "http://localhost:5000/v1/employees/1"
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