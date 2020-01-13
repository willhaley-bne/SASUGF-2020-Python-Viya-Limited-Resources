import swat
from sasctl import Session
from time import sleep


class Viya(object):

    url = None
    user_name = None
    password = None
    port = None


class ViyaConnection(Viya):

    def __init__(self):
        self.conn = swat.CAS(self.url, self.port, self.user_name, self.password)

    def get_server_status(self):
        return self.conn.serverstatus()

    def get_data(self, library, table):
        return self.conn.CASTable()

    def read_sql(self, sql, db_conn):
        return self.conn.read_sql(sql, db_conn)

    def request_get(self, url):
        return self.ctl.get(url)

    def request_post(self, url):
        return self.ctl.post(url)

    def drop_cas_table(self, output_table, output_lib):
        table = self.conn.CASTable(name=output_table, caslib=output_lib)
        table.dropTable()
