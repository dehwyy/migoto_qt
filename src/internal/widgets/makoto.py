import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtGui import QIcon, QFont
from internal.widgets.generated.makotoUI import Ui_Makoto
from config import DEFAULT_WINDOW_SIZE, DEFAULT_QMESSAGE_SIZE
from internal.lib.database import Database

# twirp
from twirp.context import Context
from twirp.exceptions import TwirpServerException
from generated.auth_twirp import AuthRPCClient
from generated.hashmap_twirp import HashmapRPCClient
from generated.auth_pb2 import SignInRequest
from generated.hashmap_pb2 import GetItemsPayload
from generated.general_pb2 import UserId


class Makoto(QWidget,  Ui_Makoto):
    def __init__(self, db: Database):
        super().__init__()
        self.db = db
        self.USER_NICKNAME = ""

        # App init
        self.init_ui()

        # init UI inherited by UI_Migoto
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)

        # setup actions
        self.btn_login.clicked.connect(self.login_to_makoto)
        self.btn_logout.clicked.connect(self.logout)

    def init_ui(self):
        self.setWindowIcon(QIcon('assets/icon.png'))
        self.setFixedSize(*DEFAULT_WINDOW_SIZE)

    # actions

    def login_to_makoto(self):
        username = self.input_username.text()
        password = self.input_password.text()

        try:
            client = AuthRPCClient("http://localhost:4000")
            response, headers = client.SignIn(ctx=Context(), request=SignInRequest(
                credentials={
                    "username": username,
                    "password": password
                }), server_path_prefix="/authorization")

            authorization_token = headers["Authorization"].split()[1]
            userId = response.userId
            username = response.username

            self.db.update_or_insert_user(userId, username)
            self.db.update_or_insert_token(userId, authorization_token)
            self.auth_success(username)
            self.stackedWidget.setCurrentIndex(1)
            self.nickname.setText(username)
            self.USER_NICKNAME = username
            self.set_hashmap_data_by_user_id(userId)

        except TwirpServerException as e:
            print(e.code, e.message, e.meta, e.to_dict())
            self.invalid_credentials()
        except Exception as e:
            print("Unexpected error", e)

    def logout(self):
        self.db.delete_token(self.USER_NICKNAME)
        self.stackedWidget.setCurrentIndex(0)

    def invalid_credentials(self):
        error_box = QMessageBox(self)
        error_box.show()
        error_box.setIcon(QMessageBox.Critical)
        error_box.setText("Error!")
        error_box.setInformativeText("Invalid credentials! Please try again.")
        error_box.exec_()

    def auth_success(self, username):
        success_box = QMessageBox(self)

        success_box.setFixedSize(*DEFAULT_QMESSAGE_SIZE)

        success_box.show()

        # font
        font = QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        success_box.setFont(font)

        success_box.setIcon(QMessageBox.Information)
        success_box.setText("Success!")
        success_box.setInformativeText(f"Welcome, {username}!")
        success_box.exec_()

    def set_hashmap_data_by_user_id(self, user_id):
        try:
            token = f"Bearer {self.db.get_token(user_id)}"

            client = HashmapRPCClient("http://localhost:4000")
            ctx = Context()
            ctx.set_header("Authorization", token)

            response, _ = client.GetItems(ctx=ctx, request=GetItemsPayload(
                user_id=user_id,
                part=0,
                keyword="",
            ), server_path_prefix="/hashmap")

            items = ["", "", "", "", ""]
            for i, item in enumerate(response.items):
                if i == 5:
                    break
                items[i] = f"{item.key} - {item.value}"

            ctx2 = Context()
            ctx2.set_header("Authorization", token)

            response, _ = client.GetTags(ctx=ctx2, request=UserId(
                user_id=user_id
            ), server_path_prefix="/hashmap")

            tags = ["", "", "", "", ""]
            for i, tag in enumerate(response.tags):
                if i == 5:
                    break
                tags[i] = f"{tag.text} with {tag.usages} usages"

            self.set_items_and_tags(items, tags)

        except TwirpServerException as e:
            print(e.code, e.message, e.meta, e.to_dict())
        except Exception as e:
            print("Unexpected error", e)

    def set_items_and_tags(self, items: list[str], tags: list[str]):
        # set items
        self.item1.setText(items[0])
        self.item2.setText(items[1])
        self.item3.setText(items[2])
        self.item4.setText(items[3])
        self.item5.setText(items[4])

        # set tags
        self.tag1.setText(tags[0])
        self.tag2.setText(tags[1])
        self.tag3.setText(tags[2])
        self.tag4.setText(tags[3])
        self.tag5.setText(tags[4])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    t = Makoto()
    t.show()

    sys.exit(app.exec())
