from faker import Faker
from services.task_service import TaskService


def create_fake_task_on_board(access_token, board_id):

    task_description = Faker().user_name()
    task_title = Faker().user_name()

    created_task = TaskService().create_task(access_token, board_id, title=task_title, description=task_description)

    return task_title, task_description, created_task
