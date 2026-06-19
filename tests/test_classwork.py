import json

import pytest
import requests



# @pytest.mark.api
# def test_health_check():
#     response = requests.get('http://localhost:8000/')
#     assert response.status_code == 200

#     response_json = response.json()

#     assert response_json['message'] == 'Task Management System API'
#     assert response_json['version'] ==  '1.0.0'
#     assert response_json['docs'] ==  '/docs'
#     assert response_json['redoc'] ==  '/redoc'
#     assert response_json['health'] ==  '/health'


@pytest.mark.regis
def test_register():
    body = json.dumps({
        "username": "user2@example.com",
        "email": "user2@example.com",
        "password": "Qwerty123!",
    })

    response = requests.post('http://localhost:8000/auth/register', data = body)
    breakpoint()

    assert response.status_code == 201
