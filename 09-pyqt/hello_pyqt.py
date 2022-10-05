import sys

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QPen
from PyQt5.QtCore import Qt


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(400, 300)
        self.label.setPixmap(canvas)

        self.setCentralWidget(self.label)
        self.draw_canvas()

    def draw_canvas(self):
        painter = QtGui.QPainter(self.label.pixmap())
        painter.drawLine(15, 15, 100, 100)
        painter.setPen(QPen(Qt.green, 3, Qt.DashLine))
        painter.drawEllipse(90, 100, 60, 70)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec()
