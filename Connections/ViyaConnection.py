import swat


class Viya(object):
    url = None
    user_name = None
    password = None
    port = None


class ViyaConnection(Viya):

    def __init__(self):

        if self.url is None:
            raise Exception('You need to provide the URL for your Viya application')
        if self.port is None:
            raise Exception('You need to provide the PORT for your Viya application')
        if self.user_name is None:
            raise Exception('You need to provide the Username for your Viya application')
        if self.password is None:
            raise Exception('You need to provide the Password for your Viay application')

        self.conn = swat.CAS(self.url, self.port, self.user_name, self.password)

    def get_server_status(self):
        return self.conn.serverstatus()

    def get_cas_table(self, table_name, caslib_name):
        return self.conn.CASTable(name=table_name, caslib=caslib_name)

    def drop_cas_table(self, table_name, caslib_name):
        table = self.conn.CASTable(name=table_name, caslib=caslib_name)
        table.dropTable()

    def update_cas_table(self, records, table_name, caslib_name):
        swat.cas.table.CASTable.from_records(self.conn, records,
                           casout={'name': table_name,
                                   'caslib': caslib_name,
                                   'promote': True})
