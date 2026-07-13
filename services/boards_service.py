import allure

from core.http_client import HttpClient
from models.board import BoardResponse


class BoardsService(HttpClient):
    SERVICE_URL = '/boards'

    def headers(self, access_token: str):
        return {
            'Authorization': f'Bearer {access_token}',
            'accept': 'application/json'
        }

    @allure.step("Add member to board")
    def add_member_to_board(self, access_token, board_id, user_id):
        return HttpClient().post(f'{self.SERVICE_URL}/{board_id}/members/{user_id}', headers=self.headers(access_token))

    @allure.step("Create_board")
    def create_board(self, access_token, board_title, description, public_status=False):
        body = {
            "title": board_title,
            "description": description,
            "public": public_status
        }
        return BoardResponse(**self.post(f'{self.SERVICE_URL}/', headers=self.headers(access_token), body=body))

    @allure.step("Get list of all boards")
    def get_list_of_boards(self, access_token):
        boards = self.get(f'{self.SERVICE_URL}/?skip=0&limit=100&archived=false', headers=self.headers(access_token))
        boards_objects = [BoardResponse(**board) for board in boards]
        return boards_objects

    @allure.step("Get public board by id")
    def get_public_board_by_id(self, access_token, board_id):
        return BoardResponse(**self.get(f'{self.SERVICE_URL}/public/{board_id}', headers=self.headers(access_token)))

    @allure.step("Update board with new data")
    def update_board(self, access_token, board_id, title=None, description=None, public=None, archived=None):
        temp_data = {
            "title": title,
            "description": description,
            "public": public,
            "archived": archived
        }

        data = {}
        for k, v in temp_data.items():
            if v is not None:
                data[k] = v

        return BoardResponse(**self.put(f'{self.SERVICE_URL}/{board_id}', headers=self.headers(access_token), body=data))

    @allure.step("Get private board by id")
    def get_private_board_by_id(self, access_token, board_id):
        return BoardResponse(**self.get(f'{self.SERVICE_URL}/{board_id}', headers=self.headers(access_token)))

    @allure.step("Delete board by id")
    def delete_board_by_id(self, access_token, board_id):
        return self.delete(f'{self.SERVICE_URL}/{board_id}', headers=self.headers(access_token))
