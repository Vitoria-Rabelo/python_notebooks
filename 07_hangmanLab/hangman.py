# Jogo da forca parte 2 

#funcao para limpar a tela a cada execução
import random
from os import system, name

def limpar_tela():
    #Windows
    if name == 'nt':
        _ =system ('cls')

    #Mac ou Linux
    else:
      _ = system('clear')

print("Hangman\n")

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
  #Construtor
  def __init__(self,palavra):
    self.palavra = palavra
    #listas
    self.letrasErradas = []
    self.letrasEscolhidas = []
  
  #verificando letras escolhidas
  def advinharLetra(self, letra):
    if letra in self.palavra and letra not in self.letrasEscolhidas:
      self.letrasEscolhidas.append(letra)
    elif letra not in self.palavra and letra not in self.letrasEscolhidas:
      self.letrasErradas.append(letra)
    else: 
      return False
    return True

#Verifica se o jogo terminou
  def hangmanOver(self):
    return self.hangmanWon() or (len(self.letrasErradas) == 6)

#Verifica se o jogador venceu
  def hangmanWon(self):
    if '_' not in self.hidePalavra():
      return True
    return False
  
def printGameStatus(self):
  print(board)
def randPalavra():
  palavras = ['professor', 'lousa', 'caderno', 'lapis', 'caneta', 'regua', 'giz']

  palavra = random.choice(palavras)
  return palavra 

def main():
  limpar_tela()

  #Cria o objeto e relaciona randomicamente
  game = Hangman(randPalavra())

  #Enquanto o jogo não terminar:
  while not game.hangmanOver():
    game.printGameStatus()
    user_input = input('\nDigite uma letra: ')
    game.guess(user_input)

  game.printGameStatus()
  if game.hangmanWon():
    print('Parabens voce venceu o jogo')
  else:
    print('Game Over!\n')
    print('Você perdeu')

#Executa o programa
if __name__== "__main__":
  main()