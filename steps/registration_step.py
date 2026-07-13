import allure

from services.auth_service import AuthenticationService

allure.step("registration_user")
def registration_user(user_name, email, password = "Qwerty123!"):
    response = AuthenticationService().registration_user(user_name, email, password)

    return response.access_token
