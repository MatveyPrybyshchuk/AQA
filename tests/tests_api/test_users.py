import pytest, allure

from typing import Tuple
from faker import Faker
from services.auth_service import TokenResponse
from services.users_service import UsersService, UserResponse

@allure.feature("TestUsers")
class TestUsers:
    @allure.title("test_update_user_email")
    @allure.description("Update user's email")
    @allure.tag("smoke")
    @pytest.mark.test_users
    def test_update_user_email(self, admin_token:str, random_user: Tuple[TokenResponse, UserResponse]):
        _, user_info = random_user

        new_email = Faker().email()
        UsersService().update_user(admin_token, user_id=user_info.id, email=new_email)

        updated_user  = UsersService().get_user_by_id(admin_token, user_info.id)

        assert updated_user.email == new_email

    @allure.title("test_update_user_username")
    @allure.description("Update user's username")
    @allure.tag("smoke")
    @pytest.mark.test_users
    def test_update_user_username(self, admin_token:str, random_user: Tuple[TokenResponse, UserResponse]):
        _, user_info = random_user

        new_username = Faker().name()
        UsersService().update_user(admin_token, user_id=user_info.id, username=new_username)

        updated_user  = UsersService().get_user_by_id(admin_token, user_info.id)

        assert updated_user.username == new_username

    @allure.title("test_update_user_avatar")
    @allure.description("Update user's avatar")
    @allure.tag("smoke")
    @pytest.mark.test_users
    def test_update_user_avatar(self, admin_token:str, random_user: Tuple[TokenResponse, UserResponse]):
        _, user_info = random_user

        new_avatar = Faker().name()
        UsersService().update_user(admin_token, user_id=user_info.id, avatar_url=new_avatar)

        updated_user  = UsersService().get_user_by_id(admin_token, user_info.id)

        assert updated_user.avatar_url == new_avatar

    @allure.title("test_update_admin_username")
    @allure.description("Update admins's username")
    @allure.tag("critical")
    @pytest.mark.test_users
    def test_update_admin_username(self, admin_token):
        admin_info = UsersService().get_user_me(admin_token)

        new_username = Faker().email()
        UsersService().update_user(admin_token, user_id=admin_info.id, username=new_username)

        updated_admin  = UsersService().get_user_by_id(admin_token, admin_info.id)

        assert updated_admin.username == new_username

    @allure.title("test_update_admin_email")
    @allure.description("Update admins's email")
    @allure.tag("critical")
    @pytest.mark.test_users
    def test_update_admin_email(self, admin_token, restore_admin_data):
        admin_info = UsersService().get_user_me(admin_token)

        new_email = Faker().email()
        UsersService().update_user(admin_token, user_id=admin_info.id, email=new_email)

        updated_admin  = UsersService().get_user_by_id(admin_token, admin_info.id)

        assert updated_admin.email == new_email

    @allure.title("test_update_admin_avatar")
    @allure.description("Update admins's avatar")
    @allure.tag("critical")
    @pytest.mark.test_users
    def test_update_admin_avatar(self, admin_token):
        admin_info = UsersService().get_user_me(admin_token)

        new_avatar = Faker().name()
        UsersService().update_user(admin_token, user_id=admin_info.id, avatar_url=new_avatar)

        updated_admin  = UsersService().get_user_by_id(admin_token, admin_info.id)

        assert updated_admin.avatar_url == new_avatar

    @allure.title("test_delete_user_by_admin")
    @allure.description("Delete user by admin")
    @allure.tag("critical")
    @pytest.mark.test_users1
    def test_delete_user_by_admin(self, admin_token, random_user: Tuple[TokenResponse, UserResponse]):
        _, user_info = random_user

        UsersService().delete_user_by_id(admin_token, user_id=user_info.id)

        list_of_users = UsersService().get_list_of_users(admin_token, 100)

        assert not any(user.id == user_info.id for user in list_of_users)
