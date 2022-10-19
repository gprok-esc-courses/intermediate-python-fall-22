from PyQt5.QtGui import QPixmap, QPainter, QBrush
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt

from Drawables import Head, Body, LeftFoot, RightFoot, LeftHand, RightHand


class DrawingArea(QLabel):
    def __init__(self):
        super(DrawingArea, self).__init__()
        self.canvas = QPixmap(150, 150)
        self.body_parts = []
        self.body_parts.append(Head())
        self.body_parts.append(Body())
        self.body_parts.append(LeftFoot())
        self.body_parts.append(RightFoot())
        self.body_parts.append(LeftHand())
        self.body_parts.append(RightHand())
        self.setPixmap(self.canvas)
        self.draw(0)

    def draw(self, errors):
        self.canvas = QPixmap(150, 150)
        self.setPixmap(self.canvas)
        painter = QPainter(self.pixmap())

        painter.setBrush(QBrush(Qt.white))
        painter.fillRect(0, 0, 150, 150, painter.brush())
        painter.setBrush(QBrush(Qt.black))
        for p in range(errors):
            self.body_parts[p].draw(painter)





