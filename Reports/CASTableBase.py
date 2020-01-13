import pandas as pd
import swat


class CASTableBase(object):
    source_sql = None
    source_data = None

    cas_table_name = None
    caslib = None

    def __init__(self, conn_db, conn_viya):
        self.conn_db = conn_db
        self.conn_viya = conn_viya

    def update_from_source(self):
        self.update_from_records(self.get_source_data())

    def update_from_records(self, records):
        self.remove_from_cas()
        swat.cas.table.CASTable.from_records(self.conn_viya, records,
                                             casout={'name': self.cas_table_name,
                                                     'caslib': self.caslib,
                                                     'promote': True})

    def remove_from_cas(self):
        try:
            table = self.conn_viya.CASTable(name=self.cas_table_name, caslib=self.caslib)
            table.dropTable()
        except:
            pass

    def get_source_data(self):
        return pd.read_sql_query(self.source_sql, self.conn_db)

