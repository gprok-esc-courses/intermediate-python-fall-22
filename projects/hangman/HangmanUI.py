from PyQt5 import QtWidgets


class HangmanUI(QtWidgets.QMainWindow):
    def __init__(self, hangman):
        super(HangmanUI, self).__init__()
        self.hangman = hangman
        self.setGeometry(400, 400, 400, 400)
        self.secret_label = QtWidgets.QLabel("Label")
        self.user_input = QtWidgets.QLineEdit()
        self.user_input.textChanged.connect(self.check_user_input)
        self.wrong_letters = QtWidgets.QLabel("Wrong: ")
        self.correct_letters = QtWidgets.QLabel("Correct: ")
        self.play_again_btn = QtWidgets.QPushButton("Play Again")
        self.play_again_btn.clicked.connect(self.play_again)
        self.exit_btn = QtWidgets.QPushButton("EXIT")
        panel = QtWidgets.QFrame()
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.secret_label)
        vbox.addWidget(self.user_input)
        vbox.addWidget(self.wrong_letters)
        vbox.addWidget(self.correct_letters)
        vbox.addWidget(self.play_again_btn)
        vbox.addWidget(self.exit_btn)
        panel.setLayout(vbox)
        self.setCentralWidget(panel)

    def display_secret(self, secret):
        self.secret_label.setText(secret)

    def play_again(self):
        self.hangman.start()
        self.secret_label.setText(self.hangman.get_secret())

    def check_user_input(self):
        print(self.user_input.text())
        self.hangman.play(self.user_input.text())
        self.user_input.setText('')
        self.correct_letters.setText("Correct: " + self.hangman.correct)
        self.wrong_letters.setText("Wrong: " + self.hangman.wrong)
        self.secret_label.setText(self.hangman.get_secret())


