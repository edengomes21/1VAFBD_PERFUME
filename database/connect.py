import psycopg2



from modulos.cliente.sql import SQLCliente
from modulos.perfume.sql import SQLPerfume

class ConnectDataBase:
    def __init__(self):
        self._connect = psycopg2.connect(
            host="localhost",
            database="FBD_LojaPerfume1VA",
            user="postgres",
            password="postgres"
        )

    def get_instance(self):
        return self._connect

    def init_table(self):
        cursor = self._connect.cursor()
        cursor.execute(SQLCliente._SCRIPT_CREATE_TABLE)
        cursor.execute(SQLPerfume._SCRIPT_CREATE_TABLE)
        self._connect.commit()
    def sql_new(self):
        return
