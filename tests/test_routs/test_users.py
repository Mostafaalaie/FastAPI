from fastapi import Response

def test_create_user(client):
    data = {"username":"testuser5","email":"testuser5@nofoobar.com","password":"testuser5secret"}
    #data = {"email":"testuser@nofoobar.com","password":"testing"}
    #response = client.post("/users/",json.dumps(data))
    response = client.post("/users/users",params=data)
    assert response.status_code == 200 
    assert response.body["email"] == "testuser5@nofoobar.com"
    assert response.json()["is_active"] == True