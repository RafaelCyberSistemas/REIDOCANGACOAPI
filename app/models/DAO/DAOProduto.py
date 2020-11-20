import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import json 
from decimal import Decimal as D
from flask import flash, request
from app.models.classes_basicas.Produto import Produto



def add_produto(p):
    try:
        if p.getIdFornecedorPF()==None:
            sql = "INSERT INTO PRODUTOS(desc_produto, tipo_volume, preco, id_fornecedorpj, status) VALUES(%s, %s, %s, %s, %s)"
            data = (p.getDescProduto(), p.getTipoVolume(), p.getPreco(), p.getIdFornecedorPJ(), p.getStatus())
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('PRODUTO ' + p.getDescProduto() + ' added successfully!')
            resp.status_code = 200
            return resp
        else:
            if p.getIdFornecedorPJ()==None:
                sql = "INSERT INTO PRODUTOS(desc_produto, tipo_volume, preco, id_fornecedorpf, status) VALUES(%s, %s, %s, %s, %s)"
                data = (p.getDescProduto(), p.getTipoVolume(), p.getPreco(), p.getIdFornecedorPF(), p.getStatus())
                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.execute(sql, data)
                conn.commit()
                resp = jsonify('PRODUTO ' + p.getDescProduto() + ' added successfully!')
                resp.status_code = 200
                return resp
                
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()


def listarProdutos():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        sql = "SELECT id_produto idProduto, desc_produto descProduto, tipo_volume tipoVolume, preco, id_fornecedorpj idFornecedorPJ, id_fornecedorpf idFornecedorPF, status  FROM PRODUTOS"
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
        

def getProdutoById(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        sql = "SELECT id_produto idProduto, desc_produto descProduto, tipo_volume tipoVolume, preco, id_fornecedorpj idFornecedorPJ, id_fornecedorpf idFornecedorPF, status  FROM PRODUTOS  WHERE id_produto=%s"
        cursor.execute(sql, id)
        rows = cursor.fetchone()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as ex:
        print(ex)
    finally:
        cursor.close() 
        conn.close()


def update_produto(p):
    try:
        if p.getIdFornecedorPF()==None:
            sql = "UPDATE PRODUTOS SET desc_produto=%s, tipo_volume=%s, preco=%s, id_fornecedorpj=%s, status=%s WHERE id_produto=%s"
            data = (p.getDescProduto(), p.getTipoVolume(), p.getPreco(), p.getIdFornecedorPJ(), p.getStatus(), p.getIdProduto())
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('PRODUTO: updated successfully!')
            resp.status_code = 200
            return resp
        else:
            if p.getIdFornecedorPJ()==None:
                sql = "UPDATE PRODUTOS SET desc_produto=%s, tipo_volume=%s, preco=%s, id_fornecedorpf=%s, status=%s WHERE id_produto=%s"
                data = (p.getDescProduto(), p.getTipoVolume(), p.getPreco(), p.getIdFornecedorPF(), p.getStatus(), p.getIdProduto())
                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.execute(sql, data)
                conn.commit()
                resp = jsonify('PRODUTO: ' + p.getDescProduto() + ' updated successfully!')
                resp.status_code = 200
                return resp
                
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()

        

def delete_produto(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        sql = "DELETE FROM PRODUTOS WHERE id_produto=%s"
        cursor.execute(sql, id)
        conn.commit()
        resp = jsonify('Produto deleted successfully!')
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