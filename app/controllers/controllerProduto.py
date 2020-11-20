from app.models.DAO import DAOProduto
import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.classes_basicas.Produto import Produto




def add_produto(produto):
    try:
        if produto.getIdFornecedorPF()=="":
            produto.setIdFornecedorPF(None)
        else:
            if produto.getIdFornecedorPJ()=="":
                produto.setIdFornecedorPJ(None)

        return DAOProduto.add_produto(produto)
    except Exception as ex:
        print(ex)


def listarProdutos():
    try:
        return DAOProduto.listarProdutos()
    except Exception as ex:
        print(ex)
    

def getProdutoById(id):
    try:
        return DAOProduto.getProdutoById(id)
    except Exception as ex:
        print(ex)
    

def update_produto(produto):
    try:
        if produto.getIdFornecedorPF()=="":
            produto.setIdFornecedorPF(None)
        else:
            if produto.getIdFornecedorPJ()=="":
                produto.setIdFornecedorPJ(None)

        return DAOProduto.update_produto(produto)
    except Exception as ex:
        print(ex)
       

def delete_produto(id):
    try:
        return DAOProduto.delete_produto(id)
    except Exception as ex:
        print(ex)