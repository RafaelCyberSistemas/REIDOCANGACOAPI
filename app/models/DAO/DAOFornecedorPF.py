import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request
from app.models.classes_basicas.FornecedorPF import FornecedorPF


def add_fornecedorpf(f):
	try:	
		sql = "INSERT INTO FORNECEDORESPF(nome, nickname, cpf, sexo, data_nascimento, telefone, celular, email, endereco, complemento, bairro, cep, cidade, estado, pais, status) VALUES(%s, %s, %s, %s,%s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s)"
		data = (f.getNome(), f.getNickName(), f.getCpf(), f.getSexo(), f.getDataNascimento(), f.getTelefone(), f.getCelular(), f.getEmail(), f.getEndereco(), f.getComplemento(), f.getBairro(), f.getCep(), f.getCidade(), f.getEstado(), f.getPais(), f.getStatus())
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute(sql, data)
		conn.commit()
		resp = jsonify('Fornecedor ' + f.getNome() + ' added successfully!')
		resp.status_code = 200
		return resp
	except Exception as ex:
		print(ex)
	finally:
		cursor.close() 
		conn.close()


def listarFornecedoresPF():
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		sql = "SELECT id_fornecedorpf idFornecedorPF, nome, nickname nickName, cpf, sexo, data_nascimento dataNascimento, telefone, celular, email, endereco, complemento, bairro, cep, cidade, estado, pais, status from FORNECEDORESPF"
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


def getFornecedorPFById(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        sql = "SELECT id_fornecedorpf idFornecedorPF, nome, nickname nickName, cpf, sexo, data_nascimento dataNascimento, telefone, celular, email, endereco, complemento, bairro, cep, cidade, estado, pais, status from FORNECEDORESPF WHERE id_fornecedorpf=%s"
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


def update_fornecedorpf(f):
	try:
		sql = "UPDATE FORNECEDORESPF SET nome=%s, nickname=%s, cpf=%s, sexo=%s, data_nascimento=%s, telefone=%s, celular=%s, email=%s, endereco=%s, complemento=%s, bairro=%s, cep=%s, cidade=%s, estado=%s, pais=%s, status=%s  WHERE id_fornecedorpf=%s"
		data = (f.getNome(), f.getNickName(), f.getCpf(), f.getSexo(), f.getDataNascimento(), f.getTelefone(), f.getCelular(), f.getEmail(), f.getEndereco(), f.getComplemento(), f.getBairro(), f.getCep(), f.getCidade(), f.getEstado(), f.getPais(), f.getStatus(), f.getIdFornecedorPF())
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute(sql, data)
		conn.commit()
		resp = jsonify('Fornecedor ' + f.getNome() + ' updated successfully!')
		resp.status_code = 200
		return resp
	
	except Exception as ex:
		print(ex)
	finally:
		cursor.close()
		conn.close()


def delete_fornecedorpf(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        sql = "DELETE FROM FORNECEDORESPF WHERE id_fornecedorpf=%s"
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