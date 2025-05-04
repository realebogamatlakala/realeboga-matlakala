# api/time_entry_api.py

from fastapi import APIRouter, HTTPException
from services.time_entry_service import TimeEntryService
from src.in_memory_time_entry_repository import InMemoryTimeEntryRepository

router = APIRouter()
time_entry_service = TimeEntryService(InMemoryTimeEntryRepository())

@router.post("/clock-in")
def clock_in(employee_id: str):
    try:
        return time_entry_service.clock_in(employee_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/clock-out")
def clock_out(employee_id: str):
    try:
        return time_entry_service.clock_out(employee_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{employee_id}")
def get_time_entries(employee_id: str):
    return time_entry_service.get_entries_for_employee(employee_id)
