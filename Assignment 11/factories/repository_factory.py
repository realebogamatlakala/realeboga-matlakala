from repositories.inmemory.in_memory_employee_repository import InMemoryEmployeeRepository
from repositories.inmemory.in_memory_time_entry_repository import InMemoryTimeEntryRepository
from repositories.inmemory.in_memory_schedule_repository import InMemoryScheduleRepository

class RepositoryFactory:
    @staticmethod
    def get_employee_repository(storage_type="MEMORY"):
        if storage_type == "MEMORY":
            return InMemoryEmployeeRepository()
        else:
            raise ValueError(f"Unsupported storage type: {storage_type}")

    @staticmethod
    def get_time_entry_repository(storage_type="MEMORY"):
        if storage_type == "MEMORY":
            return InMemoryTimeEntryRepository()
        else:
            raise ValueError(f"Unsupported storage type: {storage_type}")

    @staticmethod
    def get_schedule_repository(storage_type="MEMORY"):
        if storage_type == "MEMORY":
            return InMemoryScheduleRepository()
        else:
            raise ValueError(f"Unsupported storage type: {storage_type}")
