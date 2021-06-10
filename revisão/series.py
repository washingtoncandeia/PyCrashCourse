# Séries animadas
# 09 de junho de 2021
# Modificando com o método items
animated  = {
    'os simpsons': ['bart', 'lisa', 'maggie', 'margie', 'homer'],
    'south park': ['cartman', 'stan', 'kenny', 'kyle'],
    'scooby-doo': ['scooby', 'salsicha', 'velma', 'fred', 'daphne'],
    'thundercats': ['lion', 'cheetara', 'panthro', 'tygra', 'wilyKit', 'wilyKat', 'snarf'],
    'caverna do dragão': ['hank', 'eric', 'diana', 'sheila', 'presto', 'bobby', 'uni', 'vingador','mestre dos magos']
}

for serie, names in animated.items():
    print(f'\nA série {serie.title()} possui os seguintes personagens:')
    for name in names:
        print(f'\t- {name.title()}')
