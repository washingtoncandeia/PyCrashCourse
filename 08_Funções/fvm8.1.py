##-----------------------------
# Pychrash Course
# Eric Matthes
# Cap. 8 - Funções
# Faça você mesmo, p.188
##-----------------------------

#8.1 - Mensagem
def display_message():
    """Mostra uma mensagem informando o que estou aprendendo."""
    print("Olá, todos! Estou aprendendo a fazer funções em python.")

display_message()

# 8.2 - Livro favorito
def favorite_book(title):
    """Mostra que livro é um dos meus favoritos."""
    print("Um de meus livros favoritos é " + title.title() + ".")

favorite_book('o mundo assombrado por demonios')

