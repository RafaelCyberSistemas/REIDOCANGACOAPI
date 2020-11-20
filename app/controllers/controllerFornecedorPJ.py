from app.models.DAO import DAOFornecedorPJ
import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request
from app.models.classes_basicas.FornecedorPJ import FornecedorPJ


def add_fornecedorpj(f):
    try:
        return DAOFornecedorPJ.add_fornecedorpj(f)
    except Exception as ex:
        print(ex)


def listarFornecedorespj():
    try:
        return DAOFornecedorPJ.listarFornecedorespj()
    except Exception as ex:
        print(ex)
    

def getFornecedorPJById(id):
    try:
        return DAOFornecedorPJ.getFornecedorPJById(id)
    except Exception as ex:
        print(ex)
    

def update_fornecedorpj(f):
    try:
        return DAOFornecedorPJ.update_fornecedorpj(f)
    except Exception as ex:
        print(ex)
       

def delete_fornecedorpj(id):
    try:
        return DAOFornecedorPJ.delete_fornecedorpj(id)
    except Exception as ex:
        print(ex)
    