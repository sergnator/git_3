import random
import sys
import traceback

from PyQt5 import uic
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.change)
        self.draw_ = False

    def change(self):
        self.draw_ = True

    def draw(self, qp: QPainter):
        x, y = random.randint(0, 1000), random.randint(0, 1000)
        center = QPoint(x, y)
        r = random.randint(1, 100)
        QPainter.setBrush(QColor(255, 255, 0))
        QPainter.drawEllipse(center, r)

    def paintEvent(self, event):
        if self.draw_:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()
        self.draw_ = False



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
