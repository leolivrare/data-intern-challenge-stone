import psycopg2

class Connection(object):
    database = None

    def __init__(self, host_info, db, usr, pwd, port_info):
        self.database = psycopg2.connect(host = host_info,
                                         database = db,
                                         user = usr,
                                         password = pwd,
                                         port = port_info)

    def select_table(self, table_name):
        try:
            cursor = self.database.cursor()
            cursor.execute("select * from " + table_name)
            result_set = cursor.fetchall()
            cursor.close()
        except (Exception, psycopg2.Error) as error:
            print(error)
            return None
        return result_set

    def close(self):
        self.database.close()
