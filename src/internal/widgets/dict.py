import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog
from internal.widgets.generated.dictUI import Ui_Dictionary
from config import DEFAULT_WINDOW_SIZE
import sqlite3
from os import getenv
import requests as req


class Dict(QWidget,  Ui_Dictionary):
    def __init__(self):
        super().__init__()
        # App init
        self.init_ui()

        # init UI inherited by UI_Migoto
        self.setupUi(self)

        # connect to db
        self.init_db()

        # setup actions
        self.btn_translate.clicked.connect(self.onClickButtonTranslate)

    def init_ui(self):
        self.setFixedSize(*DEFAULT_WINDOW_SIZE)

    # ! db operations
    def init_db(self):
        db_connection = self.get_sqlite3_connection()

        # create table if not exists
        #
        # ________________Dictionary____________________
        # `id`:      `int`   `primary key;autoincrement`
        # `api_key`: `text`                              @see `https://yandex.com/dev/dictionary/keys/get`
        # ______________________________________________
        db_connection.execute(
            "CREATE TABLE IF NOT EXISTS dictionary (id INTEGER PRIMARY KEY AUTOINCREMENT, api_key TEXT)")

        db_connection.execute(
            "INSERT INTO dictionary (api_key) VALUES (?)", ("dict.1.1.20231022T070342Z.ed96950eca1b7bd5.2092598dc924cb780f0086537440ff74fa15bccf",))

        # submit queries
        db_connection.commit()

        # close connection
        db_connection.close()

    # get api_key from db
    def get_api_key(self) -> str:
        conn = self.get_sqlite3_connection()
        res = conn.execute(
            "SELECT api_key FROM dictionary").fetchone()[0]

        if res is None:
            raise ApiKeyError("API key not provided")
        return res

    def get_sqlite3_connection(self) -> sqlite3.Connection:
        db_connection = sqlite3.connect(
            "src/internal/database/user.sqlite")
        return db_connection

    # actions
    def onClickButtonTranslate(self):
        text = self.input.text().lower()

        result = self.get_word(text)
        self.output.setText(result)

    # indirect used fn
    def get_word(self, word: str) -> str:
        # @see `https://yandex.com/dev/dictionary/doc/dg/reference/lookup.html`

        key = getenv("YANDEX_API_KEY")
        if not getenv("DEV"):
            try:
                key = self.get_api_key()

            except ApiKeyError as e:
                print(e)
                return
            except Exception as e:
                print(f"unknown error occuried {e}")
                return

        url = f"https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key={key}&lang={self.infer_language(word)}&text={word}"

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
        first_letter = word[0]

        if ord("a") <= ord(first_letter) <= ord("z"):
            return "en-ru"
        elif ord("а") <= ord(first_letter) <= ord("я") or ord(first_letter) == ord("ё"):
            return "ru-en"

        # default translation
        return "en-ru"


# Custom exception. Should be raised when ApiKey is required but not provided (not stored in db)
class ApiKeyError(Exception):
    pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    t = Dict()
    t.show()

    sys.exit(app.exec())
