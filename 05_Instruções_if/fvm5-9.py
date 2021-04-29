##---------------------
# Faça você mesmo cap.5
# 5.9 - Sem usuários
##---------------------

users = []

if users:
    for user in users:
        if user == 'admin':
            print('Olá ' + user + '! Gostaria de ver um relatório de status?')
        else:
            print('Olá, ' + user.title() + '!')

else:
    print('Precisamos encontrar alguns usuários!')