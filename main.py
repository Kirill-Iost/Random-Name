import sys
import random

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class Painter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 710, 600)
        self.setWindowTitle('Рисование')
        self.btn = QPushButton('Рисовать', self)
        self.btn.resize(681, 31)
        self.btn.move(10, 520)
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_circle(self, qp):
        for _ in range(random.randint(15, 30)):
            r, g ,b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
            qp.setBrush(QColor(r, g ,b))
            x, y, r = random.randint(0, 710), random.randint(0, 400), random.randint(10, 50)
            qp.drawEllipse(x, y, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Painter()
    ex.show()
    sys.exit(app.exec_())
