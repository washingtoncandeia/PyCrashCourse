class Texto():
    """Classe que simula manipulações em arquivos de texto."""

    def __init__(self, filename):
        """Utiliza arquivo de texto."""
        self.filename = filename

    def escreve_texto(self):
        """Escreverá um texto e armazenará num arquivo."""
        nome_arquivo = self.filename

        while True:
            print("\n(Digite 'sair' para encerrar.)")
            texto = input("Digite seu texto: \n")
            if texto == 'sair':
                break
            else:
                with open(nome_arquivo, 'a') as obj:
                    obj.write(texto + "\n")

    def le_texto(self):
        """Lê o texto que foi escrito."""
        nome_arquivo = self.filename
        try:
            with open(nome_arquivo) as obj:
                contents = obj.read()

        except FileNotFoundError:
            print("O arquivo '" + nome_arquivo + "' não existe ou não está nesse diretório.")

        else:
            print(contents)

    def conta_palavras(self):
        """Conta o número de palavras - aproximado - em um texto."""
        nome_arquivo = self.filename

        try:
            with open(nome_arquivo) as obj:
                linhas = obj.read()

        except FileNotFoundError:
            print("O arquivo '" + nome_arquivo + "' não existe ou não está nesse diretório.")

        else:
            palavras = linhas.split()
            num_palavras = len(palavras)
            # Saída para texto:
            print("No arquivo '" + nome_arquivo + "' há, aproximadamente, "
                  + str(num_palavras) + " palavras.")
                  
                  
    def dict_to_text(dictionary, filename='dict_to_text.txt'):
    """Usa informações de um dicinário para escrever textos."""
    for keys, values in dictionary.items():
        try:
            with open(filename, 'a') as obj:
                obj.write('As linguagens favoritas de ' + keys.title() + ' são: \n')
                for l in values:
                    obj.write('- ' + l.title() + '\n')
        except FileNotFoundError:
            print("\nDesculpe, o arquivo '" + filename + "' não existe ou não está neste diretório.")
            
            
