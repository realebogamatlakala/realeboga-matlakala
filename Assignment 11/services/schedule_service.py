# services/schedule_service.py

from src.schedule_repository import ScheduleRepository
from src.schedule import Schedule

class ScheduleService:
    def __init__(self, schedule_repo: ScheduleRepository):
        self.schedule_repo = schedule_repo

    def assign_schedule(self, employee_id: str, start_time: str, end_time: str):
        schedule = Schedule(employee_id, start_time, end_time)
        self.schedule_repo.save(schedule)
        return schedule

    def get_schedule(self, employee_id: str):
        schedule = self.schedule_repo.find_by_employee(employee_id)
        if not schedule:
            raise ValueError("No schedule assigned for employee.")
        return schedule
