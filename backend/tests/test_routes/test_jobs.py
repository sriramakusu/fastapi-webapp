import json
from datetime import datetime

def test_create_job(client):
    data = {
        "title": "SDE super",
        "company": "doogle",
        "company_url": "www.doogle.com",
        "location": "USA,NY",
        "description": "python",
        "date_posted": "2022-03-20" # this is giving an error. need to work out.
        }
    response = client.post("/jobs/create-job/", json = data)
    assert response.status_code == 200 
    assert response.json()["company"] == "doogle"
    assert response.json()["description"] == "python"