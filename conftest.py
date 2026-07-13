from pytest import fixture
from requests import HTTPError
from faker import Faker
from services.auth_service import AuthenticationService
from services.users_service import UsersService
from services.boards_service import BoardsService
from test_data.get_random_user import get_random_user


@fixture
def admin_token():
    token = AuthenticationService().login('admin@example.com', 'admin123')
    yield token.access_token

@fixture
def random_user(token: str):
    user_token = AuthenticationService().registration_user(*get_random_user())
    user_info = UsersService().get_user_me(user_token.access_token)

    yield user_token.access_token, user_info

    try:
        UsersService().delete_user_by_id(token, user_id=user_info.id)
    except HTTPError as e:
        if e.response.status_code != 404:
            raise

@fixture
def restore_admin_data(token):
    admin_info = UsersService().get_user_me(token)

    yield

    UsersService().update_user(token, user_id=admin_info.id, username="admin", email='admin@example.com')

@fixture
def random_public_board(token):
    admin_info = UsersService().get_user_me(token)
    board_title = Faker().name()
    description = Faker().name()

    new_board = BoardsService().create_board(token, board_title=board_title, description=description, public_status=True)

    yield new_board, board_title, description, admin_info.id

    BoardsService().delete_board_by_id(token, board_id=new_board.id)

@fixture
def random_private_board(token):
    admin_info = UsersService().get_user_me(token)
    board_title = Faker().name()
    description = Faker().name()

    new_board = BoardsService().create_board(token, board_title=board_title, description=description, public_status=False)

    yield new_board, board_title, description, admin_info.id

    BoardsService().delete_board_by_id(token, board_id=new_board.id)

@fixture
def random_public_board_by_user(user):
    user_token, user_info = user

    board_title = Faker().name()
    description = Faker().name()

    new_board = BoardsService().create_board(user_token, board_title=board_title, description=description, public_status=True)

    yield user_token, new_board, board_title, description, user_info.id

    BoardsService().delete_board_by_id(user_token, board_id=new_board.id)

@fixture
def random_private_board_by_user(user):
    user_token, user_info = user

    board_title = Faker().name()
    description = Faker().name()

    new_board = BoardsService().create_board(user_token, board_title=board_title, description=description, public_status=False)

    yield user_token, new_board, board_title, description, user_info.id

    BoardsService().delete_board_by_id(user_token, board_id=new_board.id)
