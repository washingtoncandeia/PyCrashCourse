## Cap.5 - pt.1
## Retirado do jupyter notebook

cars = ['audi', 'bmw', 'subaru', 'toyota']

print(cars)

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

print('\tFILMES:')
filmes = [
    'o segredo de seus olhos', 'onde os fracos não têm vez', 
    'hereditário', 'a bruxa', 'o paciente inglês', 
    'o exorcista', 'curtindo a vida adoidado', 
    'de volta para o futuro'
]

terror = [
    'hereditário', 'a bruxa', 'o exorcista'
]

for cine in filmes:
    if cine in terror:
        print(f'--> O filme "{cine.title()}" é um filme de terror.\n')
    else:
        print(f'O filme "{cine.title()}" pode ser assistido por qualquer um.\n')
        
# False
nome = 'lua'
if nome == 'sol':
    print(nome.title())
    
# True
nome = 'lua'
if nome != 'sol':
    print(nome.title())
    
# números
answer = 9

if answer != 42:
    print('Esta não é a resposta correta. Tente novamente!')
    
# Checagens múltiplas
age_0 = 22
age_1 = 18

# teste
age_0 >= age_1 and age_1 >= 21

age_0 < age_1 and age_1 >= 21
age_0 >= age_1 and age_1 < 21

## Para melhorar a legibilidade:
(age_0 >= age_1) and (age_1 < 21)

# Um valor em uma lista
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f'{user.title()}, você pode postar respostas se quiser.')
    
usuarios = [
    'bart', 'lisa', 'hommer', 'margie', 'meggie',
    'eric', 'kyle', 'stan', 'kenny'
]

banidos = ['eric', 'kyle', 'stan', 'kenny']

for user in usuarios:
    if user in banidos:
        print(f'---X---O usuário {user.title()} está banido do fórum.---X---')
    else:
        print(f'O usuário {user.title()} pode postar no fórum.')   
    
car = 'subaru'

print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

# Testes condicionais
age = 19

if age >= 18:
    print('Você é velho o suficiente para votar.')

age = 37

if age <= 35:
    print('Você ainda é novo.')
    
else:
    print('Já tá um vovôzinho.')

# exemplo 2
age = 12

if age < 4:
    print('A entrada é gratuita.')
    
elif age < 18:
    print('A entrada custa R$25,00.')
    
elif age >= 60:
    print('A entrada é gratuita.')
    
else:
    print('A entrada custa R$45,00')

# exemplo 3
age = 70

if age < 4:
    print('A entrada é gratuita.')
    
elif age < 18:
    print('A entrada custa R$25,00.')
    
elif age >= 60:
    print('A entrada é gratuita.')
    
else:
    print('A entrada custa R$45,00')
    
print('\tIF, ELIF, ESLE CHAIN:')   

# Para facilitar, pode-se fazer um encadeamento mais conciso
age = 12

if age < 4:
    price = 0
    
elif age < 18:
    price = 25
    
elif age >= 60:
    price = 0
    
else:
    price = 45
    
print(f'A sua entrada custa R${price}.')
    
age = 60

if age < 4:
    price = 0
    
elif age < 18:
    price = 25
    
elif age >= 60:
    price = 0
    
else:
    price = 45
    
print(f'A sua entrada custa R${price}.')   
    
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
