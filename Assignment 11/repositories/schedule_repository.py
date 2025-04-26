from .repository import Repository
from src.schedule import Schedule

class ScheduleRepository(Repository[Schedule, str]):
    pass
