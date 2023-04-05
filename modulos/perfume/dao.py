from flask import Response

from database.connect import ConnectDataBase
from modulos.perfume.modelo import Perfume
from modulos.perfume.sql import SQLPerfume

class DaoPerfume(object):

    def __init__(self):
        self.connect = ConnectDataBase().get_instance()

    def get_perfumes(self, busca=None):
        cursor = self.connect.cursor()
        sql = SQLPerfume._SELECT_BUSCA_NOME.format(SQLPerfume._NOME_TABELA,
                                              busca) if busca else SQLPerfume._SELECT_ALL

        cursor.execute(sql)
        perfumes = []
        columns_name = [desc[0] for desc in cursor.description]
        for perfume in cursor.fetchall():
            data = dict(zip(columns_name, perfume))
            perfumes.append(Perfume(**data).get_json())
        return perfumes

    def salvar(self, perfurme):
        cursor = self.connect.cursor()
        cursor.execute(SQLPerfume._SCRIPT_INSERT,
                       (perfurme.nome, perfurme.marca, perfurme.volume,
                        perfurme.preco,perfurme.fragrancia))
        self.connect.commit()
        id = cursor.fetchone()[0]
        return id

    def get_por_id(self, id):
        cursor = self.connect.cursor()
        cursor.execute(SQLPerfume._SELECT_ID, (str(id)))
        perfume = cursor.fetchone()
        if not perfume:
            return None
        columns_name = [desc[0] for desc in cursor.description]
        data = dict(zip(columns_name, perfume))
        return Perfume(**data)

    def atualizar(self, perfume):
        cursor = self.connect.cursor()
        cursor.execute(SQLPerfume._UPDATE_BY_ID, (perfume.nome, perfume.marca, perfume.volume,
                                                  perfume.preco, perfume.fragrancia, perfume.id))
        self.connect.commit()
        return True