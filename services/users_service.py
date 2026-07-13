import allure

from core.http_client import HttpClient
from models.user import UserResponse


class UsersService(HttpClient):
    SERVICE_URL = '/users'

    def headers(self, access_token: str):
        return {
            'Authorization': f'Bearer {access_token}',
            'accept': 'application/json'
        }

    @allure.step("Get user information")
    def get_user_me(self, access_token):
        return UserResponse(**self.get(f'{self.SERVICE_URL}/me', headers=self.headers(access_token)))

    @allure.step("Get list of users")
    def get_list_of_users(self, access_token, max_in_list = 100):
        users = self.get(f'{self.SERVICE_URL}/?skip=0&limit={max_in_list}', headers=self.headers(access_token))
        users_objects = [UserResponse(**user) for user in users]
        return users_objects

    @allure.step("Update user wuth new data")
    def update_user(self, access_token, user_id, username=None, email=None, role=None, avatar_url=None):
        temp_data = {
            "username": username,
            "email": email,
            "role": role,
            "avatar_url": avatar_url
        }

        data = {}
        for k, v in temp_data.items():
            if v is not None:
                data[k] = v

        return UserResponse(**self.put(f'{self.SERVICE_URL}/{user_id}', headers=self.headers(access_token), body=data))

    @allure.step("Delete user by id")
    def delete_user_by_id(self, access_token, user_id):
        return self.delete(f'{self.SERVICE_URL}/{user_id}', headers=self.headers(access_token))

    @allure.step("Get user info by id")
    def get_user_by_id(self, access_token, user_id):
        return UserResponse(**self.get(f'{self.SERVICE_URL}/{user_id}', headers=self.headers(access_token)))
