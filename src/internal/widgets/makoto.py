import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtGui import QIcon, QFont
from internal.widgets.generated.makotoUI import Ui_Makoto
from config import DEFAULT_WINDOW_SIZE, DEFAULT_QMESSAGE_SIZE
from internal.lib.database import Database

# twirp
from twirp.context import Context
from twirp.exceptions import TwirpServerException
from generated.auth_twirp import AuthClient
from generated.auth_pb2 import AuthResponse, SignInRequest


class Makoto(QWidget,  Ui_Makoto):
    def __init__(self, db: Database):
        super().__init__()
        self.db = db

        # App init
        self.init_ui()

        # init UI inherited by UI_Migoto
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)

        # setup actions
        self.btn_login.clicked.connect(self.login_to_makoto)

    def init_ui(self):
        self.setWindowIcon(QIcon('icon.png'))
        self.setFixedSize(*DEFAULT_WINDOW_SIZE)

    # actions

    def login_to_makoto(self):
        username = self.input_username.text()
        password = self.input_password.text()

        try:
            client = AuthClient("http://localhost:5001")
            response, headers = client.SignIn(ctx=Context(), request=SignInRequest(
                credentials={
                    "username": username,
                    "password": password
                }))

            authorization_token = headers["Authorization"]
            userId = response.userId
            username = response.username

            self.db.update_or_insert_user(userId, username)
            self.db.update_or_insert_token(userId, authorization_token)
            self.auth_success(username)
            self.stackedWidget.setCurrentIndex(1)

        except TwirpServerException as e:
            print(e.code, e.message, e.meta, e.to_dict())
            self.invalid_credentials()
        except Exception as e:
            print("Unexpected error", e)

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    t = Makoto()
    t.show()

    sys.exit(app.exec())
