# Jogo da forca parte 2 

# Função para limpar a tela a cada execução
import random
from os import system, name

def limpar_tela():
    # Windows
    if name == 'nt':
        _ = system('cls')
    # Mac ou Linux
    else:
        _ = system('clear')

# Hangman stages
hangman_stages = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """
]

class Hangman:
    # Construtor
    def __init__(self, palavra):
        self.palavra = palavra
        self.letrasErradas = []
        self.letrasEscolhidas = []
    
    # Verificando letras escolhidas
    def advinharLetra(self, letra):
        if letra in self.palavra and letra not in self.letrasEscolhidas:
            self.letrasEscolhidas.append(letra)
        elif letra not in self.palavra and letra not in self.letrasErradas:
            self.letrasErradas.append(letra)
        else: 
            return False
        return True

    # Verifica se o jogo terminou
    def hangmanOver(self):
        return self.hangmanWon() or (len(self.letrasErradas) == 6)

    # Verifica se o jogador venceu
    def hangmanWon(self):
        return '_' not in self.hidePalavra()
    
    # Ocultar letras não adivinhadas
    def hidePalavra(self):
        rtn = ''
        for letra in self.palavra:
            if letra not in self.letrasEscolhidas:
                rtn += '_'
            else:
                rtn += letra
        return rtn
    
    # Imprime o status do jogo
    def printGameStatus(self):
        print(hangman_stages[len(self.letrasErradas)])
        print('\nPalavra:', self.hidePalavra())
        print('\nLetras erradas:', ' '.join(self.letrasErradas))
        print('Letras corretas:', ' '.join(self.letrasEscolhidas))
        print()

# Selecionar uma palavra aleatória
def randPalavra():
    palavras = ['professor', 'lousa', 'caderno', 'lapis', 'caneta', 'regua', 'giz']
    return random.choice(palavras)

def main():
    limpar_tela()

    # Cria o objeto e seleciona uma palavra aleatoriamente
    game = Hangman(randPalavra())

    # Enquanto o jogo não terminar:
    while not game.hangmanOver():
        game.printGameStatus()
        user_input = input('\nDigite uma letra: ').lower()
        game.advinharLetra(user_input)

    # Verifica o resultado do jogo
    game.printGameStatus()
    if game.hangmanWon():
        print('\nParabéns! Você venceu o jogo!')
    else:
        print('\nGame Over! Você perdeu.')
        print('A palavra era:', game.palavra)

# Executa o programa
if __name__ == "__main__":
    main()
