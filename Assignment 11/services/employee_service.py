# services/employee_service.py

from src.employee_repository import EmployeeRepository
from src.employee import Employee

class EmployeeService:
    def __init__(self, employee_repo: EmployeeRepository):
        self.employee_repo = employee_repo

    def create_employee(self, emp_id: str, name: str):
        if self.employee_repo.find_by_id(emp_id):
            raise ValueError("Employee already exists")
        employee = Employee(emp_id, name)
        self.employee_repo.save(employee)
        return employee

    def get_employee(self, emp_id: str):
        employee = self.employee_repo.find_by_id(emp_id)
        if not employee:
            raise ValueError("Employee not found")
        return employee
