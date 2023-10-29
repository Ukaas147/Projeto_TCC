from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class LetraPontilhadaDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Escolha uma letra")
        self.setFixedSize(250, 150)

        layout = QtWidgets.QGridLayout()
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        row, col = 0, 0

        for letter in letters:
            button = QtWidgets.QPushButton(letter, self)
            button.clicked.connect(self.accept)
            layout.addWidget(button, row, col)
            col += 1
            if col > 6:
                col = 0
                row += 1

        self.setLayout(layout)
        
    def mostrar_letra_pontilhada(self, letter):
        image_path = f"letras/{letter}.png"
        pixmap = QtGui.QPixmap(image_path)

        if not pixmap.isNull():
            label = QtWidgets.QLabel(self)
            label.setPixmap(pixmap)
            label.show()
