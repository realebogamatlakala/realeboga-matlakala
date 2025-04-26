from .repository import Repository
from src.employee import Employee

class EmployeeRepository(Repository[Employee, str]):
    pass
