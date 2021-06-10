# dicionario
# 09 de junho de 2021

filmes = {
    'hereditário': 'terror', 'os goonies': 'aventura',
    'annabelle': 'terror', 'onde os fracos não têm vez': 'suspense',
    'whiplash': 'drama', 'shrek': 'animação', 
    'a bruxa': 'terror', 'seven': 'suspense'
}

lista_generos = ['terror', 'suspense']

print('\t\tInformações de filmes:')
for kine, gen in filmes.items():
    print(f'\nO filme {kine.title()} é um filme do gênero {gen.title()}.')
    if gen in lista_generos:
        print(f'===> O filme {kine.title()} vai te deixar preso na tela!')
