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

    #List Compreension
    letters = ['_' for letter in word];