import pyodbc


class Warehouse(object):
    server = None
    username = None
    password = None
    driver = '/opt/microsoft/msodbcsql/lib64/libmsodbcsql-13.1.so.9.2'


class WarehouseConnection(Warehouse):

    def __init__(self, database='Warehouse'):
        connection_string = 'DRIVER=%s;SERVER=%s;PORT=1433;UID=%s;PWD=%s;Database=%s'
        connection_string = connection_string % (
            self.driver, self.server, self.username, self.password, database
        )
        self.conn = pyodbc.connect(connection_string)
