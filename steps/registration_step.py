from services.auth_service import AuthentificationService


def registration_user(user_name, email, password = "Qwerty123!"):
    response = AuthentificationService().registration_user(user_name, email, password)

    return response.access_token
