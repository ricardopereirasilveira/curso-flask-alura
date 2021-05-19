import mysql.connector


conexao = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="admin"
)

if conexao.is_connected():
    print('O banco de dados está conectado!')