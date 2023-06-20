import json


def test_create_conference(client,normal_user_token_headers):
    data = {
        "title": "SDE super",
        "description": "python",
        "start_time": "2022-03-20"
        }
    response = client.post("/conferences/create-conference/", data=data, headers=normal_user_token_headers)
    assert response.status_code == 200 
    assert response.json()["title"] == "SDE super"
    assert response.json()["description"] == "python"


def test_read_conference(client,normal_user_token_headers):    
    data = {
        "title": "SDE super",
        "description": "python",
        "start_time": "2022-03-20"
        }
    response = client.post("/conferences/create-conference/", data=data,headers=normal_user_token_headers)

    response = client.get("/conferences/get/1/")
    assert response.status_code == 200
    assert response.json()['title'] == "SDE super"
