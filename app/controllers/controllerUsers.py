from app.models.DAO import DAOUsuario
import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.classes_basicas.User import User
        


def add_user(user):

    try:
        return DAOUsuario.add_user(user)
    except Exception as ex:
        print(ex)


def listarUsers():
    try:
        return DAOUsuario.listarUsers()
    except Exception as ex:
        print(ex)
    

def getById(id):
    try:
        return DAOUsuario.getById(id)
    except Exception as ex:
        print(ex)
    

def update_user(user):
    try:
        return DAOUsuario.update_user(user)
    except Exception as ex:
        print(ex)
       

def delete_user(id):
    try:
        return DAOUsuario.delete_user(id)
    except Exception as ex:
        print(ex)
    