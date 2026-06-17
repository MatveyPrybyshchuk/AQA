from core.http_client import HttpClient
from models.user import UserResponse


class UsersService(HttpClient):
    SERVICE_URL = '/users'

    def headers(self, access_token: str):
        return {
            'Authorization': f'Bearer {access_token}',
            'accept': 'application/json'
        }


    def get_user_me(self, access_token):
        return UserResponse(**self.get(f'{self.SERVICE_URL}/me', headers=self.headers(access_token)))
    

    def get_list_of_users(self, access_token, max_in_list):
        users = self.get(f'{self.SERVICE_URL}/?skip=0&limit={max_in_list}', headers=self.headers(access_token))
        users_objects = [UserResponse(**user) for user in users]
        return users_objects
    

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


    def delete_user_by_id(self, access_token, user_id):
        return self.delete(f'{self.SERVICE_URL}/{user_id}', headers=self.headers(access_token))
    