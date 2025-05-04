# tests/test_api_schedule.py

import pytest
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_schedule_assignment():
    async with AsyncClient(app=app, base_url="http://test") as client:
        await client.post("/employees/", params={"emp_id": "E102", "name": "Charlie"})

        resp = await client.post(
            "/schedules/",
            params={"employee_id": "E102", "start_time": "09:00", "end_time": "17:00"}
        )
        assert resp.status_code == 200

        get_resp = await client.get("/schedules/E102")
        assert get_resp.status_code == 200
        assert get_resp.json()["start_time"] == "09:00"
