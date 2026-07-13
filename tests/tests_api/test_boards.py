import pytest, allure
from faker import Faker
from services.boards_service import BoardsService

@allure.feature("TestBoards")
class TestBoards:
    @allure.title("test_create_public_board_by_user")
    @allure.description("Create public board bu user")
    @allure.tag("smoke")
    @pytest.mark.test_boards
    def test_create_public_board_by_user(self, random_public_board_by_user):
        user_token, new_board, board_title, description, created_by = random_public_board_by_user

        board_info = BoardsService().get_public_board_by_id(user_token, new_board.id)

        assert board_info.title == board_title
        assert board_info.description == description
        assert board_info.public
        assert board_info.created_by == created_by

    @allure.title("test_create_private_board_by_user")
    @allure.description("Create private board by user")
    @allure.tag("smoke")
    @pytest.mark.test_boards
    def test_create_private_board_by_user(self, random_private_board_by_user):
        user_token, new_board, board_title, description, created_by = random_private_board_by_user

        board_info = BoardsService().get_private_board_by_id(user_token, new_board.id)

        assert board_info.title == board_title
        assert board_info.description == description
        assert not board_info.public
        assert board_info.created_by == created_by

    @allure.title("test_update_public_board_title_by_user")
    @allure.description("Update public board title by user")
    @allure.tag("smoke")
    @pytest.mark.test_boards
    def test_update_public_board_title_by_user(self, random_public_board_by_user):
        user_token, new_board, board_title, description, created_by = random_public_board_by_user

        board_before_update = BoardsService().get_public_board_by_id(user_token, new_board.id)

        assert board_before_update.title == board_title
        assert board_before_update.description == description
        assert board_before_update.public
        assert board_before_update.created_by == created_by

        board_title = Faker().name()
        BoardsService().update_board(user_token, board_id=new_board.id, title=board_title)

        board_after_update = BoardsService().get_public_board_by_id(user_token, new_board.id)

        assert board_after_update.title == board_title
        assert board_after_update.description == description
        assert board_after_update.public
        assert board_after_update.created_by == created_by

    @allure.title("test_update_private_board_title_by_user")
    @allure.description("Update private board title by user")
    @allure.tag("smoke")
    @pytest.mark.test_boards
    def test_update_private_board_title_by_user(self, random_private_board_by_user):
        user_token, new_board, board_title, description, created_by = random_private_board_by_user

        board_before_update = BoardsService().get_private_board_by_id(user_token, new_board.id)

        assert board_before_update.title == board_title
        assert board_before_update.description == description
        assert not board_before_update.public
        assert board_before_update.created_by == created_by

        board_title = Faker().name()
        BoardsService().update_board(user_token, board_id=new_board.id, title=board_title)

        board_after_update = BoardsService().get_private_board_by_id(user_token, new_board.id)

        assert board_after_update.title == board_title
        assert board_after_update.description == description
        assert not board_after_update.public
        assert board_after_update.created_by == created_by

    @allure.title("test_update_public_board_description_by_user")
    @allure.description("Update public board description by user")
    @allure.tag("smoke")
    @pytest.mark.test_boards
    def test_update_public_board_description_by_user(self, random_public_board_by_user):
        user_token, new_board, board_title, description, created_by = random_public_board_by_user

        board_before_update = BoardsService().get_public_board_by_id(user_token, new_board.id)

        assert board_before_update.title == board_title
        assert board_before_update.description == description
        assert board_before_update.public
        assert board_before_update.created_by == created_by

        board_description = Faker().name()
        BoardsService().update_board(user_token, board_id=new_board.id, description=board_description)

        board_after_update = BoardsService().get_public_board_by_id(user_token, new_board.id)

        assert board_after_update.title == board_title
        assert board_after_update.description == board_description
        assert board_after_update.public
        assert board_after_update.created_by == created_by

    @allure.title("test_update_private_board_description_by_user")
    @allure.description("Update private board description by user")
    @allure.tag("smoke")
    @pytest.mark.test_boards
    def test_update_private_board_description_by_user(self, random_private_board_by_user):
        user_token, new_board, board_title, description, created_by = random_private_board_by_user

        board_before_update = BoardsService().get_private_board_by_id(user_token, new_board.id)

        assert board_before_update.title == board_title
        assert board_before_update.description == description
        assert not board_before_update.public
        assert board_before_update.created_by == created_by

        board_description = Faker().name()
        BoardsService().update_board(user_token, board_id=new_board.id, description=board_description)

        board_after_update = BoardsService().get_private_board_by_id(user_token, new_board.id)

        assert board_after_update.title == board_title
        assert board_after_update.description == board_description
        assert not board_after_update.public
        assert board_after_update.created_by == created_by

    @pytest.mark.test_boards
    def test_update_board_to_public_by_user(self, random_private_board_by_user):
        user_token, new_board, board_title, description, created_by = random_private_board_by_user

        board_before_update = BoardsService().get_private_board_by_id(user_token, new_board.id)

        assert board_before_update.title == board_title
        assert board_before_update.description == description
        assert not board_before_update.public
        assert board_before_update.created_by == created_by

        BoardsService().update_board(user_token, board_id=new_board.id, public=True)

        board_after_update = BoardsService().get_public_board_by_id(user_token, new_board.id)

        assert board_after_update.title == board_title
        assert board_after_update.description == description
        assert board_after_update.public
        assert board_after_update.created_by == created_by
    
    @pytest.mark.test_boards
    def test_update_board_to_private_by_user(self, random_public_board_by_user):
        user_token, new_board, board_title, description, created_by = random_public_board_by_user

        board_before_update = BoardsService().get_private_board_by_id(user_token, new_board.id)

        assert board_before_update.title == board_title
        assert board_before_update.description == description
        assert board_before_update.public
        assert board_before_update.created_by == created_by

        BoardsService().update_board(user_token, board_id=new_board.id, public=False)

        board_after_update = BoardsService().get_private_board_by_id(user_token, new_board.id)

        assert board_after_update.title == board_title
        assert board_after_update.description == description
        assert not board_after_update.public
        assert board_after_update.created_by == created_by

    @pytest.mark.test_boards
    def test_update_public_board_to_archived_by_user(self, random_public_board_by_user):
        user_token, new_board, _, _, _ = random_public_board_by_user

        board_before_update = BoardsService().get_public_board_by_id(user_token, new_board.id)

        assert not board_before_update.archived

        BoardsService().update_board(user_token, board_id=new_board.id, archived=True)

        board_after_update = BoardsService().get_public_board_by_id(user_token, new_board.id)

        assert board_after_update.archived

    @pytest.mark.test_boards
    def test_update_public_board_from_archived_by_user(self, random_public_board_by_user):
        user_token, new_board, _, _, _ = random_public_board_by_user

        BoardsService().update_board(user_token, board_id=new_board.id, archived=True)

        board_before_update = BoardsService().get_public_board_by_id(user_token, new_board.id)

        assert board_before_update.archived

        BoardsService().update_board(user_token, board_id=new_board.id, archived=False)

        board_after_update = BoardsService().get_public_board_by_id(user_token, new_board.id)

        assert not board_after_update.archived

    @pytest.mark.test_boards
    def test_update_private_board_to_archived_by_user(self, random_private_board_by_user):
        user_token, new_board, _, _, _ = random_private_board_by_user

        board_before_update = BoardsService().get_private_board_by_id(user_token, new_board.id)

        assert not board_before_update.archived

        BoardsService().update_board(user_token, board_id=new_board.id, archived=True)

        board_after_update = BoardsService().get_private_board_by_id(user_token, new_board.id)

        assert board_after_update.archived

    @pytest.mark.test_boards
    def test_update_private_board_from_archived_by_user(self, random_private_board_by_user):
        user_token, new_board, _, _, _ = random_private_board_by_user

        BoardsService().update_board(user_token, board_id=new_board.id, archived=True)

        board_before_update = BoardsService().get_private_board_by_id(user_token, new_board.id)

        assert board_before_update.archived

        BoardsService().update_board(user_token, board_id=new_board.id, archived=False)

        board_after_update = BoardsService().get_private_board_by_id(user_token, new_board.id)

        assert not board_after_update.archived


    @pytest.mark.test_boards
    def test_create_public_board_by_admin(self, admin_token, random_public_board):

        new_board, board_title, description, created_by = random_public_board

        board_info = BoardsService().get_public_board_by_id(admin_token, new_board.id)

        assert board_info.title == board_title
        assert board_info.description == description
        assert board_info.public
        assert board_info.created_by == created_by

    @pytest.mark.test_boards
    def test_create_private_board_by_admin(self, admin_token, random_private_board):

        new_board, board_title, description, created_by = random_private_board

        board_info = BoardsService().get_private_board_by_id(admin_token, new_board.id)

        assert board_info.title == board_title
        assert board_info.description == description
        assert not board_info.public
        assert board_info.created_by == created_by

    @pytest.mark.test_boards
    def test_update_public_board_title_by_admin(self, admin_token, random_public_board):
        new_board, board_title, description, created_by = random_public_board

        board_before_update = BoardsService().get_public_board_by_id(admin_token, new_board.id)

        assert board_before_update.title == board_title
        assert board_before_update.description == description
        assert board_before_update.public
        assert board_before_update.created_by == created_by

        board_title = Faker().name()
        BoardsService().update_board(admin_token, board_id=new_board.id, title=board_title)

        board_after_update = BoardsService().get_public_board_by_id(admin_token, new_board.id)

        assert board_after_update.title == board_title
        assert board_after_update.description == description
        assert board_after_update.public
        assert board_after_update.created_by == created_by

    @pytest.mark.test_boards
    def test_update_private_board_title_by_admin(self, admin_token, random_private_board):
        new_board, board_title, description, created_by = random_private_board

        board_before_update = BoardsService().get_private_board_by_id(admin_token, new_board.id)

        assert board_before_update.title == board_title
        assert board_before_update.description == description
        assert not board_before_update.public
        assert board_before_update.created_by == created_by

        board_title = Faker().name()
        BoardsService().update_board(admin_token, board_id=new_board.id, title=board_title)

        board_after_update = BoardsService().get_private_board_by_id(admin_token, new_board.id)

        assert board_after_update.title == board_title
        assert board_after_update.description == description
        assert not board_after_update.public
        assert board_after_update.created_by == created_by

    @pytest.mark.test_boards
    def test_update_public_board_description_by_admin(self, admin_token, random_public_board):
        new_board, board_title, description, created_by = random_public_board

        board_before_update = BoardsService().get_public_board_by_id(admin_token, new_board.id)

        assert board_before_update.title == board_title
        assert board_before_update.description == description
        assert board_before_update.public
        assert board_before_update.created_by == created_by

        board_description = Faker().name()
        BoardsService().update_board(admin_token, board_id=new_board.id, description=board_description)

        board_after_update = BoardsService().get_public_board_by_id(admin_token, new_board.id)

        assert board_after_update.title == board_title
        assert board_after_update.description == board_description
        assert board_after_update.public
        assert board_after_update.created_by == created_by

    @pytest.mark.test_boards
    def test_update_private_board_description_by_admin(self, admin_token, random_private_board):
        new_board, board_title, description, created_by = random_private_board

        board_before_update = BoardsService().get_private_board_by_id(admin_token, new_board.id)

        assert board_before_update.title == board_title
        assert board_before_update.description == description
        assert not board_before_update.public
        assert board_before_update.created_by == created_by

        board_description = Faker().name()
        BoardsService().update_board(admin_token, board_id=new_board.id, description=board_description)

        board_after_update = BoardsService().get_private_board_by_id(admin_token, new_board.id)

        assert board_after_update.title == board_title
        assert board_after_update.description == board_description
        assert not board_after_update.public
        assert board_after_update.created_by == created_by

    @pytest.mark.test_boards
    def test_update_board_to_public_by_admin(self, admin_token, random_private_board):
        new_board, board_title, description, created_by = random_private_board

        board_before_update = BoardsService().get_private_board_by_id(admin_token, new_board.id)

        assert board_before_update.title == board_title
        assert board_before_update.description == description
        assert not board_before_update.public
        assert board_before_update.created_by == created_by

        BoardsService().update_board(admin_token, board_id=new_board.id, public=True)

        board_after_update = BoardsService().get_public_board_by_id(admin_token, new_board.id)

        assert board_after_update.title == board_title
        assert board_after_update.description == description
        assert board_after_update.public
        assert board_after_update.created_by == created_by
    
    @pytest.mark.test_boards
    def test_update_board_to_private_by_admin(self, admin_token, random_public_board):
        new_board, board_title, description, created_by = random_public_board

        board_before_update = BoardsService().get_public_board_by_id(admin_token, new_board.id)

        assert board_before_update.title == board_title
        assert board_before_update.description == description
        assert board_before_update.public
        assert board_before_update.created_by == created_by

        BoardsService().update_board(admin_token, board_id=new_board.id, public=False)

        board_after_update = BoardsService().get_private_board_by_id(admin_token, new_board.id)

        assert board_after_update.title == board_title
        assert board_after_update.description == description
        assert not board_after_update.public
        assert board_after_update.created_by == created_by

    @pytest.mark.test_boards
    def test_update_public_board_to_archived_by_admin(self, admin_token, random_public_board):
        new_board, _, _, _ = random_public_board

        board_before_update = BoardsService().get_public_board_by_id(admin_token, new_board.id)

        assert not board_before_update.archived

        BoardsService().update_board(admin_token, board_id=new_board.id, archived=True)

        board_after_update = BoardsService().get_public_board_by_id(admin_token, new_board.id)

        assert board_after_update.archived

    @pytest.mark.test_boards
    def test_update_public_board_from_archived_by_admin(self, admin_token, random_public_board):
        new_board, _, _, _ = random_public_board

        BoardsService().update_board(admin_token, board_id=new_board.id, archived=True)

        board_before_update = BoardsService().get_public_board_by_id(admin_token, new_board.id)

        assert board_before_update.archived

        BoardsService().update_board(admin_token, board_id=new_board.id, archived=False)

        board_after_update = BoardsService().get_public_board_by_id(admin_token, new_board.id)

        assert not board_after_update.archived

    @pytest.mark.test_boards
    def test_update_private_board_to_archived_by_admin(self, admin_token, random_private_board):
        new_board, _, _, _ = random_private_board

        board_before_update = BoardsService().get_private_board_by_id(admin_token, new_board.id)

        assert not board_before_update.archived

        BoardsService().update_board(admin_token, board_id=new_board.id, archived=True)

        board_after_update = BoardsService().get_private_board_by_id(admin_token, new_board.id)

        assert board_after_update.archived

    @pytest.mark.test_boards
    def test_update_private_board_from_archived_by_admin(self, admin_token, random_private_board):
        new_board, _, _, _ = random_private_board

        BoardsService().update_board(admin_token, board_id=new_board.id, archived=True)

        board_before_update = BoardsService().get_private_board_by_id(admin_token, new_board.id)

        assert board_before_update.archived

        BoardsService().update_board(admin_token, board_id=new_board.id, archived=False)

        board_after_update = BoardsService().get_private_board_by_id(admin_token, new_board.id)

        assert not board_after_update.archived
