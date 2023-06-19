# prePprojeto
Apresentação de Pré-projeto de Site

# Exercícios anteriores de sala de aula

import mysql.connector as database
import os
import json

mydir = os.path.dirname(__file__)
configfname = f'{mydir}/config.json'

def get_database():
    with open(configfname, 'r') as file:
        config = json.load(file)

    mysql = database.connect(**config)
    return mysql


def sql_execute(sql, mydb):
    conexao = mydb.cursor()
    conexao.execute(sql)
    ret = list(conexao)
    return ret


{
"host": "yedagabriela.mysql.pythonanywhere-services.com",
"user": "yedagabriela",
"password": "GabyPAW/1708",
"database": "yedagabriela$DB_aulaPython"
}

# Pré-projeto de site de Mercadorias


