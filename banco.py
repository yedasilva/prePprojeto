def consulta_produtos():
    lista = []

    produto = {
        'nome': 'maçã',
        'imagem': 'maca.jpg',
        'valor': 1.25,
        'descricao': 'maçã vinda da república argentina',
        'quantidade': 2500,
    }

    lista.append(produto)

    p2 = {
        'nome': 'banana',
        'imagem': 'banana.jpg',
        'valor': 3.45,
        'descricao': 'banana vinda da américa central',
        'quantidade': 1200,
    }
    lista.append(p2)

    p3 = {
        'nome': 'laranja',
        'imagem': 'laranja.jpg',
        'valor': 2.22,
        'descricao': 'laranja vinda da rússia',
        'quantidade': 10,
    }
    lista.append(p3)

    return lista