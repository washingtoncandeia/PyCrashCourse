##-----------------------------
# Pychrash Course
# Eric Matthes
# Cap. 8 - Funções
# Faça você mesmo, p.211
##-----------------------------

# 8.12 - Sanduíches
def make_sandwich(*ingredientes):
    """Mostra os ingredientes no sanduíche pedido."""
    print('\nO sanduíche possui os seguintes ingredientes:')
    for ing in ingredientes:
        print('-> ' + ing)

# uso
make_sandwich('molho', 'tomate seco', 'hamburguer', 'ovo', 'bacon', 'picles')

# 8.13 - Perfil do usuário:
def build_profile(nome, sobrenome, **info_adicionais):
    """
    A função devolve um dicionário com informações sobre um usuário.
    :param nome: Primeiro Nome
    :param sobrenome: Sobrenome
    :param info_adicionais: Quaisquer informações adicionais, em formato 'chave + valor'
    :return: Dicionário com informações do usuário
    """
    profile = {}
    profile['Primmeiro Nome'] = nome
    profile['Sobrenone'] = sobrenome

    for chave, valor in info_adicionais.items():
        profile[chave] = valor

    return profile

leia = build_profile('Leia', 'Organa',
                     Ocupação = 'Rebelde',
                     Pai = 'Anakin Skywalker',
                     Mãe = 'Senadora Amidala')

print('\nInformações sobre leia: ')
print(leia)

#8.14 - Carros
def make_car(fabricante, modelo, **info_opcional):
    """
    Devolve informações sobre um carro.
    :param fabricante: Nome do Fabricante
    :param modelo: Modelo do Carro
    :param info_opcional: Itens Opcionais
    :return: Informações sobre o carro, na forma de um dicinário.
    """
    carro = {}
    carro['Fabricante'] = fabricante
    carro['Modelo'] = modelo

    for chave, valor in info_opcional.items():
        carro[chave] = valor

    return carro
# Uso
carro = make_car('Ford', 'FordGT',
                 Constituição = 'Fibra de carbono',
                 Rodas = 'Alumínio',
                 Motor = '600HP')
print('\nInformações sobre o carro:')
print(carro)
help(make_car)