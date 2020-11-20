from app.models.DAO import DAOPedido
import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request
from app.models.classes_basicas.Pedido import Pedido
from app.models.classes_basicas.Produto import Produto
import json
from datetime import date, datetime
        


def add_pedido(_pedido):
    try:
        idUser = _pedido['idUser']
        pedido = Pedido(idUser)
        data_atual = date.today()
        dataFormatada = data_atual.strftime('%d/%m/%Y')
        pedido.setDataPedido(dataFormatada)
        pedido.setStatusPedido("Finalizado")
        pedido.listaProdutos.clear()

        listaProdutos = _pedido['listaProdutos']

        for prod in listaProdutos:
            produto = Produto(None, prod['tipoVolume'], prod['preco'], None, None, None)
            produto.setIdProduto(prod['idProduto'])
            produto.setQuantidade(prod['quantidade'])
            pedido.listaProdutos.append(produto)

        return DAOPedido.add_pedido(pedido)
    except Exception as ex:
        print(ex)


def listarPedidos():
    try:
        return DAOPedido.listarPedidos()
    except Exception as ex:
        print(ex)
    

def getPedidoById(id):
    try:
        return DAOPedido.getPedidoById(id)
    except Exception as ex:
        print(ex)
    

def update_pedido(_pedido):
    try:
        idUser = _pedido['idUser']
        pedido = Pedido(idUser)
        data_atual = date.today()
        dataFormatada = data_atual.strftime('%d/%m/%Y')
        pedido.setIdPedido(_pedido['idPedido'])
        pedido.setDataPedido(dataFormatada)
        pedido.setStatusPedido("Finalizado")
        pedido.listaProdutos.clear()

        listaProdutos = _pedido['listaProdutos']

        for prod in listaProdutos:
            produto = Produto(None, prod['tipoVolume'], prod['preco'], None, None, None)
            produto.setIdProduto(prod['idProduto'])
            produto.setQuantidade(prod['quantidade'])
            pedido.listaProdutos.append(produto)

        return DAOPedido.update_pedido(pedido)
    except Exception as ex:
        print(ex)
       

def delete_pedido(id):
    try:
        return DAOPedido.delete_pedido(id)
    except Exception as ex:
        print(ex)
    