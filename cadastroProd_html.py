import json
from flask import Flask, request

html = '''
<html>
    <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
     
        <p>
        <_USUARIO_LOGADO_>
        </p>
        <h1>Catálogo dos Produtos</h1>

        <form class="upload-form" action="/upload" method="post" enctype="multipart/form-data">
            <input type="file" name="imagem" accept="image/*" required>
            <br>
            <button type="submit">Enviar</button>
        </form>
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
        </td>
        <td>
            <_NOME_PRODUTO_>
        </td>
    </tr>
    <tr>
        <td>
            <img src="static/__IMAGEM__" width="150px">
        </td>
        <td>
            <_DESCRICAO_>
            <br><br>
            <labe>Quantidade: </label>
            <input id="quantidade" name="quantidade" min="1" value="1"/> 
            <labe>Valor: R$</label>
            <input id="valor" name="valor" value="<_VALOR_>" disabled/>
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


def cadastrar_produto():
    lista =[] #lista vazia

    # Solicita as informações do produto ao usuário
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    imagem = request.files['imagem']
    imagem.save('uploads/' + imagem.filename)    
    descricao = input("Digite uma descrição do produto: ")
    quantidade = int(input("Digite a quantidade do produto: "))
    #loop para adicionar itens à lista usando append
    for i in range (3):
        

        item = {
            'item': str(i+1),
            'nome': nome,
            'imagem': imagem,
            'valor': preco,
            'descricao': descricao,
            'quantidade': quantidade,
        }
        lista.append(item)
    print (lista)

    return 'Upload realizado com sucesso!'


cadastrar_produto()