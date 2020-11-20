import mysql.connector

MYSQL_DATABASE_USER = 'reidocangaco'
MYSQL_DATABASE_PASSWORD = 'reidocangaco'
MYSQL_DATABASE_DB = 'reidocangacodb'
MYSQL_DATABASE_HOST = 'localhost'
MYSQL_DATABASE_CHARSET = 'utf8'

conn = mysql.connector.connect(host = MYSQL_DATABASE_HOST, user = MYSQL_DATABASE_USER, password = MYSQL_DATABASE_PASSWORD, database = MYSQL_DATABASE_DB, charset = MYSQL_DATABASE_CHARSET)
cursor = conn.cursor(dictionary=True)

query = "INSERT INTO EMPREGADOS(nome_empregado, cpf,sexo, data_nascimento, telefone, celular, email, endereco, bairro, cep, cidade, estado, pais) VALUES('Daniel', '089.098.876-34', 'M', '14/12/1984', '34443444', '81999999999', 'daniel@gmail', 'rua da paz', 'estancia', '60.999-345', 'recife', 'PE', 'Brasil')"

cursor.execute(query)
conn.commit()
