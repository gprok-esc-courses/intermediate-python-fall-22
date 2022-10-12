from Hangman import Hangman
from HangmanTk import HangmanTk


class GameTk:
    def __init__(self):
        self.hangman = Hangman()
        self.ui = HangmanTk(self.hangman)


if __name__ == '__main__':
    game = GameTk()
    game.ui.play_again()
    game.ui.mainloop()

