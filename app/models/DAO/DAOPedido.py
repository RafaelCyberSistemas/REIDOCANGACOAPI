import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request
from app.models.classes_basicas.Pedido import Pedido


def add_pedido(p):   
    try:
        sql = "INSERT INTO PEDIDOS(data_pedido, status_pedido, id_user) VALUES(%s, %s, %s)"
        data = (p.getDataPedido(), p.getStatusPedido(), p.getIdUser())
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, data)
        idPedido = cursor.lastrowid
        valorTotalProduto = None
        conn.commit()
        cursor.close() 
        conn.close()
        

        for prod in p.listaProdutos:
            sql_pp = "INSERT INTO PEDIDO_PRODUTOS(id_pedido, id_produto, preco_produto, tipo_volume, quantidade_produto, valor_total_produto) VALUES(%s, %s, %s, %s, %s, %s)"
            valorTotalProduto = float(prod.getPreco()) * int(prod.getQuantidade())
            data = (idPedido, prod.getIdProduto(), prod.getPreco(), prod.getTipoVolume(), prod.getQuantidade(),  valorTotalProduto)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql_pp, data)
            conn.commit()
            cursor.close()
            conn.close()
 
        resp = jsonify('Pedido added successfully!')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    
        

def listarPedidos():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        sql = "SELECT P.id_pedido idPedido, P.data_pedido dataPedido, P.status_pedido statusPedido, P.id_user idUser, PP.id_produto idProduto, PP.preco_produto preco, PP.tipo_volume tipoVolume, PP.quantidade_produto quantidade, PP.valor_total_produto valorTotalProduto FROM PEDIDOS P INNER JOIN PEDIDO_PRODUTOS PP ON P.id_pedido = PP.id_pedido"
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
        

def getPedidoById(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        sql = "SELECT P.id_pedido idPedido, P.data_pedido dataPedido, P.status_pedido statusPedido, P.id_user idUser, PP.preco_produto preco, PP.tipo_volume tipoVolume, PP.quantidade_produto quantidade, PP.valor_total_produto valorTotalProduto FROM PEDIDOS P INNER JOIN PEDIDO_PRODUTOS PP ON P.id_pedido = PP.id_pedido WHERE P.id_pedido=%s"
        cursor.execute(sql, id)
        row = cursor.fetchall()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()


def update_pedido(p):
    try:
        sql = "UPDATE PEDIDOS SET data_pedido=%s, status_pedido=%s, id_user=%s WHERE id_pedido=%s"
        data = (p.getDataPedido(), p.getStatusPedido(), p.getIdUser(), p.getIdPedido())
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql, data)
        valorTotalProduto = None
        conn.commit()
        cursor.close() 
        conn.close()

        sql_del = "DELETE FROM PEDIDO_PRODUTOS WHERE id_pedido=%s"
        data = (p.getIdPedido())
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql_del, data)
        valorTotalProduto = None
        conn.commit()
        cursor.close() 
        conn.close()

        for prod in p.listaProdutos:
            sql_pp = "INSERT INTO PEDIDO_PRODUTOS(id_pedido, id_produto, preco_produto, tipo_volume, quantidade_produto, valor_total_produto) VALUES(%s, %s, %s, %s, %s, %s)"
            valorTotalProduto = float(prod.getPreco()) * int(prod.getQuantidade())
            data = (p.getIdPedido(), prod.getIdProduto(), prod.getPreco(), prod.getTipoVolume(), prod.getQuantidade(),  valorTotalProduto)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql_pp, data)
            conn.commit()
            cursor.close()
            conn.close()
 
        resp = jsonify('Pedido updated successfully!')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        

def delete_pedido(id):
    try:
        sql_del = "DELETE FROM PEDIDO_PRODUTOS WHERE id_pedido=%s"
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql_del, id)
        conn.commit()
        cursor.close() 
        conn.close()

        sql_del_ped = "DELETE FROM PEDIDOS WHERE id_pedido=%s"
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(sql_del_ped, id)
        conn.commit()
        cursor.close() 
        conn.close()

        resp = jsonify('Pedido deleted successfully!')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
        
        
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp
        
