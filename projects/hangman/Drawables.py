from abc import ABC, abstractmethod

from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter


class Drawable(ABC):
    @abstractmethod
    def draw(self, painter: QPainter):
        pass


class Head(Drawable):
    def draw(self, painter: QPainter):
        painter.drawEllipse(QPoint(40, 40), 20, 20)


class Body(Drawable):
    def draw(self, painter: QPainter):
        painter.drawLine(40, 60, 40, 100)


class LeftFoot(Drawable):
    def draw(self, painter: QPainter):
        painter.drawLine(40, 100, 20, 120)


class RightFoot(Drawable):
    def draw(self, painter: QPainter):
        painter.drawLine(40, 100, 60, 120)


class LeftHand(Drawable):
    def draw(self, painter: QPainter):
        painter.drawLine(40, 80, 20, 60)


class RightHand(Drawable):
    def draw(self, painter: QPainter):
        painter.drawLine(40, 80, 60, 60)