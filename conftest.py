
import pytest

from services.auth_service import AuthentificationService


@pytest.fixture(scope = "session")
def admin_token():
    return AuthentificationService().login('admin@example.com', 'admin123').access_token
