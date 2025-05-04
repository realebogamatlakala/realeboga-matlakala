# tests/test_api_employee.py

import pytest
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_create_and_get_employee():
    async with AsyncClient(app=app, base_url="http://test") as client:
        resp = await client.post("/employees/", params={"emp_id": "E100", "name": "Alice"})
        assert resp.status_code == 200
        data = resp.json()
        assert data["emp_id"] == "E100"

        get_resp = await client.get("/employees/E100")
        assert get_resp.status_code == 200
