import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request
from app.models.classes_basicas.Empregado import Empregado
		

def add_empregado(e):
	try:	
		sql = "INSERT INTO EMPREGADOS(nome_empregado, cpf, sexo, data_nascimento, telefone, celular, email, endereco, complemento, bairro, cep, cidade, estado, pais, status) VALUES(%s, %s, %s,%s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s)"
		data = (e.getNome(), e.getCpf(), e.getSexo(), e.getDataNascimento(), e.getTelefone(), e.getCelular(), e.getEmail(), e.getEndereco(), e.getComplemento(), e.getBairro(), e.getCep(), e.getCidade(), e.getEstado(), e.getPais(), e.getStatus())
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute(sql, data)
		conn.commit()
		resp = jsonify('Empregado' + e.getNome() + 'added successfully!')
		resp.status_code = 200
		return resp
	except Exception as ex:
		print(ex)
	finally:
		cursor.close() 
		conn.close()


def listarEmpregados():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		sql = "SELECT id_empregado idEmpregado, nome_empregado nomeEmpregado, cpf, sexo, data_nascimento dataNascimento, telefone, celular, email, endereco, complemento, bairro, cep, cidade, estado, pais, status from EMPREGADOS"
		cursor.execute(sql)
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as ex:
		print(ex)
	finally:
		cursor.close()
		conn.close()


def getById(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		sql = "SELECT id_empregado idEmpregado, nome_empregado nomeEmpregado, cpf, sexo, data_nascimento dataNascimento, telefone, celular, email, endereco, complemento, bairro, cep, cidade, estado, pais, status from EMPREGADOS WHERE id_empregado = %s"
		cursor.execute(sql, id)
		row = cursor.fetchone()
		resp = jsonify(row)
		resp.status_code = 200
		return resp
	except Exception as ex:
		print(ex)
	finally:
		cursor.close()
		conn.close()


def update_empregado(e):
	try:
		sql = "UPDATE EMPREGADOS SET nome_empregado=%s, cpf=%s, sexo=%s, data_nascimento=%s, telefone=%s, celular=%s, email=%s, endereco=%s, complemento=%s, bairro=%s, cep=%s, cidade=%s, estado=%s, pais=%s, status=%s  WHERE id_empregado=%s"
		data = (e.getNome(), e.getCpf(), e.getSexo(), e.getDataNascimento(), e.getTelefone(), e.getCelular(), e.getEmail(), e.getEndereco(), e.getComplemento(), e.getBairro(), e.getCep(), e.getCidade(), e.getEstado(), e.getPais(), e.getStatus(), e.getIdEmpregado())
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute(sql, data)
		conn.commit()
		resp = jsonify('Empregado updated successfully!')
		resp.status_code = 200
		return resp
	
	except Exception as ex:
		print(ex)
	finally:
		cursor.close()
		conn.close()


def delete_empregado(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        sql = "DELETE FROM EMPREGADOS WHERE id_empregado=%s"
        data = id
        cursor.execute(sql, data)
        conn.commit()
        resp = jsonify('Empregado deleted successfully!')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()



@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp
        
