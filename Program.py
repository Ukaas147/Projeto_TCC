import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QWidget
from PyQt5.QtGui import QImage, QPixmap, QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPoint

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Desenho em QLabel")
        self.setGeometry(100, 100, 640, 480)

        # Crie uma QImage e inicialize com um fundo branco
        self.image = QImage(400, 400, QImage.Format_RGB32)
        self.image.fill(QColor("#ffffff"))
        pixmap = QPixmap.fromImage(self.image)

        self.label = QLabel(self)
        self.label.setPixmap(pixmap)
        self.label.setGeometry(100, 100, 400, 400)  # Defina a posição e tamanho da QLabel

        self.drawing = False
        self.last_point = QPoint()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.last_point = self.label.mapFromGlobal(event.globalPos())

    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.LeftButton) & self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brush_color, self.brush_size, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = False

def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
