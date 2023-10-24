import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QImage, QPainter, QPen, QColor
from PyQt5.QtCore import Qt, QPoint

class DrawingLabel(QLabel):
    def __init__(self):
        super().__init__()

        self.setFixedSize(400, 200)  # Tamanho da área de desenho
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)
        self.last_point = QPoint()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(0, 0, self.image)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.last_point = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            painter = QPainter(self.image)
            painter.setPen(QPen(QColor(0, 0, 0), 2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawLine(self.last_point, event.pos())
            self.last_point = event.pos()
            self.update()

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.setStyleSheet(u"background-color:#ffffdf")

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        drawing_label = DrawingLabel()
        layout.addWidget(drawing_label)
        central_widget.setLayout(layout)

        self.setGeometry(100, 100, 200, 400)
        self.setWindowTitle('Área de Desenho')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainApp()
    sys.exit(app.exec_())
