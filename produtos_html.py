
html = '''
<html>
    <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
        <h1>Lista dos Produtos</h1>
        <p>
            Veja abaixo os últimos produtos...
        </p>
        <br>
        <table>
            <_LISTAR_PRODUTOS_>
        </table>
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js"></script>
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
            <br>
            Valor: R$ <_VALOR_>
        </td>
    </tr>
'''

def gerar_html_produtos(lista):
    lista_html = ''
    for prod in lista:
        html_prod = f'{html_template}'
        html_prod = html_prod.replace('<_NOME_PRODUTO_>', prod['nome'])
        html_prod = html_prod.replace('__IMAGEM__', prod['imagem'])
        valor = str(prod['valor'])
        html_prod = html_prod.replace('<_VALOR_>', valor)
        html_prod = html_prod.replace('<_DESCRICAO_>', prod['descricao'])
        lista_html = lista_html + html_prod

    ret = html.replace('<_LISTAR_PRODUTOS_>', lista_html)
    return ret