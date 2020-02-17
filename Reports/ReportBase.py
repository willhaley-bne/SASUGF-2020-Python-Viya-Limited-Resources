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
            self.conn_factory.TYPE_WAREHOUSE
        )
        self.conn_warehouse = self.conns[self.conn_factory.TYPE_WAREHOUSE]
        self.conn_viya = self.conns[self.conn_factory.TYPE_VIYA]

    def set_base(self):
        if isinstance(self.base_table, list) is False:
            self.base_table = [self.base_table]

        for base_table in self.base_table:
            self.__set_base(base_table)

    def __set_base(self, base_table):
        module_obj = __import__('Reports')
        if hasattr(module_obj, base_table):
            table = getattr(module_obj, base_table)
            table_class = table(conn_db=self.conn_warehouse, conn_viya=self.conn_viya)
            self.base_data[base_table] = table_class.get_source_data()

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
