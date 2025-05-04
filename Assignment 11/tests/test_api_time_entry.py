# tests/test_api_time_entry.py

import pytest
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_clock_in_and_out():
    async with AsyncClient(app=app, base_url="http://test") as client:
        await client.post("/employees/", params={"emp_id": "E101", "name": "Bob"})

        in_resp = await client.post("/time-entry/clock-in", params={"employee_id": "E101"})
        assert in_resp.status_code == 200

        out_resp = await client.post("/time-entry/clock-out", params={"employee_id": "E101"})
        assert out_resp.status_code == 200

        list_resp = await client.get("/time-entry/E101")
        assert len(list_resp.json()) >= 1
