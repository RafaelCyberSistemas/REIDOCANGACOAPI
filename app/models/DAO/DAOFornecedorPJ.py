import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request
from app.models.classes_basicas.FornecedorPJ import FornecedorPJ


def add_fornecedorpj(f):
	try:	
		sql = "INSERT INTO FORNECEDORESPJ(razao_social, nome_fantasia, nickname, cnpj, telefone, celular, email, endereco, complemento, bairro, cep, cidade, estado, pais, status) VALUES(%s, %s, %s, %s,%s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s)"
		data = (f.getRazaoSocial(), f.getNomeFantasia(),  f.getNickName(), f.getCnpj(), f.getTelefone(), f.getCelular(), f.getEmail(), f.getEndereco(), f.getComplemento(), f.getBairro(), f.getCep(), f.getCidade(), f.getEstado(), f.getPais(), f.getStatus())
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute(sql, data)
		conn.commit()
		resp = jsonify('Fornecedor ' + f.getNomeFantasia() + ' added successfully!')
		resp.status_code = 200
		return resp
	except Exception as ex:
		print(ex)
	finally:
		cursor.close() 
		conn.close()


def listarFornecedorespj():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		sql = "SELECT id_fornecedorpj idFornecedorPJ, razao_social razaoSocial, nome_fantasia nomeFantasia ,nickname nickName, cnpj, telefone, celular, email, endereco, complemento, bairro, cep, cidade, estado, pais, status from FORNECEDORESPJ"
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


def getFornecedorPJById(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        sql = "SELECT id_fornecedorpj idFornecedorPJ, razao_social razaoSocial, nome_fantasia nomeFantasia ,nickname nickName, cnpj, telefone, celular, email, endereco, complemento, bairro, cep, cidade, estado, pais, status from FORNECEDORESPJ WHERE id_fornecedorpj=%s"
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


def update_fornecedorpj(f):
    try:
        sql = "UPDATE FORNECEDORESPJ SET razao_social=%s, nome_fantasia=%s, nickname=%s, cnpj=%s, telefone=%s, celular=%s, email=%s, endereco=%s, complemento=%s, bairro=%s, cep=%s, cidade=%s, estado=%s, pais=%s, status=%s WHERE id_fornecedorpj=%s"
        data = (f.getRazaoSocial(), f.getNomeFantasia(), f.getNickName(), f.getCnpj(), f.getTelefone(), f.getCelular(), f.getEmail(), f.getEndereco(), f.getComplemento(), f.getBairro(), f.getCep(), f.getCidade(), f.getEstado(), f.getPais(), f.getStatus(), f.getIdFornecedorPJ())
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, data)
        conn.commit()
        resp = jsonify('Fornecedor ' + f.getNomeFantasia() + ' updated successfully!')
        resp.status_code = 200
        return resp
    except Exception as ex:
        print(ex)
    finally:
        cursor.close()
        conn.close()


def delete_fornecedorpj(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        sql = "DELETE FROM FORNECEDORESPJ WHERE id_fornecedorpj=%s"
        cursor.execute(sql, id)
        conn.commit()
        resp = jsonify('Fornecedor deleted successfully!')
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