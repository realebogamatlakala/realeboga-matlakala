from repositories.time_entry_repository import TimeEntryRepository
from src.time_entry import TimeEntry

class InMemoryTimeEntryRepository(TimeEntryRepository):
    def __init__(self):
        self._storage = {}

    def save(self, time_entry: TimeEntry) -> None:
        self._storage[time_entry.entry_id] = time_entry

    def find_by_id(self, id: str) -> TimeEntry:
        return self._storage.get(id)

    def find_all(self) -> list:
        return list(self._storage.values())

    def delete(self, id: str) -> None:
        if id in self._storage:
            del self._storage[id]
