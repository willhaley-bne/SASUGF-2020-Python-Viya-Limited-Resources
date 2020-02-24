import pandas as pd


class CASTableBase(object):
    source_sql = None
    source_data = None

    cas_table_name = None
    caslib = None

    decision_source = None
    decision = None

    def __init__(self, conn_db=None, conn_viya=None):
        self.conn_db = conn_db
        self.conn_viya = conn_viya
        self.set_decision_source()

    def set_decision_source(self):

        if self.decision_source is None:
            return

        module_obj = __import__('Reports')
        if hasattr(module_obj, self.decision_source):
            decision_module = getattr(module_obj, self.decision_source)
            self.decision = decision_module(self.conn_db, self.conn_viya)

    def remove_from_cas(self):
        try:
            self.conn_viya.drop_cas_table(self.cas_table_name, self.caslib)
        except:
            pass

    def update_from_records(self, records):
        self.remove_from_cas()
        self.conn_viya.update_cas_table(records, self.cas_table_name, self.caslib)

    def update_from_source(self):
        self.update_from_records(self.get_source_data())

    def get_source_data(self):

        if self.source_data is not None:
            return self.source_data

        self.pre_process_source_data()

        if self.decision_source:
            self.decision.exec()
            self.source_data = self.conn_viya.get_cas_table(self.cas_table_name, self.caslib)
        else:
            self.source_data = pd.read_sql_query(self.source_sql, self.conn_db.conn)

        self.source_data = pd.DataFrame().from_records(self.source_data.to_records())

        self.post_process_source_data()

        return self.source_data

    def pre_process_source_data(self):
        pass

    def post_process_source_data(self):
        pass

    def get_from_cas(self):
        return self.conn_viya.get_cas_table(self.cas_table_name, self.caslib)
