produtos = {
    'Notebook': 3500,
    'Mouse': 50,
    'Teclado': 120,
    'Monitor': 1000,
    'Mousepad': 30
}

for produto, preco in produtos.items():
    if preco > 100:
        print(f'{produto}: R$ {preco}')
