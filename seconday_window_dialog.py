import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDialog

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        #self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle('Botão para Abrir Janela')

        button = QPushButton('Abrir Janela', self)
        button.clicked.connect(self.openDialog)

    def openDialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle('Janela Pequena')
        dialog.setGeometry(200, 200, 300, 100)

        button_in_dialog = QPushButton('Botão na Janela Pequena', dialog)
        button_in_dialog.setGeometry(10, 10, 200, 30)

        dialog.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

