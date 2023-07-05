import banco
import carrinho_html
import produtos_html
import cadastroProd_html
from flask import Flask,redirect, session,request, url_for
from flask_session import Session


app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/logout")
def logout():
    session["usuarioLogado"] = None
    session["usuarioAdmin"] = None
    return redirect("/")

@app.route('/')
def principal():
    produtos = banco.consulta_produtos()
    pag = produtos_html.gerar_html_produtos(produtos)
    return pag

@app.route('/compra_carrinho')
def comprar():
   carrinho = banco.consulta_carrinho()
   comp = carrinho_html.gerar_html_carrinho(carrinho)
   return comp

@app.route('/cliente')
def aut_cliente():
    msg = '''
    <html>
        <body>
            <h1>Mercearia</h1>
            <ul>
                <li>
                    Caso ainda não possua login, clique aqui para fazer o seu <a href="/cadastro_cli">cadastro</a>;
                </li>
                <li>
                    Faça seu <a href="/login_cli">login</a>
                </li>
            </ul>
        </body>
    </html>
    '''
    return msg

@app.route('/cadastro_cli') 
def cad_cli():
    msg = '''
    <html>
        <body>
            <h1>Cadastro de clientes</h1>
            <br>
            <hr>
            <form action="/cadastro" method="POST">
                <label for="name">Nome:</label><br>
                <input type="text" id="nome_pessoa" name="nome_pessoa"><br>
                <label for="email">E-mail:</label><br>
                <input type="text" id="email" name="email"><br>
                <label for="telefone">Telefone:</label><br>
                <input type="text" id="telefone" name="telefone"><br>
                <label for="endereco">Endereço:</label><br>
                <input type="text" id="endereco" name="endereco"><br>
                <label for="login">Login:</label><br>
                <input type="text" id="login" name="login"><br>
                <label for="senha">Senha:</label><br>
                <input type="text" id="senha" name="senha"><br>
                <br>

                <input type="submit" value="OK">
            </form>
        </body>
    </html>
    '''
    return msg

@app.route('/login_cli') 
def form_login():
    msg = '''
    <html>
        <body>
            <h1>Login</h1>
            <br>
            <hr>
            <form action="/login" method="POST">
                <label for="login">Login:</label><br>
                <input type="text" id="login" name="login"><br>
                <label for="senha">Senha:</label><br>
                <input type="password" id="senha" name="senha"><br>
                <br>
                <input type="submit" value="OK">
            </form>
            <ul>
                <li>
                    Caso ainda não possua login, clique aqui para fazer o seu <a href="/cadastro_cli">cadastro</a>;
                </li>
            </ul>
        </body>
    </html>
    '''
    return msg


@app.route('/compra',methods=('POST',))
def fazer_compra():
    if session.get('usuarioLogado') != None:
        msg = '''
        <html>
            <body>
                <h1>Pedido</h1>
                <br>
                <hr>
                O seu pedido foi cadastrado com valor total de R$10.
            </body>
        </html>
        
        '''
        return msg
    else:
        session['msgErro'] = 'Você não está logado, por favor realize o login.'
        
    return redirect("/")



VARIAVEIS = []

teste = {
    'nome': 'admin',
    'telefone': '21321456',
    'email': 'aaaa@bbbb',
    'login': 'admin',
    'senha': 'admin123',
    'endereco': 'sdfgshdçfklgh',
}
VARIAVEIS.append(teste)

def novo_cliente(nome, telefone,email,login, senha,endereco):
    novo_dado = {
       'nome': nome,
       'telefone': telefone,
       'email': email,
       'login': login,
       'senha': senha,
       'endereco': endereco,
    }
    VARIAVEIS.append(novo_dado)
    return redirect('/')


@app.route('/cadastro',methods=('POST',))
def fazer_cadastro():
    nome = request.form['nome_pessoa']
    login = request.form['login']
    senha = request.form['senha']
    email = request.form['email']
    telefone = request.form['telefone']
    endereco = request.form['endereco']
    return novo_cliente(nome, telefone,email,login, senha, endereco)
    




def check_login(login, passwd):
    
    for cadastro in VARIAVEIS:
        if login == cadastro['login'] and passwd == cadastro['senha']:
            session['usuarioLogado'] = cadastro
            if login=='admin':
                session['usuarioAdmin'] = cadastro 
            return True

    return False


@app.route('/login',methods=('POST',))
def fazer_login():
    login = request.form['login']
    senha = request.form['senha']
    
    if check_login(login, senha):
        print('ok, login.. fazer o resto..')
        return redirect('/') 
    
    else:
        #aut_cliente()
        session['msgErro'] = 'Usuário ou senha inválido.'
        print('erro.. tente de novo')
        return redirect('/')


@app.route('/cliente', methods=('POST', 'GET'))
@app.route('/login2',methods=('POST', 'GET'))
def login():
   user = None
   if request.method == 'POST':
      user = request.form['nome']

   if user == None:
      return redirect('/login_cli')

   return redirect(url_for('success',nome=user))

@app.route('/listar') 
def funcao_2():
    # Gerar o HTML da tabela
    html_tabela = '<table border="1">\n'
    html_tabela += '<tr><th>Item</th></tr>\n'

    # Percorrer o dicionário e criar as linhas da tabela
    for valor in VARIAVEIS:
        html_tabela += f'<tr><td>{valor}</td></tr>\n'

    html_tabela += '</table>'
    if session.get('usuarioLogado') != None:
        html_tabela += session['usuarioLogado'] ['nome']

    # Exibir o HTML gerado
    print(html_tabela)


    return html_tabela

@app.route('/cadastroProduto', methods=['GET', 'POST'])
def funcao_3():
    cadProd = cadastroProd_html.pag_cadProd()
    return cadProd

@app.route('/cadastrar', methods=[ 'GET','POST',])
def funcao_4():
    cadastroProd_html.add_product()
    return redirect("/")

@app.route("/consultar", methods=["GET"])
def consultar():
    produtos = banco.consulta_produtos()

    # Lógica para exibir os produtos na página de consulta

    return "Página de consulta de produtos"

@app.route('/carrinho/<nome_produto>/<quantidade>')
def adiciona_carrinho(nome_produto=None, quantidade=None):
    banco.adicionar_carrinho(nome_produto,quantidade)
    return redirect('/compra_carrinho')
  




#############################################
#
# ao copiar seu codigo para o pythonanywhere, remover as linhas abaixo!
#
#############################################


if __name__ == '__main__':
  app.run(debug=True, use_debugger=False, use_reloader=False)