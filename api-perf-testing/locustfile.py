from locust import HttpUser, task, between

class EmployeeManagementUser(HttpUser):
    wait_time = between(1, 3)  # Wait time between requests in seconds

    # Create a new employee
    @task(1)
    def create_employee(self):
        payload = {
            "id": 5,
            "first_name": "Jane",
            "last_name": "Doe",
            "position": "Manager"
        }
        response = self.client.post("/v1/employees", json=payload)
        if response.status_code != 201:
            print(f"Failed to create employee: {response.status_code}")

    # Fetch all employees
    @task(2)
    def get_employees(self):
        response = self.client.get("/v1/employees")
        if response.status_code != 200:
            print(f"Failed to get employees: {response.status_code}")

    # Fetch a specific employee
    @task(3)
    def get_single_employee(self):
        response = self.client.get("/v1/employees/1")
        if response.status_code != 200:
            print(f"Failed to get single employee: {response.status_code}")

    # Update an existing employee
    @task(1)
    def update_employee(self):
        payload = {
            "id": 1,
            "first_name": "John",
            "last_name": "Doe",
            "position": "Senior Engineer"
        }
        response = self.client.put("/v1/employees/1", json=payload)
        if response.status_code != 200:
            print(f"Failed to update employee: {response.status_code}")

    # Delete an employee
    @task(1)
    def delete_employee(self):
        response = self.client.delete("/v1/employees/5")
        if response.status_code != 200:
            print(f"Failed to delete employee: {response.status_code}")
