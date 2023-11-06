import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from random import randint, shuffle
from internal.widgets.generated.textopsUI import Ui_TextOperations
from config import DEFAULT_WINDOW_SIZE

OPERATIONS = {
    "REMOVE_SYMBOL": "REMOVE_SYMBOL",
    "CHANGE_ORDER": "CHANGE_ORDER",
    "GET_LENGTH": "GET_LENGTH",
    "REVERSE": "REVERSE",
    "TRUE_CAMEL_CASE": "TRUE_CAMEL_CASE",
}


class TextOps(QWidget,  Ui_TextOperations):
    def __init__(self):
        super().__init__()
        # Init variables
        self.selected_mode = None

        # App init
        self.init_ui()

        # init UI inherited by generated UI
        self.setupUi(self)

        # ! setup listeners
        # mode setters
        self.btn_remove_symbol.clicked.connect(
            lambda: self.set_mode(self.btn_remove_symbol, \
                                  OPERATIONS["REMOVE_SYMBOL"]))
        self.btn_change_order.clicked.connect(
            lambda: self.set_mode(self.btn_change_order, \
                                  OPERATIONS["CHANGE_ORDER"]))
        self.btn_length_str.clicked.connect(
            lambda: self.set_mode(self.btn_length_str, \
                                  OPERATIONS["GET_LENGTH"]))
        self.btn_reverse_str.clicked.connect(
            lambda: self.set_mode(self.btn_reverse_str, \
                                  OPERATIONS["REVERSE"]))
        self.btn_makoto_camel.clicked.connect(
            lambda: self.set_mode(self.btn_makoto_camel, \
                                  OPERATIONS["TRUE_CAMEL_CASE"]))

        # compile
        self.btn_compile.clicked.connect(self.compile)

    def init_ui(self):
        self.setWindowIcon(QIcon('assets/icon.png'))
        self.setFixedSize(*DEFAULT_WINDOW_SIZE)

    def compile(self):
        result = self.get_compile_result()
        self.set_output(result)

    # ! internal
    def get_compile_result(self):
        # get text from input
        text = self.input.text()

        if self.selected_mode == OPERATIONS["REMOVE_SYMBOL"]:
            return self.remove_symbol(text)

        elif self.selected_mode == OPERATIONS["CHANGE_ORDER"]:
            return self.change_order(text)

        elif self.selected_mode == OPERATIONS["GET_LENGTH"]:
            return str(self.get_length(text))

        elif self.selected_mode == OPERATIONS["REVERSE"]:
            return self.reverse(text)

        elif self.selected_mode == OPERATIONS["TRUE_CAMEL_CASE"]:
            return self.true_camel_case(text)

        else:
            return "Please choose a mode!"

    def remove_symbol(self, text):
        s_idx = randint(0, len(text))

        return text[:s_idx] + text[s_idx + 1:]

    def change_order(self, text):
        chars = list(text)
        shuffle(chars)

        return "".join(chars)

    def get_length(self, text):
        return len(text)

    def reverse(self, text):
        return text[::-1]

    def true_camel_case(self, text):
        chars = list("".join(text.lower().split()))
        for i in range(0, len(chars), 2):
            chars[i] = chars[i].upper()

        return "".join(chars)

    def set_output(self, text, fallback=""):
        try:
            self.output.setText(text)
        except:
            self.output.setText(fallback)

    def set_mode(self, btn_self: QPushButton, text: str) -> None:
        BASE_STYLE_SHEET = """
            font-size: 18px;
            background-color: white;
            color: #222222;
            border: 3px solid #555555;
            border-radius: 10px;
        """

        # reset all colors
        self.btn_change_order.setStyleSheet(BASE_STYLE_SHEET)
        self.btn_length_str.setStyleSheet(BASE_STYLE_SHEET)
        self.btn_reverse_str.setStyleSheet(BASE_STYLE_SHEET)
        self.btn_remove_symbol.setStyleSheet(BASE_STYLE_SHEET)
        self.btn_makoto_camel.setStyleSheet(BASE_STYLE_SHEET)

        # set new mode val (as enum member)
        self.selected_mode = text

        # set different color for pressed button
        btn_self.setStyleSheet(BASE_STYLE_SHEET +
                               "\nbackground-color: #ff00d2;")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    t = TextOps()
    t.show()

    sys.exit(app.exec())
