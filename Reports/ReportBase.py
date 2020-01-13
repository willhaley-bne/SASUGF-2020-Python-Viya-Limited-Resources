import pandas as pd
import swat


class ReportBase(object):
    conns = dict()
    conn_warehouse = None
    conn_viya = None
    conn_mysql = None

    sql = None

    def __init__(self, conn_factory):
        self.conn_factory = conn_factory

    def set_connections(self):
        self.conns = self.conn_factory.set_connection(
            self.conn_factory.TYPE_VIYA,
            self.conn_factory.TYPE_WAREHOUSE,
            self.conn_factory.TYPE_MYSQL
        )
        self.conn_warehouse = self.conns[self.con_factory.TYPE_WAREHOUSE].conn
        self.conn_viya = self.conns[self.con_factory.TYPE_VIYA].conn
        self.conn_mysql = self.conns[self.con_factory.TYPE_MYSQL].conn

    def run(self):
        pass
