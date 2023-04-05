from flask import Flask, make_response, jsonify, request, Response
from database.connect import ConnectDataBase
from modulos.cliente.dao import DaoCliente
from modulos.cliente.modelo import Cliente
from modulos.perfume.dao import DaoPerfume
from modulos.perfume.modelo import Perfume

app = Flask(__name__)
ConnectDataBase().init_table()

dao_cliente = DaoCliente()
dao_perfume = DaoPerfume()


#buscar todos perfumes
@app.route("/perfumes/", methods=["GET"])
def perfumes():
    parametros = request.args
    busca = parametros.get("busca", None)
    perfumes = dao_perfume.get_perfumes(busca)
    return make_response(jsonify(perfumes))

#buscar perfume por id
@app.route('/perfumes/<int:id>/', methods=['GET'])
def perfume_id(id: int):
    perfume = dao_perfume.get_por_id(id)
    if not perfume:
        return Response({}, status=404)
    return make_response(jsonify(perfume.get_json()))

#adicionar um perfume
@app.route('/perfumes/add/', methods=['POST'])
def add_perfume():
    data_perfume = dict(request.form)
    perfume = Perfume(**data_perfume)
    id = dao_perfume.salvar(perfume)
    Perfume.id = id
    return make_response({})

#atualizar perfume por id
@app.route('/perfumes/<int:id>/atualizar/', methods=['PUT'])
def atualizar_perfume(id: int):
    data_perfume = dict(request.form)
    perfume = dao_perfume.get_por_id(id)
    perfume.nome = data_perfume.get('nome')
    perfume.marca = data_perfume.get('marca')
    perfume.volume = data_perfume.get('volume')
    perfume.preco = data_perfume.get('preco')
    perfume.fragrancia = data_perfume.get('fragrancia')

    if dao_perfume.atualizar(perfume):
        return make_response(jsonify(perfume.get_json()))
    return Response({}, status=404)


#adicionar cliente com perfume
@app.route('/perfumes/<int:id>/clientes/add/', methods=['POST'])
def add_cliente(id:int):
    perfume = dao_perfume.get_por_id(id)
    if not perfume:
        return Response({}, status=404)
    data_cliente = dict(request.form)
    cliente = Cliente(**data_cliente)
    id = dao_cliente.salvar(cliente, id)
    cliente.id = id
    return make_response({})

#buscar clientes por id do perfume
@app.route('/perfumes/<int:id>/clientes/', methods=['GET'])
def clientes_perfumes(id: int):
    perfume = dao_perfume.get_por_id(id)
    if not perfume:
        return Response({}, status=404)
    clientes = dao_cliente.get_por_perfume(perfume.id)
    return make_response(jsonify(clientes))

@app.route('/perfumes/relatorio/', methods=['GET'])
def perfumes_relatorio_cliente():
    clientes = dao_cliente.get_relatorios_clientes()
    print(clientes)
    return make_response((jsonify(clientes)))



# #atualizar cliente por id
# @app.route('/perfumes/<int:id>/clientes/atualizar/', methods=['PUT'])
#
# def atualizar_cliente(id:int):
#     perfume = dao_perfume.get_por_id(id)
#     if not perfume:
#         return Response({}, status=404)
#     clientes = dao_cliente.get_por_perfume(perfume.id)
#     print(clientes[0])
#     data_cliente = dict(request.form)
#     clientesJson = make_response(jsonify(clientes[0]))
#     print(clientesJson)
#
#
#     if dao_cliente.atualizar(clientes[0]):
#         return make_response(jsonify(clientes[0].get_json()))
#     return Response({}, status=404)




app.run()
