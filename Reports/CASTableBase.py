import pandas as pd


class CASTableBase(object):
    source_sql = None
    source_data = None

    cas_table_name = None
    caslib = None

    def __init__(self, conn_db=None, conn_viya=None):
        self.conn_db = conn_db
        self.conn_viya = conn_viya

    def remove_from_cas(self):
        try:
            self.conn_viya.drop_cas_table(self.cas_table_name, self.caslib)
        except:
            pass

    def update_from_source(self):
        self.update_from_records(self.get_source_data())

    def update_from_records(self, records):
        self.remove_from_cas()
        self.conn_viya.update_cas_table(records, self.cas_table_name, self.caslib)

    def get_source_data(self):
        return pd.read_sql_query(self.source_sql, self.conn_db)

    def get_from_cas(self):
        return self.conn_viya.get_cas_table(self.cas_table_name, self.caslib)
