from core.http_client import HttpClient
from models.board import BoardResponse


class BoardsService(HttpClient):
    SERVICE_URL = '/boards'

    def headers(self, access_token: str):
        return {
            'Authorization': f'Bearer {access_token}',
            'accept': 'application/json'
        }
    

    def add_member_to_board(self, access_token, board_id, user_id):
        return HttpClient().post(f'{self.SERVICE_URL}/{board_id}/members/{user_id}', headers=self.headers(access_token))
    

    def create_board(self, access_token, board_title, description, public_status=False):
        body = {
            "title": board_title,
            "description": description,
            "public": public_status
        }

        return BoardResponse(**self.post(f'{self.SERVICE_URL}/', headers=self.headers(access_token), body=body))
                                     

    def get_list_of_boards(self, access_token):
        boards = self.get(f'{self.SERVICE_URL}/?skip=0&limit=100&archived=false', headers=self.headers(access_token))
        boards_objects = [BoardResponse(**board) for board in boards]
        return boards_objects
    