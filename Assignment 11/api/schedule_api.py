# api/schedule_api.py

from fastapi import APIRouter, HTTPException
from services.schedule_service import ScheduleService
from src.in_memory_schedule_repository import InMemoryScheduleRepository

router = APIRouter()
schedule_service = ScheduleService(InMemoryScheduleRepository())

@router.post("/")
def assign_schedule(employee_id: str, start_time: str, end_time: str):
    return schedule_service.assign_schedule(employee_id, start_time, end_time)

@router.get("/{employee_id}")
def get_schedule(employee_id: str):
    try:
        return schedule_service.get_schedule(employee_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
