
import banco
from flask import request


def pag_cadProd():

    msg = '''
            <html>
                <head>
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
                    <title>Cadastro de Produtos</title>
                </head>
                <body>
                    <h1>Cadastro de Produtos</h1>

                    <form action="/cadastrar" method="post" enctype="multipart/form-data">
                        <label for="nome">Nome do Produto:</label>
                        <input type="text" name="nome" id="nome" required><br><br>

                        <label for="descricao">Descrição do Produto:</label>
                        <input type="textarea" name="descricao" id="descricao" required><br><br>

                        <label for="valor">Preço do Produto:</label>
                        <input type="text" name="valor" id="valor" required><br><br>

                        <label for="quantidade">Quantidade do Produto:</label>
                        <input type="text" name="quantidade" id="quantidade" required><br><br>

                        <label for="imagem">Imagem do Produto:</label>
                        <input type="file" name="imagem" id="imagem" required><br><br>

                        <input type="submit" value="Cadastrar">
                    </form>

                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
                    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js"></script>
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.min.js"></script> 
                </body>
            </html>
        '''
    return msg

def add_product():
    nome = request.form.get("nome")
    descricao = request.form.get("descricao")
    valor = request.form.get("valor")
    quantidade = request.form.get("quantidade")
    imagem = request.files["imagem"]

    banco.adicionar_produto(nome, descricao, valor, quantidade, imagem.filename)
    
    # Salvar a imagem em algum diretório
    imagem.save("C:/Users/Gaby/Documents/GitHub/prePprojeto/.venv/static/" + imagem.filename)

    return "Produto cadastrado com sucesso!"