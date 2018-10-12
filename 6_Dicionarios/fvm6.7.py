#!/bin/env python
# Faça voce mesmo, p.163

# Lista de pessoas
pessoas = []

# Pessoa 1
pessoa1 = {
    'nome': 'eric', 'sobrenome': 'cartman',
    'idade': 10, 'local': 'south park'
}

pessoas.append(pessoa1)

# Pessoa 2
pessoa2 = {
    'nome': 'obi-wan', 'sobrenome': 'kenobi',
    'idade': 57, 'local': 'república galáctica'
}

pessoas.append(pessoa2)
# Pessoa 3
pessoa3 = {
    'nome': 'jerry', 'sobrenome': 'seinfeld',
    'idade': 64, 'local': 'nova iorque'
}

pessoas.append(pessoa3)

for pessoa in pessoas:
    print('\nPessoa: ' + pessoa['nome'].title())
    nome = pessoa['nome'].title() + ' ' + pessoa['sobrenome'].title()
    idade = pessoa['idade']
    local = pessoa['local'].title()

    print('\n' + nome + ' tem ' + str(idade) + ' anos, mora em ' + local.title() + '.')