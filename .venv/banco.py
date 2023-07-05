

produtos = []


def adicionar_produto(nome, descricao, valor,quantidade, imagem):
    produto = {
        "nome": nome,
        "descricao": descricao,
        "valor": valor,
        "quantidade": quantidade,
        "imagem": imagem
    }
    produtos.append(produto)

def consulta_produtos():
    return produtos

def consulta_prod_nome(nome):
    for prod in produtos:
        if nome == prod['nome']:
            return prod
        
    return None

compra = []

def adicionar_carrinho(nome, quantidade):
    prod = consulta_prod_nome(nome)
    if prod!= None:

        carrinho = {
            "nome": nome,
            "valorUnit":prod['valor'],
            "valorTotal": float(prod['valor'])*int(quantidade),
            "quantidade": quantidade,
        }
        compra.append(carrinho)

def consulta_carrinho():
    return compra


print(compra)