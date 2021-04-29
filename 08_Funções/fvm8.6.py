##-----------------------------
# Pychrash Course
# Eric Matthes
# Cap. 8 - Funções
# Faça você mesmo, p.199-200
##-----------------------------
# 8.6 - Nomes de cidade
def city_country(city, country):
    """Exibe nomes de cidade e país."""
    print('\nMinha cidade é ' + city.title() + '.')
    print('Pertence ao ' + country.title() + '.')

city_country('natal', 'brasil')

# 8.7 - Álbum
def make_album(artist, album_name, faixas=''):
    """Devolve um dicionário com informações sobre um álbum."""
    album = {'artista': artist, 'título do álbum': album_name}

    if faixas:
        album['faixas'] = faixas

    return album



album = make_album('neil young', 'on the beach', faixas=9)
print(album)

# 8.8 - Álbuns de usuários
while True:
    print('\nForneça o nome de um artista e o título de um de seus álbums.')
    print("(Digite 'sair' para encerrar.)")

    nome = input('O nome do artista é: ')
    if nome == 'q':
        break
    album = input('O nome de um de seus álbums é: ')
    if album == 'q':
        break

    complete_album = make_album(nome, album)
    print(complete_album)