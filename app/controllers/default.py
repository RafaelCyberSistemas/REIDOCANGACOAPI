#import pymysql
from app import app
from app.controllers import controllerUsers
from app.controllers import controllerEmpregado
from app.controllers import controllerFornecedorPF
from app.controllers import controllerFornecedorPJ
from app.controllers import controllerProduto
from app.controllers import controllerPedido
from config import mysql
from flask import Flask, request, flash, render_template, redirect, jsonify
from app.models.classes_basicas.User import User
from app.models.classes_basicas.Empregado import Empregado
from app.models.classes_basicas.FornecedorPF import FornecedorPF
from app.models.classes_basicas.FornecedorPJ import FornecedorPJ
from app.models.classes_basicas.Produto import Produto
from app.models.classes_basicas.Pedido import Pedido 
import json


@app.route("/index")
@app.route("/")
def index():
    return "index"


###ROTAS DE USERS

@app.route("/users",  methods=["POST"])
def add_user():
    _json = request.json
    _username = str(_json['userName'])
    _senha = str(_json['senha']) 
    _tipo = str(_json['tipo'])
    _id_empregado = str(_json['idEmpregado'])
    _status = str(_json['status'])
    user = User(_username, _senha, _tipo, _id_empregado, _status) 
    return controllerUsers.add_user(user)    

@app.route("/users",  methods=['GET'])
def listarUsers():
    return controllerUsers.listarUsers()

@app.route("/users/<int:id>",  methods=['GET'])
def getUserById(id):
    return controllerUsers.getById(id)

@app.route("/users",  methods=["PUT"])
def update_user():
    _json = request.json
    _id_user = str(_json['idUser'])
    _username = str(_json['userName'])
    _senha = str(_json['senha']) 
    _tipo = str(_json['tipo'])
    _id_empregado = int(_json['idEmpregado'])
    _status = str(_json['status'])
    user = User(_username, _senha, _tipo, _id_empregado, _status)
    user.setIdUser(_id_user) 
    return controllerUsers.update_user(user)   


@app.route("/users/<int:id>", methods=['DELETE'])
def delete_user(id):
    return controllerUsers.delete_user(id)
      



###ROTAS DE EMPREGADOS

@app.route("/empregados",  methods=["POST"])
def add_empregado():
    _json = request.json
    _nome_empregado = str(_json['nomeEmpregado'])
    _cpf = str(_json['cpf']) 
    _sexo = str(_json['sexo'])
    _data_nascimento = str(_json['dataNascimento'])
    _telefone = str(_json['telefone'])
    _celular = str(_json['celular'])
    _email = str(_json['email'])
    _endereco = str(_json['endereco'])
    _complemento = str(_json['complemento'])
    _bairro = str(_json['bairro'])
    _cep = str(_json['cep'])
    _cidade = str(_json['cidade'])
    _estado = str(_json['estado'])
    _pais = str(_json['pais'])
    _status = str(_json['status'])

    empregado = Empregado(_nome_empregado, _cpf, _sexo, _data_nascimento, _celular, _email, _endereco, _bairro, _cidade, _estado, _pais, _status)
    empregado.setTelefone(_telefone)
    empregado.setComplemento(_complemento)
    empregado.setCep(_cep)  
    return controllerEmpregado.add_empregado(empregado)


@app.route("/empregados",  methods=['GET'])
def listarEmpregados():
    return controllerEmpregado.listarEmpregados()


@app.route("/empregados/<int:id>",  methods=['GET'])
def getEmpregadoById(id):
    return controllerEmpregado.getById(id)


@app.route("/empregados",  methods=["PUT"])
def update_empregado():
    _json = request.json
    _id_empregado = str(_json['idEmpregado'])
    _nome_empregado = str(_json['nomeEmpregado'])
    _cpf = str(_json['cpf']) 
    _sexo = str(_json['sexo'])
    _data_nascimento = str(_json['dataNascimento'])
    _telefone = str(_json['telefone'])
    _celular = str(_json['celular'])
    _email = str(_json['email'])
    _endereco = str(_json['endereco'])
    _complemento = str(_json['complemento'])
    _bairro = str(_json['bairro'])
    _cep = str(_json['cep'])
    _cidade = str(_json['cidade'])
    _estado = str(_json['estado'])
    _pais = str(_json['pais'])
    _status = str(_json['status'])
    
    empregado = Empregado(_nome_empregado, _cpf, _sexo, _data_nascimento, _celular, _email, _endereco, _bairro, _cidade, _estado, _pais, _status)
    empregado.setIdEmpregado(_id_empregado)
    empregado.setTelefone(_telefone)
    empregado.setComplemento(_complemento)
    empregado.setCep(_cep) 
    return controllerEmpregado.update_empregado(empregado)


@app.route("/empregados/<int:id>", methods=['DELETE'])
def delete_empregado(id):
    return controllerEmpregado.delete_empregado(id) 



##ROTAS DE FORNECEDORESPF

@app.route("/fornecedorespf",  methods=["POST"])
def add_fornecedorpf():
    _json = request.json
    _nome_fornecedorpf = str(_json['nome'])
    _nick_name = str(_json['nickName'])
    _cpf = str(_json['cpf']) 
    _sexo = str(_json['sexo'])
    _data_nascimento = str(_json['dataNascimento'])
    _telefone = str(_json['telefone'])
    _celular = str(_json['celular'])
    _email = str(_json['email'])
    _endereco = str(_json['endereco'])
    _complemento = str(_json['complemento'])
    _bairro = str(_json['bairro'])
    _cep = str(_json['cep'])
    _cidade = str(_json['cidade'])
    _estado = str(_json['estado'])
    _pais = str(_json['pais'])
    _status = str(_json['status'])

    fornecedorpf = FornecedorPF(_nome_fornecedorpf, _cpf, _sexo, _data_nascimento, _celular, _email, _endereco, _bairro, _cidade, _estado, _pais, _status)
    fornecedorpf.setNickName(_nick_name)
    fornecedorpf.setTelefone(_telefone)
    fornecedorpf.setComplemento(_complemento)
    fornecedorpf.setCep(_cep)
    return controllerFornecedorPF.add_fornecedorpf(fornecedorpf)


@app.route("/fornecedorespf",  methods=['GET'])
def listarFornecedorespf():
    return controllerFornecedorPF.listarFornecedorespf()


@app.route("/fornecedorespf/<int:id>",  methods=['GET'])
def getFornecedorPFById(id):
    return controllerFornecedorPF.getFornecedorPFById(id)


@app.route("/fornecedorespf",  methods=["PUT"])
def update_fornecedorpf():
    _json = request.json
    _id_fornecedorpf = str(_json['idFornecedorPF'])
    _nome_fornecedorpf = str(_json['nome'])
    _nick_name = str(_json['nickName'])
    _cpf = str(_json['cpf']) 
    _sexo = str(_json['sexo'])
    _data_nascimento = str(_json['dataNascimento'])
    _telefone = str(_json['telefone'])
    _celular = str(_json['celular'])
    _email = str(_json['email'])
    _endereco = str(_json['endereco'])
    _complemento = str(_json['complemento'])
    _bairro = str(_json['bairro'])
    _cep = str(_json['cep'])
    _cidade = str(_json['cidade'])
    _estado = str(_json['estado'])
    _pais = str(_json['pais'])
    _status = str(_json['status'])

    fornecedorpf = FornecedorPF(_nome_fornecedorpf, _cpf, _sexo, _data_nascimento, _celular, _email, _endereco, _bairro, _cidade, _estado, _pais, _status)
    fornecedorpf.setIdFornecedorPF(_id_fornecedorpf)
    fornecedorpf.setNickName(_nick_name)
    fornecedorpf.setTelefone(_telefone)
    fornecedorpf.setComplemento(_complemento)
    fornecedorpf.setCep(_cep)
    return controllerFornecedorPF.update_fornecedorpf(fornecedorpf)


@app.route("/fornecedorespf/<int:id>", methods=['DELETE'])
def delete_fornecedorpf(id):
    return controllerFornecedorPF.delete_fornecedorpf(id)


##ROTAS DE FORNECEDORESPJ

@app.route("/fornecedorespj",  methods=["POST"])
def add_fornecedorpj():
    _json = request.json
    _razao_social = str(_json['razaoSocial'])
    _nome_fantasia = str(_json['nomeFantasia'])
    _nick_name = str(_json['nickName'])
    _cnpj = str(_json['cnpj']) 
    _telefone = str(_json['telefone'])
    _celular = str(_json['celular'])
    _email = str(_json['email'])
    _endereco = str(_json['endereco'])
    _complemento = str(_json['complemento'])
    _bairro = str(_json['bairro'])
    _cep = str(_json['cep'])
    _cidade = str(_json['cidade'])
    _estado = str(_json['estado'])
    _pais = str(_json['pais'])
    _status = str(_json['status'])

    fornecedorpj = FornecedorPJ(_razao_social, _nome_fantasia, _cnpj, _celular, _email, _endereco, _bairro, _cidade, _estado, _pais, _status)
    fornecedorpj.setNickName(_nick_name)
    fornecedorpj.setTelefone(_telefone)
    fornecedorpj.setComplemento(_complemento)
    fornecedorpj.setCep(_cep)
    return controllerFornecedorPJ.add_fornecedorpj(fornecedorpj)


@app.route("/fornecedorespj",  methods=['GET'])
def listarFornecedorespj():
    return controllerFornecedorPJ.listarFornecedorespj()

@app.route("/fornecedorespj/<int:id>",  methods=['GET'])
def getFornecedorPJById(id):
    return controllerFornecedorPJ.getFornecedorPJById(id)

@app.route("/fornecedorespj",  methods=["PUT"])
def update_fornecedorpj():
    _json = request.json
    _id_fornecedorpj = str(_json['idFornecedorPJ'])
    _razao_social = str(_json['razaoSocial'])
    _nome_fantasia = str(_json['nomeFantasia'])
    _nick_name = str(_json['nickName'])
    _cnpj = str(_json['cnpj']) 
    _telefone = str(_json['telefone'])
    _celular = str(_json['celular'])
    _email = str(_json['email'])
    _endereco = str(_json['endereco'])
    _complemento = str(_json['complemento'])
    _bairro = str(_json['bairro'])
    _cep = str(_json['cep'])
    _cidade = str(_json['cidade'])
    _estado = str(_json['estado'])
    _pais = str(_json['pais'])
    _status = str(_json['status'])

    fornecedorpj = FornecedorPJ(_razao_social, _nome_fantasia, _cnpj, _celular, _email, _endereco, _bairro, _cidade, _estado, _pais, _status)
    fornecedorpj.setIdFornecedorPJ(_id_fornecedorpj)
    fornecedorpj.setNickName(_nick_name)
    fornecedorpj.setTelefone(_telefone)
    fornecedorpj.setComplemento(_complemento)
    fornecedorpj.setCep(_cep)
    return controllerFornecedorPJ.update_fornecedorpj(fornecedorpj)


@app.route("/fornecedorespj/<int:id>", methods=['DELETE'])
def delete_fornecedorpj(id):
    return controllerFornecedorPJ.delete_fornecedorpj(id)




##ROTAS DE PRODUTOS

@app.route("/produtos",  methods=["POST"])
def add_produto():
    _json = request.json
    _desc_produto = str(_json['descProduto'])
    _tipo_volume = str(_json['tipoVolume'])
    _preco = str(_json['preco'])
    _id_fornecedorpj = str(_json['idFornecedorPJ']) 
    _id_fornecedorpf = str(_json['idFornecedorPF'])
    _status = str(_json['status'])

    produto = Produto(_desc_produto, _tipo_volume, _preco, _id_fornecedorpj, _id_fornecedorpf, _status)
    return controllerProduto.add_produto(produto)


@app.route("/produtos",  methods=['GET'])
def listarProdutos():
    return controllerProduto.listarProdutos()

@app.route("/produtos/<int:id>",  methods=['GET'])
def getProdutoById(id):
    return controllerProduto.getProdutoById(id)

@app.route("/produtos",  methods=["PUT"])
def update_produto():
    _json = request.json
    _id_produto = str(_json['idProduto'])
    _desc_produto = str(_json['descProduto'])
    _tipo_volume = str(_json['tipoVolume'])
    _preco = str(_json['preco'])
    _id_fornecedorpj = str(_json['idFornecedorPJ']) 
    _id_fornecedorpf = str(_json['idFornecedorPF'])
    _status = str(_json['status'])
    produto = Produto(_desc_produto, _tipo_volume, _preco, _id_fornecedorpj, _id_fornecedorpf, _status)
    produto.setIdProduto(_id_produto)
    return controllerProduto.update_produto(produto)


@app.route("/produtos/<int:id>", methods=['DELETE'])
def delete_produto(id):
    return controllerProduto.delete_produto(id)


##ROTAS DE PEDIDOS

@app.route("/pedidos",  methods=["POST"])
def add_pedido():
    _json = request.json
    _pedido = _json['pedido']
    return controllerPedido.add_pedido(_pedido)


@app.route("/pedidos",  methods=['GET'])
def listarPedidos():
    return controllerPedido.listarPedidos()

@app.route("/pedidos/<int:id>",  methods=['GET'])
def getPedidoById(id):
    return controllerPedido.getPedidoById(id)

@app.route("/pedidos",  methods=["PUT"])
def update_pedido():
    _json = request.json
    _pedido = _json['pedido']
    return controllerPedido.update_pedido(_pedido)


@app.route("/pedidos/<int:id>", methods=['DELETE'])
def delete_pedido(id):
    return controllerPedido.delete_pedido(id)