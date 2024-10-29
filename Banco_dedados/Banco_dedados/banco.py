from os import system
system('cls')
import pyodbc
import pandas as pd 

#instalar o comando = pip install pyodbc 
#Defina os parâmetros da conexão 

server = 'NOTEBOOK08' #Substitua pelo nome ou endereço do seu servidor SQL 
database = 'bd_manha' # Substitua pelo nome do seu banco de dados 

#String de conexão para autenticação do Windows (Trusted Connection)
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'


try:

    #Estabelecendo a conexão 
    conn = pyodbc.connect(connection_string)
    print("Conexão com o banco de dados estabelecida com sucesso!")
    
    #Exemplo de consulta
    #cursor = conn.cursor()
    #cursor.execute("SELECT * FROM cliente") #Substitua pela sua consulta SQL
    
    
    #Exportando a base de dados para um arquivo CSV
    df = pd.read_sql("SELECT * FROM cliente", conn)
    df.to_csv("Jorge.csv")
    
    #for row in cursor: 
       # print(row)
        
    # Fechando a conexão
    #cursor.close()
    conn.close()
    
except Exception as e: 
    print("Erro ao conectar ao banco de dados:", e)
