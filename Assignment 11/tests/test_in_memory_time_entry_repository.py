import unittest
from repositories.inmemory.in_memory_time_entry_repository import InMemoryTimeEntryRepository
from src.time_entry import TimeEntry

class TestInMemoryTimeEntryRepository(unittest.TestCase):
    def test_save_and_find(self):
        repo = InMemoryTimeEntryRepository()
        time_entry = TimeEntry("T001", "2024-04-01", 8)
        repo.save(time_entry)

        found = repo.find_by_id("T001")
        self.assertIsNotNone(found)
        self.assertEqual(found.hours, 8)

    def test_delete(self):
        repo = InMemoryTimeEntryRepository()
        time_entry = TimeEntry("T002", "2024-04-02", 6)
        repo.save(time_entry)

        repo.delete("T002")
        self.assertIsNone(repo.find_by_id("T002"))

if __name__ == "__main__":
    unittest.main()
