# api/employee_api.py

from fastapi import APIRouter, HTTPException
from services.employee_service import EmployeeService
from src.in_memory_employee_repository import InMemoryEmployeeRepository

router = APIRouter()
employee_service = EmployeeService(InMemoryEmployeeRepository())

@router.post("/")
def create_employee(emp_id: str, name: str):
    try:
        return employee_service.create_employee(emp_id, name)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{emp_id}")
def get_employee(emp_id: str):
    try:
        return employee_service.get_employee(emp_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
