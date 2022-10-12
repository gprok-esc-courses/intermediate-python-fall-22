from tkinter import Tk, Label, Button, Text, END


class HangmanTk(Tk):
    def __init__(self, hangman):
        super(HangmanTk, self).__init__()
        self.hangman = hangman
        self.geometry("400x400")
        self.secret_label = Label(self, text="")
        self.secret_label.grid(column=0, row=0)
        self.play_again_btn = Button(self, text="Play Again", command=self.play_again)
        self.play_again_btn.grid(column=0, row=2)
        self.user_input = Text(self, width=5, height=1)
        self.user_input.grid(column=0, row=1)
        self.check_btn = Button(self, text="Check", command=self.check)
        self.check_btn.grid(column=1, row=1)

    def play_again(self):
        self.hangman.start()
        print(self.hangman.get_secret())
        self.secret_label.config(text=self.hangman.get_secret())

    def check(self):
        letter = self.user_input.get("1.0", END)
        print(letter)
        self.hangman.play(letter[0])
        self.user_input.delete("1.0", END)
        self.secret_label.config(text=self.hangman.get_secret())


