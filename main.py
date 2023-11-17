import random
import sys
import traceback


from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from Ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.change)
        self.draw_ = False
        self.setGeometry(100, 100, 1000, 1000)

    def change(self):
        self.draw_ = True
        self.update()

    def draw(self, qp: QPainter):
        x, y = random.randint(0, 1000), random.randint(0, 1000)

        center = QPoint(x, y)
        r = random.randint(1, 200)
        qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        qp.drawEllipse(center, r, r)

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
