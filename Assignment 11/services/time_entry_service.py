# services/time_entry_service.py

from src.time_entry import TimeEntry
from src.time_entry_repository import TimeEntryRepository
from datetime import datetime

class TimeEntryService:
    def __init__(self, time_entry_repo: TimeEntryRepository):
        self.time_entry_repo = time_entry_repo

    def clock_in(self, employee_id: str):
        last_entry = self.time_entry_repo.get_last_entry_for_employee(employee_id)
        if last_entry and last_entry.clock_out is None:
            raise ValueError("Cannot clock in — employee is already clocked in.")

        entry = TimeEntry(employee_id, datetime.now(), None)
        self.time_entry_repo.save(entry)
        return entry

    def clock_out(self, employee_id: str):
        last_entry = self.time_entry_repo.get_last_entry_for_employee(employee_id)
        if not last_entry or last_entry.clock_out is not None:
            raise ValueError("Cannot clock out — no active session found.")

        last_entry.clock_out = datetime.now()
        self.time_entry_repo.update(last_entry)
        return last_entry

    def get_entries_for_employee(self, employee_id: str):
        return self.time_entry_repo.find_by_employee(employee_id)
