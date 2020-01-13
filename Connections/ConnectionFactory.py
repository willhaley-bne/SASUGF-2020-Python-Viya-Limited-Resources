class ConnectionFactory(object):

    TYPE_VIYA = 'Viya'
    TYPE_WAREHOUSE = 'Warehouse'
    TYPE_MYSQL = 'MySql'

    @staticmethod
    def get_connection(connection):
        class_string = '%sConnection' % str(connection)
        module_obj = __import__('Connections.%s' % class_string)

        if hasattr(module_obj, class_string):
            class_obj = getattr(module_obj, class_string)

            return class_obj()
        else:
            raise Exception('CONNECTION: Requested Connection Type Not Found')

    def set_connection(self, *argv):
        conns = dict()
        for arg in argv:
            conns.__setitem__(arg, self.get_connection(arg))
        return conns
