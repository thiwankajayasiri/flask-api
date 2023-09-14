from flask import Flask, request, jsonify, make_response
from pydantic import BaseModel, Field, ValidationError
from typing import List
import logging
# Initialize Flask app
app = Flask(__name__)

# Initialize logging
logging.basicConfig(level=logging.DEBUG)


# Pydantic model to hold and validate employee information.
class Employee(BaseModel):
    id: int = Field(..., example=1)
    first_name: str = Field(..., example="John")
    last_name: str = Field(..., example="Doe")
    position: str = Field(..., example="Engineer")


# Data structure to hold employee data. Using a list for simplicity.
employees: List[Employee] = [
    Employee(id=1, first_name='John', last_name='Doe', position='Engineer'),
    Employee(id=2, first_name='Jane', last_name='Doe', position='Manager')
]


# Utility function to check if an employee ID already exists
def is_unique_id(employee_id: int) -> bool:
    for employee in employees:
        if employee.id == employee_id:
            return False
    return True


# ADD: Add a new employee
@app.route('/employees', methods=['POST'])
def add_employee():
    """
    Add a new employee.
    Validates the incoming data and ensures the employee ID is unique.
    Returns:
        JSON: New employee data if added successfully or an error message.
    """
    # Validate and construct an Employee object from JSON data
    try:
        new_employee = Employee(**request.json)

    except ValidationError as e:
        return make_response(jsonify({"error": "Bad Request", "message": str(e)}), 400)

    except Exception as e:
        return make_response(jsonify({"error": "Internal Server Error", "message": str(e)}), 500)

    # Check for unique ID and return 409 if ID already exists
    if not is_unique_id(new_employee.id):
        return make_response(jsonify({"error": "Conflict", "message": "Employee ID already exists"}), 409)
    # Add the new employee
    employees.append(new_employee)
    # Return the new employee data with HTTP status code 201 (Created)
    return make_response(jsonify(new_employee.dict()), 201)


# READ: Get all employees
# Simple endpoint to read all data. No validation required.
@app.route('/employees', methods=['GET'])
def get_employees():
    """
    Retrieve all existing employees.
    Returns:
        JSON: List of all employee data or error message.
    """
    try:
        # Retrieve all employee data and convert to list of dicts
        return make_response(jsonify([employee.dict() for employee in employees]), 200)

    except AttributeError as e:
        # AttributeError: One of the objects is missing the `dict()` method or similar
        return make_response(jsonify({"error": "Internal Server Error", "message": f"An attribute error occurred: {e}"}), 500)

    except Exception as e:
        # General Exception: Something else went wrong
        return make_response(jsonify({"error": "Internal Server Error", "message": f"An unexpected error occurred: {e}"}), 500)


# UPDATE: Update an existing employee
@app.route('/employees/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    """
    Update an existing employee by ID.
    Parameters:
        employee_id (int): Employee ID to update.
    Returns:
        JSON: Updated employee data or error message.
    """
    try:
        # Find employee by ID
        existing_employee = next((employee for employee in employees if employee.id == employee_id), None)
        # Return 404 if employee not found
        if existing_employee is None:
            return make_response(jsonify({"error": "Not Found", "message": "Employee not found"}), 404)
        # Create Employee object from JSON data
        updated_employee = Employee(**request.json)
        # Manually update existing employee data
        existing_employee.first_name = updated_employee.first_name
        existing_employee.last_name = updated_employee.last_name
        existing_employee.position = updated_employee.position
        # Return updated data
        return make_response(jsonify({"status": "success", "message": "Employee updated", "data": updated_employee.dict()}), 200)

    except KeyError as e:
        # KeyError: The JSON data is missing a necessary field
        print(f"KeyError: {e}")
        return make_response(jsonify({"error": "Bad Request", "message": f"Missing field {e}"}), 400)

    except ValueError as e:
        # ValueError: Data types are wrong or data is invalid in some other way
        print(f"ValueError: {e}")
        return make_response(jsonify({"error": "Bad Request", "message": "Invalid field value"}), 400)

    except Exception as e:
        # General Exception: Something else went wrong
        print(f"An unexpected error occurred: {e}")
        return make_response(jsonify({"error": "Internal Server Error", "message": "An unexpected error occurred"}), 500)

# DELETE: Delete an existing employee
@app.route('/employees/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    """
    Delete an employee by ID.
    Verifies the employee exists before deletion and removes it from the list.
    Returns:
        JSON: A success message if deleted, or an error message if not found.
    """
    try:
        # Find the existing employee by ID
        existing_employee = next((employee for employee in employees if employee.id == employee_id), None)

        # If the employee does not exist, return a 404 error
        if existing_employee is None:
            return make_response(jsonify({"error": "Not Found", "message": "Employee not found"}), 404)

        # Remove the existing employee
        employees.remove(existing_employee)

        # Return a success message with HTTP status code 200 (OK)
        return make_response(jsonify({"message": "Employee deleted"}), 200)
    except Exception as e:
        # Log the exception for debugging
        print(f"An unexpected error occurred: {e}")

        # Return a generic internal server error with HTTP status code 500
        return make_response(jsonify({"error": "Internal Server Error", "message": f"An unexpected error occurred: {e}"}), 500)


# Optional endpoint to get a single employee by ID
@app.route('/employees/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    """
    Retrieve an employee by their ID.
    Parameters:
        - employee_id (int): The ID of the employee to retrieve
    Returns:
        - JSON object containing the employee information and success status, or an error message if not found.
    """
    # Filter the list of employees to find the employee with the given ID
    matching_employees = [employee.dict() for employee in employees if employee.id == employee_id]

    # If no matching employee is found, return a 404 error
    if len(matching_employees) == 0:
        return make_response(jsonify({"status": "error", "message": "Employee not found"}), 404)
    # Return a success message with HTTP status code 200 (OK)
    return make_response(jsonify({"status": "success", "message": "Employee found", "data": matching_employees[0]}), 200)


if __name__ == '__main__':
    app.run(debug=True)
