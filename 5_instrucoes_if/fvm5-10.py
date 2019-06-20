##---------------------
# Faça você mesmo cap.5
# 5.9 - Sem usuários
##---------------------

current_users = ['admin', 'Jimmi', 'Leia', 'Sol', 'Winston', 'Bowser']
new_users = ['admin', 'jimmi', 'leia', 'sol', 
             'winston', 'bowser', 'bart', 'lisa',
            'eric cartman', 'kenny', 'kyle', 'stan']

current_user_lower = [user.lower() for user in current_users]

if current_users:
    for new_user in new_users:
        if new_user.lower() in current_user_lower:
            print('O usuário ' + new_user + ' já existe. Por favor, forneça outro nome.')
        else:
            print('O nome de usuário ' + new_user + ' está disponível!')
else:
    print('Precisamos encontrar alguns usuários!')