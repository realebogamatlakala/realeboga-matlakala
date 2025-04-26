from repositories.employee_repository import EmployeeRepository
from src.employee import Employee

class DatabaseEmployeeRepository(EmployeeRepository):
    def save(self, entity: Employee) -> None:
        # TODO: Implement database save logic
        pass

    def find_by_id(self, id: str) -> Employee:
        # TODO: Implement database find logic
        pass

    def find_all(self) -> list:
        # TODO: Implement database find all logic
        pass

    def delete(self, id: str) -> None:
        # TODO: Implement database delete logic
        pass
