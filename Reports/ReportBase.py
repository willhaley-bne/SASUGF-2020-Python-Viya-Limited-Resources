import pandas as pd
from .CASTableBase import CASTableBase


class ReportBase(object):
    conns = dict()
    conn_factory = None
    conn_warehouse = None
    conn_viya = None
    conn_mysql = None
    base_table = CASTableBase
    base_data = pd.DataFrame()

    def set_connections(self, conn_factory):
        self.conn_factory = conn_factory
        self.conns = self.conn_factory.set_connection(
            self.conn_factory.TYPE_VIYA,
            self.conn_factory.TYPE_WAREHOUSE,
            self.conn_factory.TYPE_MYSQL
        )
        self.conn_warehouse = self.conns[self.con_factory.TYPE_WAREHOUSE].conn
        self.conn_viya = self.conns[self.con_factory.TYPE_VIYA].conn
        self.conn_mysql = self.conns[self.con_factory.TYPE_MYSQL].conn

    def set_base(self):
        module_obj = __import__('Reports')
        if hasattr(module_obj, self.base_table):
            table = getattr(module_obj, self.base_table)
            table_class = table(conn_db=self.conn_warehouse, conn_viya=self.conn_viya)
            self.base_data = table_class.get_source_data()

    def preprocess(self):
        pass

    def update_records(self):
        module_obj = __import__('Reports')
        if hasattr(module_obj, self.base_table):
            table = getattr(module_obj, self.base_table)
            table_class = table(conn_db=self.conn_warehouse, conn_viya=self.conn_viya)
            table_class.update_from_records(self.base_data)

    def run(self):
        self.set_base()
        self.preprocess()
        self.update_records()
