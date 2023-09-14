import json
import pytest
import logging
from app import app, employees, Employee

# Configure logging
logging.basicConfig(level=logging.INFO)

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_employees(client):
    try:
        logging.info('Running test_get_employees')
        rv = client.get('/employees')
        assert rv.status_code == 200
        assert len(json.loads(rv.data)) == len(employees)
        logging.info('PASSED: test_get_employees')
    except AssertionError as e:
        logging.error('FAILED: test_get_employees')
        logging.error('Error Details: %s', e)
        raise

def test_add_employee(client):
    try:
        logging.info('Running test_add_employee')
        new_employee = {
            "id": 3,
            "first_name": "Mike",
            "last_name": "Johnson",
            "position": "Developer"
        }
        rv = client.post('/employees', json=new_employee)
        assert rv.status_code == 201
        assert json.loads(rv.data) == new_employee
        logging.info('PASSED: test_add_employee')
    except AssertionError as e:
        logging.error('FAILED: test_add_employee')
        logging.error('Error Details: %s', e)
        raise

def test_add_employee_with_existing_id(client):
    try:
        logging.info('Running test_add_employee_with_existing_id')
        existing_employee = {
            "id": 1,
            "first_name": "Michael",
            "last_name": "Johnson",
            "position": "Developer"
        }
        rv = client.post('/employees', json=existing_employee)
        assert rv.status_code == 409
        assert "Conflict" in json.loads(rv.data)["error"]
        logging.info('PASSED: test_add_employee_with_existing_id')
    except AssertionError as e:
        logging.error('FAILED: test_add_employee_with_existing_id')
        logging.error('Error Details: %s', e)
        raise

def test_update_existing_employee(client):
    try:
        logging.info('Running test_update_existing_employee')
        updated_employee = {
            "id": 1,
            "first_name": "John",
            "last_name": "Doe",
            "position": "Lead Engineer"
        }
        rv = client.put('/employees/1', json=updated_employee)
        assert rv.status_code == 200
        assert json.loads(rv.data)["data"]["position"] == "Lead Engineer"
        logging.info('PASSED: test_update_existing_employee')
    except AssertionError as e:
        logging.error('FAILED: test_update_existing_employee')
        logging.error('Error Details: %s', e)
        raise

def test_update_non_existing_employee(client):
    try:
        logging.info('Running test_update_non_existing_employee')
        updated_employee = {
            "first_name": "John",
            "last_name": "Doe",
            "position": "Lead Engineer"
        }
        rv = client.put('/employees/100', json=updated_employee)
        assert rv.status_code == 404
        assert "Not Found" in json.loads(rv.data)["error"]
        logging.info('PASSED: test_update_non_existing_employee')
    except AssertionError as e:
        logging.error('FAILED: test_update_non_existing_employee')
        logging.error('Error Details: %s', e)
        raise

def test_delete_existing_employee(client):
    try:
        logging.info('Running test_delete_existing_employee')
        rv = client.delete('/employees/1')
        assert rv.status_code == 200
        assert "Employee deleted" in json.loads(rv.data)["message"]
        logging.info('PASSED: test_delete_existing_employee')
    except AssertionError as e:
        logging.error('FAILED: test_delete_existing_employee')
        logging.error('Error Details: %s', e)
        raise

def test_delete_non_existing_employee(client):
    try:
        logging.info('Running test_delete_non_existing_employee')
        rv = client.delete('/employees/100')
        assert rv.status_code == 404
        assert "Not Found" in json.loads(rv.data)["error"]
        logging.info('PASSED: test_delete_non_existing_employee')
    except AssertionError as e:
        logging.error('FAILED: test_delete_non_existing_employee')
        logging.error('Error Details: %s', e)
        raise