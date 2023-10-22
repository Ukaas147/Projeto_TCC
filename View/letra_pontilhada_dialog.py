import cv2, sys, os
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from RedeNeural.RetornaClasse import RetornaClasse
from brush_thickness_dialog import BrushThicknessDialog

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
