import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from internal.pyui.mainui import Ui_Migoto


class App(QMainWindow,  Ui_Migoto):
    def __init__(self):
        super().__init__()
        # App initt
        self.init_ui()

        # init UI inherited by UI_Migoto
        self.setupUi(self)

    def init_ui(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    t = App()
    t.show()

    sys.exit(app.exec())
