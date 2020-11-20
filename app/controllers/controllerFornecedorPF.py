from app.models.DAO import DAOFornecedorPF
import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request
from app.models.classes_basicas.FornecedorPF import FornecedorPF


def add_fornecedorpf(f):

    try:
        return DAOFornecedorPF.add_fornecedorpf(f)
    except Exception as ex:
        print(ex)


def listarFornecedorespf():
    try:
        return DAOFornecedorPF.listarFornecedoresPF()
    except Exception as ex:
        print(ex)
    

def getFornecedorPFById(id):
    try:
        return DAOFornecedorPF.getFornecedorPFById(id)
    except Exception as ex:
        print(ex)
    

def update_fornecedorpf(f):
    try:
        return DAOFornecedorPF.update_fornecedorpf(f)
    except Exception as ex:
        print(ex)
       

def delete_fornecedorpf(id):
    try:
        return DAOFornecedorPF.delete_fornecedorpf(id)
    except Exception as ex:
        print(ex)
    