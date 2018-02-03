"""Teste de manipulação de arquivos."""
print('Digite as disciplinas que faltam para se formar: ')
print("(Digite 'sair' para encerrar.)")

while True:
    disciplina = input('Digite o nome da disciplina: ')
    if disciplina == 'sair':
        break
    else:
        print('A disciplina é ' + disciplina.title() + '.')
        with open('disciplinas.txt', 'a') as obj:
            obj.write(disciplina.title() + '\n')
