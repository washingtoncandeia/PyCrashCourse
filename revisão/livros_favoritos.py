# Dicionários
# 09 de junho de 2021

livros_favoritos ={
    'washington': ['vidas secas', 'o mundo assombrado por demônios', 'o relojoeiro cego'],
    'alien': ['o guia do mochileiro das galáxias'],
    'nelson': ['ictiologia', 'zoologia dos vertebrados'],
}

for name, books in livros_favoritos.items():
    print(f'\nOs livros favoritos de {name.title()} são:')
    for book in books:
        print(f'\t- {book.title()}')
