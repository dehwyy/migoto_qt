import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from internal.widgets.generated.dictUI import Ui_Dictionary
from config import DEFAULT_WINDOW_SIZE
from internal.lib.errors import InvalidInputError
import requests as req


class Dict(QWidget,  Ui_Dictionary):
    def __init__(self):
        super().__init__()
        # App init
        self.init_ui()

        # init UI inherited by UI_Migoto
        self.setupUi(self)

        # setup actions
        self.btn_translate.clicked.connect(self.onClickButtonTranslate)

    def init_ui(self):
        self.setWindowIcon(QIcon('assets/icon.png'))
        self.setFixedSize(*DEFAULT_WINDOW_SIZE)

    # actions
    def onClickButtonTranslate(self):
        text = self.input.text().lower()

        try:
            result = self.get_word(text)
            self.output.setText(result)
        except:
            self.output.setText(
                f'Error occurred when trying to find word "{text}"')

    # indirect used fn
    def get_word(self, word: str) -> str:
        # @see `https://yandex.com/dev/dictionary/doc/dg/reference/lookup.html`

        key = "dict.1.1.20231022T070342Z.ed96950eca1b7bd5.2092598dc924cb780f0086537440ff74fa15bccf"
        lang = ""
        try:
            lang = self.infer_language(word)
        except InvalidInputError as e:
            return str(e)

        url = f"https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key={key}&lang={lang}&text={word}"

        response = req.get(url)
        dict_body_response = response.json()

        result_words: list[str] = []

        for definition in dict_body_response["def"]:
            for tr in definition["tr"]:

                result_words.append(tr["text"])

                if len(result_words) == 5:
                    return ", ".join(result_words)

        return ", ".join(result_words) if result_words else [f"Sorry, I don't know word `${word}`"]

    def infer_language(self, word: str) -> str:
        if len(word) == 0:
            raise InvalidInputError("Input is empty, please provide a word.")

        first_letter = word[0]

        if ord("a") <= ord(first_letter) <= ord("z"):
            return "en-ru"
        elif ord("а") <= ord(first_letter) <= ord("я") or ord(first_letter) == ord("ё"):
            return "ru-en"

        # default translation
        return "en-ru"


if __name__ == "__main__":
    app = QApplication(sys.argv)
    t = Dict()
    t.show()

    sys.exit(app.exec())
