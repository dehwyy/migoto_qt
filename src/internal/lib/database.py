import sqlite3


class Database():
    def __init__(self, name="makoto.sqlite"):
        self.conn = sqlite3.connect(name)

        # id - primary key, autogenerated - uint
        # userId - userId from makoto - UUID (in current db represented as TEXT)
        # username - username from makoto - string

        self.conn.execute(
            """CREATE TABLE IF NOT EXISTS users_data (
                id INTEGER PRIMARY KEY,
                user_id TEXT,
                username TEXT)
              """)

        self.conn.commit()

        # id - primary key, autogenerated - uint
        # userId - userId from makoto - refrerences to users_data.userId
        # token - authorization token from makoto

        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS users_token (
                id INTEGER PRIMARY KEY,
                token TEXT,
                user_id TEXT ,
                FOREIGN KEY(user_id) REFERENCES users_data(user_id)
            )""")

        self.conn.commit()

    def db_close(self) -> None:
        self.conn.close()

    # ! Users
    # username = <string> or user_id = <string> should be provided
    def get_user(self, **user_login) -> tuple[str, str]:
        username = user_login.get("username")
        if username:
            return self.conn.execute(
                "SELECT user_id, username FROM users_data WHERE username = ?",
                (username, )).fetchone()

        user_id = user_login.get("user_id")
        if user_id is None:
            return "", ""

        return self.conn.execute(
            "SELECT user_id, username FROM users_data WHERE user_id = ?",
            (user_login.get("user_id"), )).fetchone()

    def insert_user(self, user_id, username) -> None:
        self.conn.execute("""
                          INSERT INTO users_data (user_id, username) VALUES (?, ?)
                          """, (user_id, username))
        self.conn.commit()

    def update_user(self, user_id, username) -> None:
        self.conn.execute("""
                          UPDATE users_data SET username = ? WHERE user_id = ?
                          """, (username, user_id))
        self.conn.commit()

    def update_or_insert_user(self, user_id, username) -> None:
        # try to get user
        res = self.get_user(user_id=user_id)

        # user wasn't found -> create
        if res is None:
            self.insert_user(user_id, username)
            return

        # user was found -> update
        self.update_user(user_id, username)

    # ! Tokens
    def get_token(self, user_id) -> str:
        res = self.conn.execute(
            "SELECT token FROM users_token WHERE user_id = ?",
            (user_id, )).fetchone()

        if res is None:
            return ""

        return res[0]

    def insert_token(self, user_id, token) -> None:
        self.conn.execute("""
                          INSERT INTO users_token (token, user_id) VALUES (?, ?)
                          """, (token, user_id))
        self.conn.commit()

    def update_token(self, user_id, token) -> None:
        self.conn.execute("""
                          UPDATE users_token SET token = ? WHERE user_id = ?
                          """, (token, user_id))
        self.conn.commit()

    def update_or_insert_token(self, user_id, token) -> None:
        # try to get token
        token_from_db = self.get_token(user_id=user_id)

        # not found => create
        if token_from_db == "":
            self.insert_token(user_id, token)
            return

        # found => update
        self.update_token(user_id, token)