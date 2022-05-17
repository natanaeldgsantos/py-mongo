
from database.connections import get_database, data_upload
from generator.test_data_generator import data_generator

profiles = data_generator(5) 


# Realizando a carga dos Dados no Mongo DB Server

data_upload(profiles)



