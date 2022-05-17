import os 

from pymongo import MongoClient
from pymongo import MongoClient
import pymongo

from dotenv import load_dotenv
load_dotenv() # Lê e carrega as variáveis de ambiente do arquivo .env

# Conectar com o cluster e gera database
def get_database():
    
    """
    
    out - return client[''] -> retorna cliente, conexão com banco de dados 

    """

    user     = os.environ.get("USER")
    password = os.environ.get("PASSWORD")
    cluster  = 'pymongoserver.hea0x'

    # Gera uma string de conexão python para o mongodb Atlas
    CONNECTION_STRING = f"mongodb+srv://{user}:{password}@{cluster}.mongodb.net/?retryWrites=true&w=majority"

    # Cria uma conexão usando MongoCliente.

    client = MongoClient(CONNECTION_STRING)
    print("Conexão realizada com sucesso ao Mongo Atlas version:", client.server_info()['version'])

    #Cria banco de dados de exemplo
    return client['customers']

# Realiza a carga de Dados
def data_upload(list_of_dicts):

    """
    in: list_of_dicts = recebe como parâmetro uma lista de dicionários a serem carregados na base
    
    """
    dbname = get_database()
    new_customers = dbname['new_customers']

    new_customers.insert_many(list_of_dicts)
    print('Carga de dados realizada com Sucesso')



