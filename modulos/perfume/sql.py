class SQLPerfume:
    _NOME_TABELA = 'perfume'
    _SCRIPT_CREATE_TABLE = f'CREATE TABLE IF NOT EXISTS {_NOME_TABELA}(' \
                           f'id serial primary key,' \
                           f'nome varchar(100),' \
                           f'marca varchar(100),' \
                           f'volume int,' \
                           f'preco decimal,' \
                           f'fragrancia varchar(100))'

    _SCRIPT_INSERT = f'INSERT INTO {_NOME_TABELA}(nome, marca, volume, preco, fragrancia) ' \
                     f'values(%s, %s, %s, %s, %s) RETURNING id'
    _SELECT_ALL = f'SELECT * FROM {_NOME_TABELA}'
    _SELECT_ID = f'SELECT * FROM {_NOME_TABELA} WHERE ID=%s'
    _SELECT_BUSCA_NOME = "SELECT * FROM {} where nome ILIKE '%{}%'"

    _UPDATE_BY_ID = f'UPDATE {_NOME_TABELA} SET nome=%s, marca=%s, volume=%s, preco=%s, fragrancia=%s ' \
                    f'WHERE id=%s'