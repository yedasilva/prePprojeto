# preProjeto
Apresentação de Pré-projeto de Site

# Exercícios anteriores de sala de aula

**Conexão com banco de dados**

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
<img align="right" src="images/mascote-html5.png" width="200">




# A very simple Flask Hello World app for you to get started with...
import sys

from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def programa_principal():
    HTML = '''
        <html>
        <body>
            <h1>Site de exercícios</h1>
            <h2>Hello World!</h2>
            <br>
            <a href="/info">1. Link para informações</a>
            <br>
            <a href="/teste1">2. Link para dicionário</a>
            <br>
            <a href="/teste2">3. Link para tabela</a>
            <br>
            <a href="/banco">4. Link para banco v2</a>
            <br>
            <a href="/loginpag">5. Link para login</a>
            <br>
            <a href="/cadastro_cli">5. Link para Cadastro</a>
        </body>
        </html>

        '''
    return HTML

@app.route('/login', methods=['POST'])
def fazer_login():
    html = '''
    <h1>Codigo depois de ter feito login:</h1>
    <br><br><br>
    __MENSAGEM__
    '''

    nome = request.form['login']
    pwd = request.form['senha']


    if nome=='admin' and pwd=='abc123':
        msg = '<h2>voce tem superpoderes..</h2>'
    else:
        msg = f'obrigado por logar. seu nome: {nome}'

    html = html.replace('__MENSAGEM__', msg)
    return html

@app.route('/loginpag')
def pag_login():
    html = '''
    <form action="/login" method="post">
        login:
        <input type="text" name="login">
        <br>
        passwd:
        <input type="text" name="senha">
        <br>
        <input type="submit" value="login">
    </form>
    '''
    return html


@app.route('/info')
def informacoes():
    return str(sys.version)

@app.route('/teste1')
def funcao_2():
    dados = ['dados1','pegos de dentro','da variavel...']

    itens = ''
    for data in dados:
        itens += f'<li>{data}</li>'
    print(itens)

    msg = '''
    <html>
        <body>
            <h1>Teste ...</h1>
            <br>
            <hr>
            <ul>

                __MEUS_ITENS__

            </ul>
        </body>
    </html>
    '''

    msg = msg.replace('__MEUS_ITENS__', itens)

    return msg


@app.route('/teste2')
def funcao_3():

    cardapio = {
        "x-salada":22.5,
        "x-burguer":45.20,
        "coca-cola 600": 12.5,
        "brigadeiro":7.0
        }

    # Gerar o HTML da tabela
    html_tabela = '<table border="1">\n'
    html_tabela += '<tr><th>Item</th><th>Preço</th></tr>\n'

    # Percorrer o dicionário e criar as linhas da tabela
    for chave, valor in cardapio.items():
        html_tabela += f'<tr><td>{chave}</td><td>{valor}</td></tr>\n'

    html_tabela += '</table>'

    # Exibir o HTML gerado
    print(html_tabela)


    return html_tabela


@app.route('/cadastro_cli')
def cad_cli():

    #clientes = {}


    msg = '''
    <html>
        <body>
            <h1>Cadastro de clientes</h1>
            <br>
            <hr>
            <form action>
                <label for="name">Nome:</label><br>
                <input type="text" id="name" name="nome"><br>
                <label for="telefone">Telefone:</label><br>
                <input type="text" id="telefone" name="telefone"><br>
                <label for="endereco">Endereço:</label><br>
                <input type="text" id="endereco" name="endereco"><br>
                <br>
                <input type="submit" value="OK">
            </form>
        </body>
    </html>
    '''


    return msg

from DB_aulaPython import get_database, sql_execute

@app.route('/banco')
def conecta_banco():
    msg = 'executando: select * from tbCliente<br>\n'
    db = get_database()

    #return sql_execute('select * from tbCliente', db)

    valores = sql_execute('select * from tbCliente', db)
    for val in valores:
        msg += f'{val}<br>\n'
    return msg

# Pré-projeto de site de Mercadorias


