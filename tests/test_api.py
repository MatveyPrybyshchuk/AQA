from faker import Faker
import pytest

from helper.helper import check_presence_by_id
from services.auth_service import AuthentificationService
from services.boards_service import BoardsService
from services.task_service import TaskService
from services.users_service import UsersService
from steps.board_steps import create_board
from steps.registration_step import registration_user
from steps.task_steps import create_fake_task_on_board

"""
1 Создать HttpClient
2 Написать автоесты Users( users, user_update, delete user)
3 Написать автоесты Tasks( task search, create task, delete task)
4 1 тест Users и 1 тест Tasks должен с параметризацией - 3-4 варианты (граничные значения и классы эквавилентности)

* Pydantic 
"""

@pytest.mark.test_api
def test_get_list_of_users(admin_token):
    user_service = UsersService()

    length_before = len(user_service.get_list_of_users(admin_token, max_in_list = 100))

    registration_user(Faker().user_name(), Faker().email())

    length_after = len(user_service.get_list_of_users(admin_token, max_in_list = 100))
    
    assert length_before == length_after - 1


# Допустим где-то в доках указано, что мин длина имени пользователя в emal = 1, а макс = 10. По классам я поверю 1, 2, 9, 10
@pytest.mark.parametrize("email", ["1@example.com", "22@example.com", "999999999@example.com", "1000000000@example.com"])
@pytest.mark.test_api
def test_update_user_email(admin_token, email):
    user_service = UsersService()
    email_before = Faker().email()
    
    new_user = AuthentificationService().registration_user(Faker().user_name(), email_before, 'test123')
    user_info = user_service.get_user_me(new_user.access_token)

    user_service.update_user(admin_token, user_id=user_info.id, email=email)

    user_info = user_service.get_user_me(new_user.access_token)
    assert user_info.email == email
    

@pytest.mark.test_api
def test_delete_user(admin_token):
    user_service = UsersService()
    # Получаем нового юзера
    new_user = AuthentificationService().registration_user(Faker().user_name(), Faker().email(), 'test123')
    user_info = user_service.get_user_me(new_user.access_token)

    # Проверяем id юзера до удаления
    users_before = user_service.get_list_of_users(admin_token, 100)
    check_presence_by_id(users_before, user_info.id)

    # Удаляем юзера по id
    user_service.delete_user_by_id(admin_token, user_id=user_info.id)

    # Проверяем id юзера после удаления
    users_after = user_service.get_list_of_users(admin_token, 100)
    check_presence_by_id(users_after, user_info.id, present=False)


@pytest.mark.test_api
def test_search_task_on_board_by_id(admin_token):
    created_board = BoardsService().create_board(admin_token, Faker().user_name(), Faker().user_name(), public_status = True)

    task_title, task_description, created_task = create_fake_task_on_board(admin_token, created_board.id)

    find_created_task = TaskService().search_task_on_board_by_id(admin_token, created_board.id, created_task.id)

    assert find_created_task.description == task_description
    assert find_created_task.title == task_title
    assert find_created_task.board_id == created_board.id
    

# Допустим есть лимит на количество тасок в борде - 5 ПРоверяю 1, 2, 3, 4, 5, чтобы и классы и граничные
@pytest.mark.parametrize("task_num", [1, 2, 3, 4, 5])
@pytest.mark.test_api
def test_create_task(admin_token, task_num):
    created_board = BoardsService().create_board(admin_token, Faker().user_name(), Faker().user_name(), public_status = True)

    for _ in range (task_num):
        task_title, task_description, created_task = create_fake_task_on_board(admin_token, created_board.id)

        assert created_task.description == task_description
        assert created_task.title == task_title
        assert created_task.board_id == created_board.id


@pytest.mark.test_api
def test_delete_task(admin_token):
    task_service = TaskService()

    created_board = create_board(admin_token)
    _, _, created_task = create_fake_task_on_board(admin_token, created_board.id)

    # Проверяем наличие таски
    tasks_before = task_service.get_list_of_tasks_on_board(admin_token, created_board.id)
    check_presence_by_id(tasks_before, created_task.id)

    # Удаляем таску
    task_service.delete_task_by_id(admin_token, board_id=created_board.id, task_id=created_task.id)
 
    # Проверяем наличие таски
    tasks_after = task_service.get_list_of_tasks_on_board(admin_token, created_board.id)
    check_presence_by_id(tasks_after, created_task.id, present=False)
