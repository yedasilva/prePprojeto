
html = '''
<html>
    <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
        <h1>Carrinho de compras</h1>
        <br>
        <p>
            Veja abaixo os últimos produtos...
        </p>
        <br>
        <table>
            <_LISTAR_PRODUTOS_>
        </table>
        <br><br>
        <input type="submit" value="Comprar">
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.min.js"></script>
    </body>
</html>
'''

html_template = '''
    <tr>
        <td>
        <br>
        </td>
        <td>
            <input type="checkbox" id="check">
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
            <input min="1" value="1"> 
            Valor: R$ <_VALOR_>
            <br><br>    
            <p>Total: R$ {{ total }}</p>    
            <input type="submit" value="Escolher">
        </td>        
    </tr>
    
'''
# def calcular(lista):
#     lista_html = ''
#     for prod in lista:
#         valor_unitario = float(prod['valor'])
#         quantidade = int(prod['quantidade'])
#         total = valor_unitario * quantidade
#     return render_template('resultado.html', valor=valor_unitario, quantidade=quantidade, total=total)

def gerar_html_carrinho(lista):
    lista_html = ''
    for prod in lista:
        html_car = f'{html_template}'
        html_car = html_car.replace('<_NOME_PRODUTO_>', prod['nome'])
        html_car = html_car.replace('__IMAGEM__', prod['imagem'])
        valor = str(prod['valor'])
        html_car = html_car.replace('<_VALOR_>', valor)
        html_car = html_car.replace('<_DESCRICAO_>', prod['descricao'])
        quantidade = str(prod['quantidade'])
        html_car = html_car.replace('<_QUANT_>', quantidade)
        lista_html = lista_html + html_car  

    ret = html.replace('<_LISTAR_PRODUTOS_>', lista_html)
    return ret