import unittest
from repositories.inmemory.in_memory_schedule_repository import InMemoryScheduleRepository
from src.schedule import Schedule

class TestInMemoryScheduleRepository(unittest.TestCase):
    def test_save_and_find(self):
        repo = InMemoryScheduleRepository()
        schedule = Schedule("E001", ["Monday", "Tuesday"], "09:00", "17:00")
        repo.save(schedule)

        found = repo.find_by_id("E001")
        self.assertIsNotNone(found)
        self.assertEqual(found.shift_start, "09:00")
        self.assertEqual(found.shift_end, "17:00")

    def test_delete(self):
        repo = InMemoryScheduleRepository()
        schedule = Schedule("E002", ["Wednesday"], "10:00", "18:00")
        repo.save(schedule)

        repo.delete("E002")
        self.assertIsNone(repo.find_by_id("E002"))

if __name__ == "__main__":
    unittest.main()
