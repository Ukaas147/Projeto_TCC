import sys
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPixmap, QImage, QPainter, QPen
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog, QLabel, QVBoxLayout, QWidget

class PaintApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Paint App')

        self.canvas = Canvas(self)
        self.setCentralWidget(self.canvas)

        main_menu = self.menuBar()
        file_menu = main_menu.addMenu('File')

        self.create_action(file_menu, 'Open Image', self.canvas.open_image)
        self.create_action(file_menu, 'Clear', self.canvas.clear)

    def create_action(self, menu, name, func):
        action = QAction(name, self)
        action.triggered.connect(func)
        menu.addAction(action)

class Canvas(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.image = QPixmap(self.size())
        self.image.fill(Qt.white)
        self.last_point = None

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.image)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.last_point = event.pos()

    def mouseMoveEvent(self, event):
        if self.last_point:
            painter = QPainter(self.image)
            pen = QPen(Qt.black, 2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
            painter.setPen(pen)
            painter.drawLine(self.last_point, event.pos())
            self.last_point = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.last_point = None

    def open_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open Image', '', 'Images (*.png *.jpg *.jpeg *.gif *.bmp);;All Files (*)')
        if file_name:
            self.image = QPixmap(file_name)
            self.update()

    def clear(self):
        self.image.fill(Qt.white)
        self.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PaintApp()
    window.show()
    sys.exit(app.exec_())
