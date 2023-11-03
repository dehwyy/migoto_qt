# internal
from internal.widgets.makoto import Makoto
from internal.widgets.calendar import Calendar
from internal.widgets.textops import TextOps
from internal.widgets.os import OS
from internal.widgets.random import Random
from internal.widgets.dict import Dict
from internal.lib.database import Database
from config import DEFAULT_WINDOW_SIZE
from internal.widgets.generated.mainUI import Ui_Migoto
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import sys

# widgets


# init db
database = Database("internal/database/makoto.sqlite")


class App(QMainWindow,  Ui_Migoto):
    def __init__(self):
        super().__init__()
        # App initt
        self.init_ui()
        self.main_init()

        self.setupUi(self)
        self.btn_translate.clicked.connect(lambda: self.w_dict.show())
        self.btn_random.clicked.connect(lambda: self.w_random.show())
        self.btn_os.clicked.connect(lambda: self.w_os.show())
        self.btn_textops.clicked.connect(lambda: self.w_textops.show())
        self.btn_calendar.clicked.connect(lambda: self.w_calendar.show())
        self.btn_makoto.clicked.connect(lambda: self.w_makoto.show())

        # set image
        LOGO_HEIGHT = 100

        # define image
        self.logo = QPixmap(
            'assets/makoto_logo.jpg').scaled(LOGO_HEIGHT, LOGO_HEIGHT)

        # attach it to label
        self.label_logo = QLabel(self)
        self.label_logo.setPixmap(self.logo)
        self.label_logo.setGeometry(350, 105, LOGO_HEIGHT, LOGO_HEIGHT)

    def init_ui(self):
        # main window
        self.setWindowIcon(QIcon('assets/icon.png'))
        self.setFixedSize(*DEFAULT_WINDOW_SIZE)

    def main_init(self):
        # `w` stays for `Widget`
        self.w_dict = Dict()
        self.w_random = Random()
        self.w_os = OS()
        self.w_textops = TextOps()
        self.w_calendar = Calendar()
        self.w_makoto = Makoto(database)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    t = App()
    t.show()

    sys.exit(app.exec_())
