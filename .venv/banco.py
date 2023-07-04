

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


print(produtos)