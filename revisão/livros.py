# Livros
# 09 de junho de 2021

# Modificando com o método items:
books = {
    'evolução': ['stearns', 'hoekstra'],
    'biologia molecular da célula': ['alberts', 'johnson', 'lewis', 'raff', 'roberts', 'walter'],
    'a vida dos vertebrados': ['pough', 'janis', 'heiser'],
    'bioquímica': ['voet', 'voet'],
    'genérica molecular humana': ['strachan', 'read'],
    'princípios de bioquímica de lehninger': ['nelson', 'cox']
}

for livro, autores in books.items():
    print(f'\nO livro {livro.title()} possui os seguintes autores:')
    for autor in autores:
        print(f'\t- {autor.title()}')
