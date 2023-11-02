import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget
from internal.widgets.generated.calendarUI import Ui_Calendar
from os import getlogin, getpid, path
from platform import system
from config import DEFAULT_WINDOW_SIZE


class Calendar(QWidget,  Ui_Calendar):
    def __init__(self):
        super().__init__()
        # App initt
        self.init_ui()

        self.setupUi(self)

    def init_ui(self):
        self.setWindowIcon(QIcon('icon.png'))
        self.setFixedSize(*DEFAULT_WINDOW_SIZE)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    t = Calendar()
    t.show()

    sys.exit(app.exec())
