from app.models.DAO import  DAOEmpregado
import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.classes_basicas.Empregado import Empregado


def add_empregado(empregado):
    return DAOEmpregado.add_empregado(empregado)

def listarEmpregados():
    return DAOEmpregado.listarEmpregados()

def getById(id):
    return DAOEmpregado.getById(id)

def update_empregado(empregado):
    return DAOEmpregado.update_empregado(empregado)   

def delete_empregado(id):
    return DAOEmpregado.delete_empregado(id)
        
