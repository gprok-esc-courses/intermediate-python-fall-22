import requests
import json


class Hangman:
    def __init__(self):
        self.word = ''
        self.wrong = ''
        self.correct = ''

    def start(self):
        # get a random word
        response = requests.get('https://random-word-api.herokuapp.com/word')
        data = json.loads(response.text)
        print(data[0])
        self.word = data[0]
        # initialize wrong and correct lists
        self.wrong = ''
        self.correct = ''

    def get_secret(self):
        secret = self.word[0]
        for p in range(1, len(self.word)-1):
            if self.word[p] in self.correct:
                secret += self.word[p]
            else:
                secret += '_'
        secret += self.word[-1]
        return secret

    def win(self):
        # return True if word is found or False otherwise
        pass

    def lost(self):
        # return True if wrong letters are 6, False otherwise
        pass

    def play(self, letter):
        # if letter is in the word put it in correct, else put it in wrong
        if letter in self.word:
            if letter not in self.correct:
                self.correct += letter
        else:
            if letter not in self.wrong:
                self.wrong += letter


if __name__ == '__main__':
    hangman = Hangman()
    hangman.start()

    while True:
        print(hangman.get_secret())
        letter = input("Guess: ")
        hangman.play(letter)
        if hangman.win():
            print("You Won!")
            break
        if hangman.lost():
            print("You lost :(")
            break
