##---------------------
# Faça você mesmo cap.4
# p. 102
##---------------------

# 4.3
for num in range(1, 21):
    print(num)

# 4.4
num = list(range(1, 1_000_001))


print(num[999_998:])

#4.5 - Somando um milhão
soma = sum(num)
print(soma)

min(num)
max(num)

# 4.6 - Números ímpares
impares = range(1, 21, 2)

for num in impares:
    print(num)

# 4.7 - Três
# Froma 1 (longa)
tres = []
for num in range(1, 31):
    multiplo = num * 3
    tres.append(multiplo)

for n in tres:
    print(n)

# 4.7 - Três
# Forma 2 (list comprehension)
tres = [x*3 for x in range(1, 31)]

for num in tres:
    print(num)


# 4.8 - Cubos
# Forma 1 (longa)
cubos = []

for num in range(1, 11):
    value = num ** 3
    cubos.append(value)
    
for n in cubos:
    print(n)


# 4.9 - Cubos
# Forma 2 (list comprehension)
cubos = [x**3 for x in range(1, 11)]

for n in cubos:
    print(n)
