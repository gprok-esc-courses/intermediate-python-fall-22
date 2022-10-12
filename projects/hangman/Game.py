import sys

from PyQt5 import QtWidgets

from Hangman import Hangman
from HangmanUI import HangmanUI


class Game:
    def __init__(self):
        self.hangman = Hangman()
        self.ui = HangmanUI(self.hangman)
        self.ui.play_again()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    game = Game()
    game.ui.show()
    app.exec()
