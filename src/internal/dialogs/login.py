import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from config import DEFAULT_WINDOW_SIZE


class LoginDialog(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.parent = parent

        # App init
        self.init_ui()

        # init UI inherited by UI_Migoto
        self.setupUi(self)

    def init_ui(self):
        self.setWindowIcon(QIcon('icon.png'))
        self.setFixedSize(*DEFAULT_WINDOW_SIZE)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    t = Dict()
    t.show()

    sys.exit(app.exec())
