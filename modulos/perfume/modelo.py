class Perfume(object):
    def __init__(self, nome, marca, volume, preco, fragrancia, id=None):
        self.nome = nome
        self.marca = marca
        self.volume = volume
        self.preco = preco
        self.fragrancia = fragrancia
        self.id = id

    def __str__(self):
        return f'ID: {self.id} - Nome: {self.nome} - Marca: {self.marca} - Volume: {self.volume}' \
               f'- Preco: {self.preco} - Fragrancia: {self.fragrancia}'

    def get_json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'marca': self.marca,
            'volume': self.volume,
            'preco': self.preco,
            'fragrancia': self.fragrancia,
        }

    def get_sql_insert(self):
        return
