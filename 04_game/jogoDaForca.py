# Projeto Jogo Da Forca

#random escolhe aleatoriamente a palavra usada na forca
import random
from os import system, name;

#Funcao para limpar a tela a cada rodada
def cleanScreen():

    #windows
    if name == 'nt':
        _= system("cls")
    
    #mac ou linux
    else:
        _= system("clear");

def game():

    cleanScreen();
    print("\nBem-vindo ao Jogo da Forca :)");
    print("Adivinhe a palavra abaixo:\n");

    #Lista de palavras
    words = ['pitaya', 'groselha', 'abacate', 'morango', 'melao']

    #Escolhendo uma palavra
    word = random.choice(words);

    #List Compreension: loop dentro de uma lista
    letters = ['_' for letter in word];

    #numero de chances
    chance = 6;
    
    #Lista para letras erradas
    wrongLetters = [];

    #Enquanto o número de chances maior que zero
    while chance > 0:
        print(" ".join(letters));
        print("\nChances Restantes : ", chance);
        print("Letras Erradas:", " ".join(wrongLetters))

        tried = input("\nDigite uma letra: ").upper();

        if tried in word:
            index = 0
            for letter in word:
                if tried == letter:
                    letters[index] = letter;
                index +=1;

        else: 
            chance -= 1;
            wrongLetters.append(tried);

if __name__ == "__main__":
    game()
