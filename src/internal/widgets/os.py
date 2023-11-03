import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget
from internal.widgets.generated.osUI import Ui_os
from os import getlogin, getpid, path
from platform import system
from config import DEFAULT_WINDOW_SIZE


class OS(QWidget,  Ui_os):
    def __init__(self):
        super().__init__()
        # App initt
        self.init_ui()

        # init UI inherited by UI_Migoto
        self.setupUi(self)

        # init listeners
        self.btn_pid.clicked.connect(self.get_pid)
        self.btn_osname.clicked.connect(self.get_os)
        self.btn_user.clicked.connect(self.get_osusername)
        self.btn_home.clicked.connect(self.get_home)

    def init_ui(self):
        self.setWindowIcon(QIcon('assets/icon.png'))
        self.setFixedSize(*DEFAULT_WINDOW_SIZE)

    # ! actions
    def get_pid(self):
        self.set_output(str(getpid()))

    def get_os(self):
        self.set_output(system())

    def get_osusername(self):
        self.set_output(getlogin())

    def get_home(self):
        self.set_output(path.expanduser('~'))

    # ! internal

    def set_output(self, text, fallack=""):
        try:
            self.output.setText(text)
        except:
            self.output.setText(fallack)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    t = OS()
    t.show()

    sys.exit(app.exec())
