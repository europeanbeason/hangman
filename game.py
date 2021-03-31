import random

def convert(arr):
    #Zmiana tablicy charów na stringa
    new = ""
    for x in arr:
        new += x
    return new

def words_table():
    #Pobieranie słów z pliku
    with open('words.txt','r') as file:
        words = []
        for word in file.readlines():
            words.append(word.strip())
    return words


def guess_words():
    #Losowanie słowa z puli
    words = words_table()
    num = int(random.random()*len(words))
    guess_words = words[num]
    return guess_words

class Game():
    #Tworzenie klasy odpowiedzialnej za grę
    def __init__(self):
        #Inicjacja podstawowych zmiennych
        self.hangman = [" ","===",
               """
                 |
                 |
                 |
                ===
               """,
               """
             +---+
                 |
                 |
                 |
                ===
               """,
               """
               +---+
               O   |
              /|   |
                   |
                  ===
               """,
               """
               +---+
               O   |
              /|\  |
                   |
                  ===
               """,
               """
               +---+
               O   |
              /|\  |
              /    |
                  ===
               """,
               """
               +---+
               O   |
              /|\  |
              / \  |
                  ===
               """]
        self.word = guess_words()
        self.lives = 8
        self.state = []
        self.guess = []
        for i in range(len(self.word)):
            self.guess += " "
        for i in range(len(self.word)):
            self.state.append("|_|")
        
    def play(self):
        #Funkcja odpowiadająca za gre
        while self.lives != 0 or convert(self.guess) == self.word:
            print(self.hangman[8-self.lives])
            print(self.state)
            char = input("Podaj literę: ")
            if char in self.word:
                print("Zgadłes literę")
                self.state[self.word.index(char)] = char
                self.guess[self.word.index(char)] = char
            else:
                print("Zła litera!")
                self.lives -= 1
        if self.lives == 0:
            print("Przegrałes")
        else: 
            print("Wygrałes") 
       
game = Game()
game.play()
