# Exercícios Cap. 6 

# 6-9 Favorite Places
favorite_places = {
    'washington': ['shows rock', 'biblioteca', 'campo'],
    'bart': ['rua', 'fliperama', 'casa'],
    'chris': ['escola', 'disco', 'casa da tasha']
}

for name, places in favorite_places.items():
    print(f"Os lugares favoritos de {name.title()} são:")
    for place in places:
        print(f"\t- {place};")
