# main.py

from fastapi import FastAPI
from api import employee_api, time_entry_api, schedule_api

app = FastAPI(title="Time Tracking System API")

app.include_router(employee_api.router, prefix="/employees")
app.include_router(time_entry_api.router, prefix="/time-entry")
app.include_router(schedule_api.router, prefix="/schedules")
