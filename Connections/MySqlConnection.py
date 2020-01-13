import pymysql


class MySqlConnection:

    def __init__(self):
        self.conn = pymysql.connect(
            host=None,
            user=None,
            password=None,
            db=None
        )

