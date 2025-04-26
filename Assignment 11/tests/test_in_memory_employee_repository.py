import unittest
from repositories.inmemory.in_memory_employee_repository import InMemoryEmployeeRepository
from src.employee import Employee

class TestInMemoryEmployeeRepository(unittest.TestCase):
    def test_save_and_find(self):
        repo = InMemoryEmployeeRepository()
        emp = Employee("E001", "John Doe")
        repo.save(emp)

        found = repo.find_by_id("E001")
        self.assertIsNotNone(found)
        self.assertEqual(found._name, "John Doe")

    def test_delete(self):
        repo = InMemoryEmployeeRepository()
        emp = Employee("E002", "Jane Doe")
        repo.save(emp)

        repo.delete("E002")
        self.assertIsNone(repo.find_by_id("E002"))

if __name__ == "__main__":
    unittest.main()
