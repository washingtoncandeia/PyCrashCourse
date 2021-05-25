## 
# 5-3 Alien colors
alien_color = 'green'

if alien_color == 'green':
    print('Você ganhou 5 pontso!')   

# exemplo
alien_color = 'green'

if alien_color == 'green':
    pontos = 5
elif alien_color == 'yellow':
    pontos = 10
else:
    pontos = 15
    
print(f'Você ganhou {pontos} pontos!') 

# 5-6 
age = 38

if age < 2:
    person = 'baby'
elif age <= 4:
    person = 'toddler'
elif (age > 4) and (age < 13):
    person = 'kid'
elif (age >= 13) and (age < 20):
    person = 'teenager'
elif (age >= 20 ) and (age < 65):
    person = 'adult'
else:
    person = 'elder'
    
print(f'This person is a {person}.')
    
print('Usando statements com listas: ')

itens_pedidos = ['calabresa', 'pimentão', 'parmesão', 'presunto']

# loop do pedido
for item in itens_pedidos:
    print(f'O ingrediente {item} foi adicionado.')
    
# Faltando um ingrediente: presunto
for item in itens_pedidos:
    if item == 'parmesão':
        print(f'\t-x- Desculpe, o ingrediente {item} está em falta.-x-')
    else:
        print(f'O ingrediente {item} foi adicionado!')

print('\nA pizza foi feita!')

# Exemplo
itens_pedidos = ['calabresa', 'pimentão', 'parmesão', 'presunto']

if itens_pedidos:
    for item in itens_pedidos:
        print(f'O ingrediente {item} foi adicionado à pizza!')
    print('A pizza foi feita!')
else:
    print('Tem certeza que inseriu algum ingrediente?')
    
novas_bandas = [
    'edu falaschi', 'smoulder', 'possessed steel',
    'megaton sword', 'lunar shadow', 'glacier',
    'freeways', 'white magician', 'iron maiden'
]

print('Novas bandas: \n')
if novas_bandas:
    for new in novas_bandas:
        if new == 'iron maiden':
            print(f'===> {new.title()} não é uma banda nova.')
        else:
            print(f'{new.title()} é uma nova banda!')
    print('\nEssas foram as novas bandas.\n')
else:
    print('Tem certeza que há bandas novas?')
    
# Exemplo
novas_bandas = []

if novas_bandas:
    for new in novas_bandas:
        if new == 'iron maiden':
            print(f'===> {new.title()} não é uma banda nova.')
        else:
            print(f'{new.title()} é uma nova banda!')
        print('Essas foram as novas bandas.\n')
else:
     print('Tem certeza que há bandas novas?')
        
# observar lista vazia
simpsons = ['bart', 'lisa', 'hommer', 'margie', 'maggie',
           'stan', 'kyle', 'eric', 'kenny'
           ]
south_park = ['stan', 'kyle', 'eric', 'kenny']
if simpsons:
    for personagem in simpsons:
        if personagem in south_park:
            print(f'---*--- O persongaem {personagem.title()} não pertence aos Simpsons.---*---')
        else:
            print(f'{personagem.title()} é dos Simpsons.')
    print('\nTerminada a lista.')
else:
    print('A lista está vazia.')
    
aims = [
    'gramática', 'direito processual penal', 'genética',
    'arquivologia', 'rlm', 'química', 'história'
]

if aims:
    for a in aims:
        if a == 'história':
            print(f'---*---- A disciplina {a.title()} não faz parte da lista.---*---')
        else:
            print(f'É preciso estudar {a.title()} agora.')
    print('\nTarefa terminada.')
else:
    print('A lista de tarefas está vazia.')
    
# Exercicio
# 5-8 Hello Admin
users = [
    'admin', 'carl_sagan', 'mark_ridley',
    'liev_tolstoi', 'graciliano_ramos'
]

if users:
    for user in users:
        if user == 'admin':
            print(f'\o/\o/\o/ Bem vindo {user}! Você é o administrador.')
        else:
            print(f'O seu nome de usuário é: {user}.')
    print('\n\tFINALIZADA A LISTA DE USUÁRIOS!')
else:
    print('\nA lista de usuários está vazia.')
    