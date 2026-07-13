import allure
from core.http_client import HttpClient
from models.token import TokenResponse


class AuthenticationService(HttpClient):
    SERVICE_URL = '/auth'
    @allure.step("Registration of a new user")
    def registration_user(self, username, email, password, user_type = "") -> TokenResponse:
        body = {
            "username": username,
            "email": email,
            "password": password,
        }

        return TokenResponse(**self.post(f'{self.SERVICE_URL}/register{user_type}', body=body))
    @allure.step("Logging into app")
    def login(self, email, password) -> TokenResponse:
        body ={
            "email": email,
            "password": password
        }

        return TokenResponse(**HttpClient().post(f'{self.SERVICE_URL}/login', body=body))
    