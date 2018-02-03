from random import randint

secret = randint(1, 15)
guess = 0

while guess != secret:
    g = input('Adivinhe o número: ')
    guess = int(g)

    if guess == secret:
        print('\nAcertou!')
    else:
        if guess > secret:
            print('Muito alto!')
        else:
            print('Muito baixo!')

print('\n\nGame Over!')