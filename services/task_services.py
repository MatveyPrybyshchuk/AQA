from core.http_client import HttpClient
from models.task import TaskResponse


class TaskServices(HttpClient):
    SERVICE_URL = '/boards'

    def headers(self, access_token: str):
        return {
            'Authorization': f'Bearer {access_token}',
            'accept': 'application/json'
        }

    def create_task(self, access_token, board_id, title, description, status="todo", priority='medium', assignee_id=0):
        body = {
            "title": title,
            "description": description,
            "status": status,
            "priority": priority,
            "assignee_id": assignee_id
        }
        return TaskResponse(**self.post(f'{self.SERVICE_URL}/{board_id}/tasks', headers=self.headers(access_token), body=body))
    
    def search_task_on_board_by_id(self, access_token, board_id, task_id):
        return TaskResponse(**self.get(f'{self.SERVICE_URL}/{board_id}/tasks/{task_id}', headers=self.headers(access_token)))
    
    def get_list_of_tasks_on_board(self, access_token, board_id):
        tasks = self.get(f'{self.SERVICE_URL}/{board_id}/tasks', headers = self.headers(access_token))
        tasks_objects = [TaskResponse(**task) for task in tasks]
        return tasks_objects
    
    def delete_task_by_id(self, access_token, board_id, task_id):
        return self.delete(f'{self.SERVICE_URL}/{board_id}/tasks/{task_id}', headers=self.headers(access_token))
    