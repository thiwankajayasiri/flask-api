# Examples for Using the Employee Management API

## Examples

- **Add an employee (POST)**:

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

- **Retrieve all employees (GET)**:

```bash
curl -X GET "http://localhost:5000/v1/employees"
```

- **Filter employees by position (GET)**:

```bash
curl -X 'GET' \
'http://localhost:5000/v1/employees?position=Developer' \
-H 'accept: application/json'
```

- **Sort employees by first name in ascending order (GET)**:

```bash
curl -X 'GET' \
'http://localhost:5000/v1/employees?sort=first_name&order=asc' \
-H 'accept: application/json'
```

- **Combine filters and sorting (GET)**:

```bash
curl -X 'GET' \
'http://localhost:5000/v1/employees?position=Developer&sort=first_name&order=asc' \
-H 'accept: application/json'
```

- **Retrieve all employees (GET) with pagination**:

```bash
curl -X GET "http://localhost:5000/v1/employees?page=1&per_page=10"
```

- **Read employee by ID (GET)**:

```bash
curl -X GET http://localhost:5000/v1/employees/1
```

- **Update an employee (PUT)**:

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

- **Delete an employee (DELETE)**:

```bash
curl -X DELETE "http://localhost:5000/v1/employees/1"
```