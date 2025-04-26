from repositories.employee_repository import EmployeeRepository
from src.employee import Employee

class InMemoryEmployeeRepository(EmployeeRepository):
    def __init__(self):
        self._storage = {}

    def save(self, employee: Employee) -> None:
        self._storage[employee._employee_id] = employee

    def find_by_id(self, id: str) -> Employee:
        return self._storage.get(id)

    def find_all(self) -> list:
        return list(self._storage.values())

    def delete(self, id: str) -> None:
        if id in self._storage:
            del self._storage[id]
