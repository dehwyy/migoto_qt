import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget
from random import randint, random
from datetime import datetime
from uuid import uuid4
from internal.widgets.generated.randomUI import Ui_Random
from config import DEFAULT_WINDOW_SIZE


class Random(QWidget,  Ui_Random):
    def __init__(self):
        super().__init__()
        # App initt
        self.init_ui()

        # init UI inherited by UI_Migoto
        self.setupUi(self)

        # setup listeners
        self.rand_int.clicked.connect(self.generate_int)
        self.rand_float.clicked.connect(self.generate_float)
        self.rand_str.clicked.connect(self.generate_str)
        self.rand_uuid.clicked.connect(self.generate_uuid)
        self.rand_bool.clicked.connect(self.generate_bool)
        self.rand_date.clicked.connect(self.generate_date)

        self.btn_copy.clicked.connect(self.copy_output)

    def init_ui(self):
        self.setWindowIcon(QIcon('icon.png'))
        self.setFixedSize(*DEFAULT_WINDOW_SIZE)

    # ! actions

    # rands
    def generate_int(self):
        self.clear_oncopy_input()
        random_int = randint(0, 2 ** 32 - 1)
        self.set_output(random_int)

    def generate_float(self):
        self.clear_oncopy_input()
        random_float = random() * (2 ** 32 - 1)
        self.set_output(random_float)

    def generate_str(self):
        self.clear_oncopy_input()
        random_str = "".join([chr(randint((ord('a')), ord('z')))
                             for _ in range(32)])
        self.set_output(random_str)

    def generate_uuid(self):
        self.clear_oncopy_input()
        random_uuid = str(uuid4())
        self.set_output(random_uuid)

    def generate_bool(self):
        self.clear_oncopy_input()
        random_bool = random() > 0.5
        self.set_output(random_bool)

    # actually it generates not random but date from 1970-01-01
    def generate_date(self):
        self.clear_oncopy_input()
        now = datetime.now().timestamp()
        self.set_output(datetime.fromtimestamp(
            now * random()).strftime("%Y-%m-%d %H:%M:%S"))

    # copy button
    def copy_output(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.output.toPlainText())
        self.label_oncopy.setText("Copied!")

    # ! internal fn

    def clear_oncopy_input(self):
        self.label_oncopy.setText("")

    def set_output(self, v, fallback=''):
        try:
            self.output.setText(str(v))
        except:
            self.output.setText(fallback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    t = Random()
    t.show()

    sys.exit(app.exec())
