import cv2, sys, os
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from RedeNeural.RetornaClasse import RetornaClasse
from brush_thickness_dialog import BrushThicknessDialog
from letra_pontilhada_dialog import LetraPontilhadaDialog

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.minha_lista = []

        caminho_pasta_imagens = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'View', 'Imagens')
        self.setWindowTitle("Tela Digitalizadora")
        self.setFixedSize(1200, 660)
        self.setStyleSheet(u"background-color:#ffffdf")
        self.setWindowIcon(QIcon(os.path.join(caminho_pasta_imagens, 'icone.png')))
        
#CRIAÇÃO DA TELA
        self.tela_digitalizada = QTextBrowser(self)
        self.tela_digitalizada.setObjectName(u"tela_digitalizada")
        self.tela_digitalizada.setGeometry(QRect(100, 21, 1070, 330))
        self.tela_digitalizada.setAutoFillBackground(False)
        self.tela_digitalizada.setStyleSheet(u"background-color:#ffffff")

        self.lado_esquerdo_amarelo = QLabel(self)
        self.lado_esquerdo_amarelo.setObjectName(u"lado_esquerdo_amarelo")
        self.lado_esquerdo_amarelo.setGeometry(QRect(0, 21, 100, 639))
        self.lado_esquerdo_amarelo.setAutoFillBackground(False)
        self.lado_esquerdo_amarelo.setStyleSheet(u"background-color:#ffffdf")
        
        self.lado_direito_amarelo = QLabel(self)
        self.lado_direito_amarelo.setObjectName(u"lado_direito_amarelo")
        self.lado_direito_amarelo.setGeometry(QRect(1170, 21, 30, 639))
        self.lado_direito_amarelo.setAutoFillBackground(False)
        self.lado_direito_amarelo.setStyleSheet(u"background-color:#ffffdf")

        self.margem_cinza_esquerda = QLabel(self)
        self.margem_cinza_esquerda.setObjectName(u"margem_cinza_esquerda")
        self.margem_cinza_esquerda.setGeometry(QRect(70, 310, 240, 290))
        self.margem_cinza_esquerda.setAutoFillBackground(False)
        self.margem_cinza_esquerda.setStyleSheet(u"background-color:#ebebeb")

        self.margem_cinza_direita = QLabel(self)
        self.margem_cinza_direita.setObjectName(u"margem_cinza_direita")
        self.margem_cinza_direita.setGeometry(QRect(605, 310, 260, 290))
        self.margem_cinza_direita.setAutoFillBackground(False)
        self.margem_cinza_direita.setStyleSheet(u"background-color:#ebebeb")
        
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)

#BOTOES
        self.botao_salvar = QPushButton(self)
        self.botao_salvar.setGeometry(10, 30, 35, 35)
        self.botao_salvar.clicked.connect(self.save)
        self.botao_salvar.setIcon(QIcon(os.path.join(caminho_pasta_imagens, 'filesave.png')))
        self.botao_salvar.setIconSize(QSize(30, 30))
        self.botao_salvar.setStyleSheet(u"background-color:#ffffff")
        
        self.botao_digitalizar = QPushButton(self)
        self.botao_digitalizar.setGeometry(10, 75, 35, 35)
        self.botao_digitalizar.clicked.connect(self.digitalizar)
        self.botao_digitalizar.setIcon(QIcon(os.path.join(caminho_pasta_imagens, 'print.png')))
        self.botao_digitalizar.setIconSize(QSize(30, 30))
        self.botao_digitalizar.setStyleSheet(u"background-color:#ffffff")
        
        self.botao_limpar = QPushButton(self)
        self.botao_limpar.setGeometry(10, 120, 35, 35)
        self.botao_limpar.clicked.connect(self.clear)
        self.botao_limpar.setIcon(QIcon(os.path.join(caminho_pasta_imagens, 'limpar.png')))
        self.botao_limpar.setIconSize(QSize(30, 30))
        self.botao_limpar.setStyleSheet(u"background-color:#ffffff")

        self.botao_espessura = QPushButton(self)
        self.botao_espessura.setGeometry(10, 165, 35, 35)
        self.botao_espessura.clicked.connect(self.show_brush_size_dialog)
        self.botao_espessura.setIcon(QIcon(os.path.join(caminho_pasta_imagens, 'espessura.png')))
        self.botao_espessura.setIconSize(QSize(30, 30))
        self.botao_espessura.setStyleSheet(u"background-color:#ffffff")
        
        self.botao_escolher_cor = QPushButton(self)
        self.botao_escolher_cor.setGeometry(10, 210, 35, 35)
        self.botao_escolher_cor.clicked.connect(self.show_color_dialog)
        self.botao_escolher_cor.setIcon(QIcon(os.path.join(caminho_pasta_imagens, 'cor.png')))
        self.botao_escolher_cor.setIconSize(QSize(30, 30))
        self.botao_escolher_cor.setStyleSheet(u"background-color:#ffffff")
        
        self.botao_borracha = QPushButton(self)
        self.botao_borracha.setGeometry(10, 255, 35, 35)
        self.botao_borracha.clicked.connect(self.borracha)
        self.botao_borracha.setIcon(QIcon(os.path.join(caminho_pasta_imagens, 'borracha.png')))
        self.botao_borracha.setIconSize(QSize(30, 30))
        self.botao_borracha.setStyleSheet(u"background-color:#ffffff")

        self.botao_lapis = QPushButton(self)
        self.botao_lapis.setGeometry(10, 300, 35, 35)
        self.botao_lapis.clicked.connect(self.lapis)
        self.botao_lapis.setIcon(QIcon(os.path.join(caminho_pasta_imagens, 'lapis.png')))
        self.botao_lapis.setIconSize(QSize(30, 30))
        self.botao_lapis.setStyleSheet(u"background-color:#ffffff")

        self.botao_letra_pontilhada = QPushButton(self)
        self.botao_letra_pontilhada.setGeometry(10, 345, 35, 35)
        self.botao_letra_pontilhada.clicked.connect(self.mostrar_letra_pontilhada_dialog)
        self.botao_letra_pontilhada.setIcon(QIcon(os.path.join(caminho_pasta_imagens, 'pontilhado.png')))
        self.botao_letra_pontilhada.setIconSize(QSize(30, 30))
        self.botao_letra_pontilhada.setStyleSheet(u"background-color:#ffffff")
        
        self.label = QLabel(self)
        self.drawing = False
        self.brush_size = 10
        self.brush_color = QColor("#000000")
        self.lastPoint = QPoint()

        main_menu = self.menuBar()
        file_menu = main_menu.addMenu("Arquivo")

        acao_digitalizar = QAction("Print", self)
        acao_digitalizar.setShortcut("Ctrl+P")
        file_menu.addAction(acao_digitalizar)
        acao_digitalizar.triggered.connect(self.digitalizar)

        clear_action = QAction("Limpar", self)
        clear_action.setShortcut("Ctrl+C")
        file_menu.addAction(clear_action)
        clear_action.triggered.connect(self.clear)

        self.mouse_release_timer = QTimer(self)
        self.mouse_release_timer.setSingleShot(True)
        self.mouse_release_timer.timeout.connect(self.after_mouse_release)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()

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
            self.mouse_release_timer.start(2500)

    @pyqtSlot()
    def after_mouse_release(self):
        self.digitalizar()

    def paintEvent(self, event):
        canvasPainter = QPainter(self)
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())

    def save(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                          "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")
 
        if filePath == "":
            return
        self.image.save(filePath)

    def digitalizar(self):
        caminho_pasta_imagens = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'View', 'Imagens')
        caminho_screenshot = os.path.join(caminho_pasta_imagens, 'screenshot.png')

        screen = QApplication.primaryScreen()
        screenshot = screen.grabWindow(self.winId())
        screenshot.save(caminho_screenshot, 'png')
        imagem = cv2.imread(caminho_screenshot)
        imagem_cortada = imagem[311:600, 310:602]
        cv2.imwrite(caminho_screenshot, imagem_cortada)
        self.pixmap = QPixmap(caminho_screenshot)
        self.retornaTextoImagem()

        
    def clear(self):
        self.image.fill(Qt.white)
        self.update()

    def show_color_dialog(self):
        color = QColorDialog.getColor(initial=self.brush_color)
        
        if color.isValid():
            self.brush_color = color
            
    def borracha(self):
        self.brush_color = QColor("#FFFFFF")

    def lapis(self):
        self.brush_color = QColor("#000000")

    def show_brush_size_dialog(self):
        brush_size_dialog = BrushThicknessDialog()
        result = brush_size_dialog.exec_()

        if result == QDialog.Accepted:
            self.brush_size = brush_size_dialog.get_selected_thickness()

    def retornaTextoImagem(self):
        caminho_pasta_imagens = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'View', 'Imagens')
        caminho_screenshot = os.path.join(caminho_pasta_imagens, 'screenshot.png')

        retornaClasse = RetornaClasse()
        letraDigitalizada = retornaClasse.prever_letra(caminho_screenshot)
        self.minha_lista.append(letraDigitalizada)
        valores_sem_colchetes = ''.join(str(valor) for valor in self.minha_lista if valor is not None and valor != 'e')

        self.tela_digitalizada.setHtml(
            u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
            f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:65pt; font-family: Calibri\">{valores_sem_colchetes}</span></p></body></html>")

    def mostrar_letra_pontilhada_dialog(self, letter):
        letra_pontilhada_dialog = LetraPontilhadaDialog()
        result = letra_pontilhada_dialog.exec_()
        image_path = f"letras/{letter}.png"
        pixmap = QtGui.QPixmap(image_path)

        if not pixmap.isNull():
            self.tela_digitalizada.setPixmap(pixmap)
            self.tela_digitalizada.setGeometry(69, 0, pixmap.width(), pixmap.height())
            self.tela_digitalizada.setStyleSheet("background-color:#ffffff; border: 1px solid black")
            self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()