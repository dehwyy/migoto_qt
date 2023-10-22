import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from internal.widgets.generated.mainUI import Ui_Migoto
from internal.widgets.dict import Dict
from config import DEFAULT_WINDOW_SIZE
from dotenv import load_dotenv


class App(QMainWindow,  Ui_Migoto):
    def __init__(self):
        super().__init__()
        # App initt
        self.init_ui()

        # load .env
        found = load_dotenv()
        if not found:
            raise FileNotFoundError(".env file not found")

        # init UI inherited by UI_Migoto
        self.setupUi(self)
        self.btn_translate.clicked.connect(lambda: self.w_dict.show())

    def init_ui(self):
        # main window
        self.setWindowIcon(QIcon('icon.png'))
        self.setFixedSize(*DEFAULT_WINDOW_SIZE)

        # init other widgets
        self.w_dict = Dict()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    t = App()
    t.show()

    sys.exit(app.exec_())
