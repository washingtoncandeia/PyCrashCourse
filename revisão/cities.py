# Exercícios Cap. 6 

# 6-11. Cities
cities = {
    'teerã': {'country': 'irã', 'population': 8_429_807, 'fact': 'persa como língua oficial' },
    'joão pessoa': {'country': 'brasil', 'population': 817_511, 'fact': 'foi fundada em 1.585'},
    'seattle': {'country': 'E.U.A.', 'population': 608_660, 'fact': 'início do grunge' },
}

for city, info in cities.items():
    print(f"\n{city.title()} localiza-se no {info['country'].title()} e possui {info['population']} habitantes.")
    print(f"* Um fato interessante sobre {city.title()} é: {info['fact']}.")
