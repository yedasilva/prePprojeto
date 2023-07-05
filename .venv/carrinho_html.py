from flask import  session, request


html = '''
    <html>
        <head>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        </head>
        <body>
        
            <p>
            <_USUARIO_LOGADO_>
            </p>
            
            <h1>Carrinho de compras</h1>
            <p>
                Veja abaixo os produtos do seu carrinho...
            </p>
            <br>
            <form action="/compra" method="POST">
            <table>
                
                    <_LISTAR_PRODUTOS_>
                    <tr>
                    <td>
                    <input type="submit" value="Comprar">
                    </td>
                    <td>
                    
                    </td>
                    </tr>
                
            </table>
            </form>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
            <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js"></script>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.min.js"></script>
        </body>
    </html>
'''

html_template = '''
    <tr>
        
        <td>
            <_NOME_PRODUTO_>
        </td>
    </tr>
    <tr>
        
        <td>         
            
            <labe>Quantidade: </label>
            <_QUANTIDADE_>
            <labe>Valor Unitário: R$</label>
            <_VALOR_UNIT_>
            <labe>Valor Total: R$</label>
            <_VALOR_>
            <br><br>    
        </td>
        
    </tr>
'''

html_login = ''' 
        <ul>
                <li>
                    Caso ainda não possua login, clique aqui para fazer o seu <a href="/cadastro_cli">cadastro</a>;
                </li>
                <li>
                    Faça seu <a href="/login_cli">login</a>
                </li>
            </ul>

        ''' 

def gerar_html_carrinho(lista):
    lista_html = ''
    for prod in lista:
        html_prod = f'{html_template}'
        html_prod = html_prod.replace('<_NOME_PRODUTO_>', prod['nome'])
        valor = str(prod['valorUnit'])
        html_prod = html_prod.replace('<_VALOR_UNIT_>', valor)
        valortotal = str(prod['valorTotal'])
        html_prod = html_prod.replace('<_VALOR_>', valortotal)
        quantidade = str(prod['quantidade'])
        html_prod = html_prod.replace('<_QUANTIDADE_>', quantidade)
        
        lista_html = lista_html + html_prod

    ret = ''
    if session.get('usuarioLogado') != None:
        ret = html.replace('<_USUARIO_LOGADO_>','Olá, '+session['usuarioLogado'] ['nome']+'(<a href="/logout">sair</a>)')
        
    else:
        ret = html.replace('<_USUARIO_LOGADO_>',html_login)

    

    ret = ret.replace('<_LISTAR_PRODUTOS_>', lista_html)

    if session.get('msgErro') != None:
        ret+='<script>alert("'+ session['msgErro'] +'")</script>'
        session['msgErro'] = None
        print('exibir erro 2')

    return ret