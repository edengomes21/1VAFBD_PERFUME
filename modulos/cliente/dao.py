from database.connect import ConnectDataBase
from modulos.cliente.modelo import Cliente
from modulos.cliente.sql import SQLCliente
from modulos.perfume.dao import DaoPerfume

dao_Perfume = DaoPerfume()


class DaoCliente():

    def __init__(self):
        self.connect = ConnectDataBase().get_instance()

    def get_clientes(self, busca=None):
        cursor = self.connect.cursor()
        sql = SQLCliente._SELECT_BUSCA_NOME.format(SQLCliente._NOME_TABELA,
                                                   busca) if busca else SQLCliente._SELECT_ALL

        cursor.execute(sql)
        clientes = []
        columns_name = [desc[0] for desc in cursor.description]
        for cliente in cursor.fetchall():
            data = dict(zip(columns_name, cliente))
            clientes.append(Cliente(**data).get_json())
        return clientes

    def salvar(self, cliente, id_perfume):
        perfume = dao_Perfume.get_por_id(id_perfume)
        cursor = self.connect.cursor()
        cursor.execute(SQLCliente._SCRIPT_INSERT,
                       (perfume.id, cliente.nome, cliente.endereco, cliente.telefone))
        self.connect.commit()
        id = cursor.fetchone()[0]
        return id

    def get_por_perfume(self, id_perfume):
        perfume = dao_Perfume.get_por_id(id_perfume)
        cursor = self.connect.cursor()
        sql = SQLCliente._SELECT_BY_CLIENTE_ID

        cursor.execute(sql, (str(id_perfume)))
        clientes = []
        coluns_name = [desc[0] for desc in cursor.description]
        for perfume in cursor.fetchall():

            data = dict(zip(coluns_name, perfume))
            clientes.append(data)

        return clientes

    def get_por_perfume_object(self, id_perfume):

        cursor = self.connect.cursor()
        sql = SQLCliente._SELECT_BY_CLIENTE_ID

        cursor.execute(sql, (str(id_perfume)))
        cursor.execute(SQLCliente._SELECT_BY_CLIENTE_ID, (str(id_perfume)))
        cliente = cursor.fetchone()

        if not cliente:
            return None
        columns_name = [desc[0] for desc in cursor.description]
        data = dict(zip(columns_name, cliente))

        return Cliente(**data)

    def get_por_id(self, id):
        cursor = self.connect.cursor()
        cursor.execute(SQLCliente._SELECT_ID, (str(id)))
        cliente = cursor.fetchone()
        if not cliente:
            return None
        columns_name = [desc[0] for desc in cursor.description]
        data = dict(zip(columns_name, cliente))
        return Cliente(**data)

    def atualizar(self, cliente):
        cursor = self.connect.cursor()
        cursor.execute(SQLCliente._UPDATE_BY_ID, (cliente.nome, cliente.endereco,
                                                  cliente.nome, cliente.id))
        self.connect.commit()
        return True

    def get_relatorios_clientes(self):
        cursor = self.connect.cursor()
        sql = SQLCliente._SELECT_ALL_AND_PERFUME
        cursor.execute(sql)
        clientes = []
        colluns_name = [desc[0] for desc in cursor.description]
        for cliente in cursor.fetchall():
            data = dict(zip(colluns_name, cliente))
            clientes.append(data)
        return clientes