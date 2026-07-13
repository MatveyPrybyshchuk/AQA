import pytest
import allure

from services.auth_service import AuthenticationService
from services.users_service import UsersService
from test_data.get_random_user import get_random_user
from helper.helper import check_presence_by_id

@allure.feature("TestAuth")
class TestAuth:
    @allure.title("test_register_new_admin")
    @allure.description("Registration of a new admin")
    @allure.tag("smoke")
    @pytest.mark.skip(reason="Регистрация первого администратора. Доступно только если в системе нет ни одного пользователя.")
    def test_register_new_admin(self):
        admin_token = AuthenticationService().registration_user(*get_random_user(), user_type="-admin")
        admin_info = UsersService().get_user_me(admin_token.access_token)

        list_of_users = UsersService().get_list_of_users(admin_token.access_token, 100)

        # Проверяем наличие созданного юзера по id
        check_presence_by_id(list_of_users, admin_info.id)

        UsersService().delete_user_by_id(admin_token.access_token, user_id=admin_info.id)

    @allure.title("test_register_new_user")
    @allure.description("Registration of a new user")
    @allure.tag("smoke")
    @pytest.mark.test_auth
    def test_register_new_user(self):
        user_token = AuthenticationService().registration_user(*get_random_user())
        user_info = UsersService().get_user_me(user_token.access_token)

        list_of_users = UsersService().get_list_of_users(user_token.access_token, 100)

        # Проверяем наличие созданного юзера по id
        check_presence_by_id(list_of_users, user_info.id)

    @allure.title("test_register_new_guest")
    @allure.description("Registration of a new guest")
    @allure.tag("smoke")
    @pytest.mark.test_auth
    def test_register_new_guest(self):
        guest_token = AuthenticationService().registration_user(*get_random_user())
        guest_info = UsersService().get_user_me(guest_token.access_token)

        list_of_users = UsersService().get_list_of_users(guest_token.access_token, 100)

        # Проверяем наличие созданного юзера по id
        check_presence_by_id(list_of_users, guest_info.id)
