from repositories.schedule_repository import ScheduleRepository
from src.schedule import Schedule

class InMemoryScheduleRepository(ScheduleRepository):
    def __init__(self):
        self._storage = {}

    def save(self, schedule: Schedule) -> None:
        self._storage[schedule.employee_id] = schedule

    def find_by_id(self, id: str) -> Schedule:
        return self._storage.get(id)

    def find_all(self) -> list:
        return list(self._storage.values())

    def delete(self, id: str) -> None:
        if id in self._storage:
            del self._storage[id]
