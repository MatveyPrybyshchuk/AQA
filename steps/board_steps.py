import allure

from faker import Faker
from services.auth_service import AuthenticationService
from services.users_service import UsersService
from services.boards_service import BoardsService
from steps.registration_step import registration_user

@allure.step("add_new_member_to_step_by_admin")
def add_new_member_to_step_by_admin(board_id):
    admin_token = AuthenticationService().login('admin@example.com', 'admin123')

    new_user_token = registration_user(Faker().user_name(), Faker().email(), "Qwerty123!")
    user_info = UsersService().get_user_me(new_user_token)

    return BoardsService().add_member_to_board(admin_token.access_token, board_id=board_id, user_id=user_info.id)

@allure.step("create_board")
def create_board(access_token):
    return BoardsService().create_board(access_token, Faker().user_name(), Faker().user_name(), public_status = True)
