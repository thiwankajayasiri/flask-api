# Flask API Design Decisions

## Introduction

This document outlines the key design decisions taken in building our Flask API for managing employees.

## Rate Limiting

We use the Flask-Limiter package to add rate-limiting functionality to our API, helping to prevent abuse.

- POST to `/v1/employees`: Limited to 4 requests per minute.
- GET from `/v1/employees`: Limited to 30 requests per minute.
- PUT to `/v1/employees/{id}`: Limited to 2 requests per minute.
- DELETE from `/v1/employees/{id}`: Limited to 2 requests per minute.

## Caching

We use a custom caching mechanism to improve the performance of the API.

- The list of all employees is cached for 100 seconds.
- The cache is invalidated whenever an employee is added or updated.

## Pagination, Sorting, and Filtering

The `GET /v1/employees` API supports pagination, sorting, and filtering:

- Pagination is supported with `page` and `per_page` query parameters.
- Filtering by position is available via the `position` query parameter.
- Sorting is supported via the `sort_by` and `order` query parameters.

## Validation

We use Pydantic for data validation to ensure that the received JSON payloads conform to the expected structure. Validation errors will result in a 400 Bad Request response.

## Exception Handling

In each API endpoint, we have multiple exception-handling mechanisms to provide informative error messages and appropriate HTTP status codes.

## Conclusion

By adhering to RESTful principles and employing caching, rate-limiting, and validation mechanisms, we aim to build a robust, efficient, and user-friendly API.


---

# Employee API Sequence Diagram

---

## Table of Contents

1. [Creating Employee](#creating-employee)
2. [Fetching All Employees](#fetching-all-employees)
3. [Updating an Employee](#updating-an-employee)
4. [Deleting an Employee](#deleting-an-employee)

---

## Creating Employee

- **Actor**: Client
- **Receiver**: Server
- **Action**: POST /v1/employees
- <span style="color:green">**Server State**: Activated</span>
- **Notes**: Validate the request
- **Server Responses**:
  - <span style="color:blue">201 Created</span> (if successful)
  - <span style="color:red">400 Bad Request</span> (if failure)
  - <span style="color:orange">500 Internal Server Error</span> (if server error)
- <span style="color:gray">**Server State**: Deactivated</span>

---

## Fetching All Employees

- **Actor**: Client
- **Receiver**: Server
- **Action**: GET /v1/employees
- <span style="color:green">**Server State**: Activated</span>
- **Server Responses**:
  - <span style="color:blue">200 OK</span> (if successful)
  - <span style="color:red">400 Bad Request</span> (if failure)
  - <span style="color:orange">500 Internal Server Error</span> (if server error)
- <span style="color:gray">**Server State**: Deactivated</span>

---

## Updating an Employee

- **Actor**: Client
- **Receiver**: Server
- **Action**: PUT /v1/employees/{id}
- <span style="color:green">**Server State**: Activated</span>
- **Server Responses**:
  - <span style="color:blue">200 OK</span> (if successful)
  - <span style="color:purple">404 Not Found</span> (if not found)
  - <span style="color:red">400 Bad Request</span> (if failure)
  - <span style="color:orange">500 Internal Server Error</span> (if server error)
- <span style="color:gray">**Server State**: Deactivated</span>

---

## Deleting an Employee

- **Actor**: Client
- **Receiver**: Server
- **Action**: DELETE /v1/employees/{id}
- <span style="color:green">**Server State**: Activated</span>
- **Server Responses**:
  - <span style="color:blue">200 OK</span> (if successful)
  - <span style="color:purple">404 Not Found</span> (if not found)
  - <span style="color:orange">500 Internal Server Error</span> (if server error)
- <span style="color:gray">**Server State**: Deactivated</span>

