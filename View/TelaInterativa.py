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

        self.lista_letras_digitalizadas = []

        caminho_pasta_imagens = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'View', 'Imagens')
        self.setWindowTitle("Tela Digitalizadora")
        self.setFixedSize(1200, 660)
        self.setWindowIcon(QIcon(os.path.join(caminho_pasta_imagens, 'icone.png')))
        
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(QColor("#ffffff"))
        
        self.image_label = QLabel(self)
        self.image_label.setGeometry(463, 272, 349, 377)
        
#CRIAÇÃO DA TELA

        self.margem_amarelo_esquerdo = QLabel(self)
        self.margem_amarelo_esquerdo.setObjectName(u"argem_amarelo_esquerdo")
        self.margem_amarelo_esquerdo.setGeometry(QRect(0, 0, 101, 660))
        self.margem_amarelo_esquerdo.setStyleSheet(u"background-color:#ffffdf; border-right: 1px solid gray")
        
        self.margem_amarelo_direito = QLabel(self)
        self.margem_amarelo_direito.setObjectName(u"argem_amarelo_direito")
        self.margem_amarelo_direito.setGeometry(QRect(1189, 0, 11, 660))
        self.margem_amarelo_direito.setStyleSheet(u"background-color:#ffffdf; border-left: 1px solid gray")
        
        self.margem_amarelo_topo = QLabel(self)
        self.margem_amarelo_topo.setObjectName(u"argem_amarelo_topo")
        self.margem_amarelo_topo.setGeometry(QRect(100, 21, 1090, 11))
        self.margem_amarelo_topo.setStyleSheet(u"background-color:#ffffdf; border-bottom: 1px solid gray")
        
        self.margem_amarelo_meio = QLabel(self)
        self.margem_amarelo_meio.setObjectName(u"argem_amarelo_meio")
        self.margem_amarelo_meio.setGeometry(QRect(100, 261, 1090, 11))
        self.margem_amarelo_meio.setStyleSheet(u"background-color:#ffffdf; border-bottom: 1px solid gray")
        
        self.margem_amarelo_baixo = QLabel(self)
        self.margem_amarelo_baixo.setObjectName(u"argem_amarelo_")
        self.margem_amarelo_baixo.setGeometry(QRect(100, 649, 1090, 11))
        self.margem_amarelo_baixo.setStyleSheet(u"background-color:#ffffdf; border-top: 1px solid gray")

        self.tela_digitalizada = QTextBrowser(self)
        self.tela_digitalizada.setObjectName(u"tela_digitalizada")
        self.tela_digitalizada.setGeometry(QRect(100, 31, 1090, 230))
        self.tela_digitalizada.setAutoFillBackground(False)
        self.tela_digitalizada.setStyleSheet(u"background-color:#ffffff; border: 1px solid gray")
        
        self.margem_cinza_esquerda = QLabel(self)
        self.margem_cinza_esquerda.setObjectName(u"margem_cinza_esquerda")
        self.margem_cinza_esquerda.setGeometry(QRect(101, 272, 349, 377))
        self.margem_cinza_esquerda.setAutoFillBackground(False)
        self.margem_cinza_esquerda.setStyleSheet(u"background-color:#ebebeb")
        
        self.margem_cinza_direita = QLabel(self)
        self.margem_cinza_direita.setObjectName(u"margem_cinza_direita")
        self.margem_cinza_direita.setGeometry(QRect(840, 272, 349, 377))
        self.margem_cinza_direita.setAutoFillBackground(False)
        self.margem_cinza_direita.setStyleSheet(u"background-color:#ebebeb")

#BOTOES
        self.botao_salvar = QPushButton(self)
        self.botao_salvar.setGeometry(10, 30, 35, 35)
        self.botao_salvar.clicked.connect(self.salvar)
        self.botao_salvar.setIcon(QIcon(os.path.join(caminho_pasta_imagens, 'filesave.png')))
        self.botao_salvar.setIconSize(QSize(30, 30))
        self.botao_salvar.setStyleSheet(u"background-color:#ffffff")
        
        self.botao_abrir_documento = QPushButton(self)
        self.botao_abrir_documento.setGeometry(55, 30, 35, 35)
        self.botao_abrir_documento.clicked.connect(self.pop_lista_letras_digitalizadas)
        self.botao_abrir_documento.setIcon(QIcon(os.path.join(caminho_pasta_imagens, '')))
        self.botao_abrir_documento.setStyleSheet(u"background-color:#ffffff")
        
        self.botao_alterar_fonte_texto = QPushButton(self)
        self.botao_alterar_fonte_texto.setGeometry(55, 75, 35, 35)
        self.botao_alterar_fonte_texto.clicked.connect(self.open_image)
        self.botao_alterar_fonte_texto.setIcon(QIcon(os.path.join(caminho_pasta_imagens, '')))
        self.botao_alterar_fonte_texto.setStyleSheet(u"background-color:#ffffff")
        
        self.botao_alterar_cor_texto = QPushButton(self)
        self.botao_alterar_cor_texto.setGeometry(55, 120, 35, 35)
        self.botao_alterar_cor_texto.setStyleSheet(u"background-color:#ffffff")
        
        self.botao_alterar_tamanho_texto = QPushButton(self)
        self.botao_alterar_tamanho_texto.setGeometry(55, 165, 35, 35)
        self.botao_alterar_tamanho_texto.setStyleSheet(u"background-color:#ffffff")
        
        self.botao_digitalizar = QPushButton(self)
        self.botao_digitalizar.setGeometry(10, 75, 35, 35)
        self.botao_digitalizar.clicked.connect(self.digitalizar)
        self.botao_digitalizar.setIcon(QIcon(os.path.join(caminho_pasta_imagens, 'print.png')))
        self.botao_digitalizar.setIconSize(QSize(30, 30))
        self.botao_digitalizar.setStyleSheet(u"background-color:#ffffff")
        
        self.botao_limpar = QPushButton(self)
        self.botao_limpar.setGeometry(10, 120, 35, 35)
        self.botao_limpar.clicked.connect(self.limpar_tela)
        self.botao_limpar.setIcon(QIcon(os.path.join(caminho_pasta_imagens, 'limpar.png')))
        self.botao_limpar.setIconSize(QSize(30, 30))
        self.botao_limpar.setStyleSheet(u"background-color:#ffffff")

        self.botao_espessura = QPushButton(self)
        self.botao_espessura.setGeometry(10, 165, 35, 35)
        self.botao_espessura.clicked.connect(self.mostrar_espessura_lapis_dialog)
        self.botao_espessura.setIcon(QIcon(os.path.join(caminho_pasta_imagens, 'espessura.png')))
        self.botao_espessura.setIconSize(QSize(30, 30))
        self.botao_espessura.setStyleSheet(u"background-color:#ffffff")
        
        self.botao_escolher_cor = QPushButton(self)
        self.botao_escolher_cor.setGeometry(10, 210, 35, 35)
        self.botao_escolher_cor.clicked.connect(self.mostrar_cor_color_dialog)
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

        digitalizar_qaction = QAction("Print", self)
        digitalizar_qaction.setShortcut("Ctrl+P")
        file_menu.addAction(digitalizar_qaction)
        digitalizar_qaction.triggered.connect(self.digitalizar)

        limpar_tela_qaction = QAction("Limpar", self)
        limpar_tela_qaction.setShortcut("Ctrl+C")
        file_menu.addAction(limpar_tela_qaction)
        limpar_tela_qaction.triggered.connect(self.limpar_tela)

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

    def salvar(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                          "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")
 
        if filePath == "":
            return self.image.save(filePath)
           
    def limpar_tela(self):
        self.image.fill(Qt.white)
        self.update()
        
    def open_image(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, 'Abrir Imagem', '', 'Imagens (*.png *.jpg *.jpeg *.gif *.bmp);;Todos os Arquivos (*)', options=options)
        if file_name:
            pixmap = QPixmap(file_name)
            if not pixmap.isNull():
                # Defina a imagem selecionada como pixmap do QLabel
                self.image_label.setPixmap(pixmap)
                self.image_label.setScaledContents(True)
                print(f'Imagem selecionada: {file_name}')

    def mostrar_cor_color_dialog(self):
        color = QColorDialog.getColor(initial=self.brush_color)
        
        if color.isValid():
            self.brush_color = color
            
    def borracha(self):
        self.brush_color = QColor("#FFFFFF")

    def lapis(self):
        self.brush_color = QColor("#000000")

    def mostrar_espessura_lapis_dialog(self):
        brush_size_dialog = BrushThicknessDialog()
        result = brush_size_dialog.exec_()

        if result == QDialog.Accepted:
            self.brush_size = brush_size_dialog.get_selected_thickness()

    def digitalizar(self):
        caminho_pasta_imagens = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'View', 'Imagens')
        caminho_screenshot = os.path.join(caminho_pasta_imagens, 'screenshot.png')

        screen = QApplication.primaryScreen()
        screenshot = screen.grabWindow(self.winId())
        screenshot.save(caminho_screenshot, 'png')
        
        imagem = cv2.imread(caminho_screenshot)
        cortar_screenshot = imagem[272:649,450:840]
        cv2.imwrite(caminho_screenshot, cortar_screenshot)
        self.pixmap = QPixmap(caminho_screenshot)
        self.retorna_texto_imagem()

    def retorna_texto_imagem(self):
        caminho_pasta_imagens = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'View', 'Imagens')
        caminho_screenshot = os.path.join(caminho_pasta_imagens, 'screenshot.png')
        retornaClasse = RetornaClasse()
        letraDigitalizada = retornaClasse.prever_letra(caminho_screenshot)
        self.append_lista_letras_digitalizadas(letraDigitalizada)
    
    def append_lista_letras_digitalizadas(self, letraDigitalizada):
        self.lista_letras_digitalizadas.append(letraDigitalizada)
        self.atualizar_info_tela_digitalizada()
        
    def pop_lista_letras_digitalizadas(self):
        try:
            self.lista_letras_digitalizadas.pop()
            self.atualizar_info_tela_digitalizada()
        except IndexError:
            print("A lista está vazia.")
        
    def atualizar_info_tela_digitalizada(self):
        lista_letras_digitalizadas_sem_colchetes = ''.join(str(valor) for valor in self.lista_letras_digitalizadas if valor is not None and valor != 'e')
        self.tela_digitalizada.setHtml(
            u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
            f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:64pt; font-family: Calibri\">{lista_letras_digitalizadas_sem_colchetes}</span></p></body></html>")

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