from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import cv2, sys, os
from RedeNeural.RetornaClasse import RetornaClasse

     
class Window(QMainWindow):  
    def __init__(self):
        super().__init__()
        caminho_pasta_imagens = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'View', 'Imagens')
        self.setWindowTitle("Tela Digitalizadora")
        self.setFixedSize(900, 600)
        self.setWindowIcon(QIcon(os.path.join(caminho_pasta_imagens, 'icone.png')))

        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)

        self.tela_digitalizada = QTextBrowser(self)
        self.tela_digitalizada.setObjectName(u"tela_digitalizada")
        self.tela_digitalizada.setGeometry(QRect(69, 21, 782, 289))
        self.tela_digitalizada.setAutoFillBackground(False)
        self.tela_digitalizada.setStyleSheet(u"background-color:#ffffff; border : 1px solid black")

        self.lado_esquerdo_amarelo = QLabel(self)
        self.lado_esquerdo_amarelo.setObjectName(u"lado_esquerdo_amarelo")
        self.lado_esquerdo_amarelo.setGeometry(QRect(0, 21, 70, 579))
        self.lado_esquerdo_amarelo.setAutoFillBackground(False)
        self.lado_esquerdo_amarelo.setStyleSheet(u"background-color:#ffffdf; border: 2px solid black")

        self.lado_direito_amarelo = QLabel(self)
        self.lado_direito_amarelo.setObjectName(u"lado_direito_amarelo")
        self.lado_direito_amarelo.setGeometry(QRect(850, 21, 150, 579))
        self.lado_direito_amarelo.setAutoFillBackground(False)
        self.lado_direito_amarelo.setStyleSheet(u"background-color:#ffffdf; border : 2px solid black")
        
        self.botao_salvar = QPushButton(self)
        self.botao_salvar.setGeometry(10, 30, 50, 50)
        self.botao_salvar.clicked.connect(self.save)
        self.botao_salvar.setIcon(QIcon(os.path.join(caminho_pasta_imagens, 'filesave.png')))
        self.botao_salvar.setIconSize(QSize(48, 48))
        self.botao_salvar.setStyleSheet(u"background-color:#ffffff")
        
        self.botao_digitalizar = QPushButton(self)
        self.botao_digitalizar.setGeometry(10, 90, 50, 50)
        self.botao_digitalizar.clicked.connect(self.digitalizar)
        self.botao_digitalizar.setIcon(QIcon(os.path.join(caminho_pasta_imagens, 'print.png')))
        self.botao_digitalizar.setIconSize(QSize(50, 50))
        self.botao_digitalizar.setStyleSheet(u"background-color:#ffffff")
        
        self.botao_limpar = QPushButton(self)
        self.botao_limpar.setGeometry(10, 150, 50, 50)
        self.botao_limpar.clicked.connect(self.clear)
        self.botao_limpar.setIcon(QIcon(os.path.join(caminho_pasta_imagens, 'limpar.png')))
        self.botao_limpar.setIconSize(QSize(48, 48))
        self.botao_limpar.setStyleSheet(u"background-color:#ffffff")
        
        self.botao_espessura = QPushButton(self)
        self.botao_espessura.setGeometry(10, 210, 50, 50)
        self.botao_espessura.clicked.connect(self.show_brush_size_dialog)

        self.botao_espessura.setIcon(QIcon(os.path.join(caminho_pasta_imagens, 'espessura.png')))
        self.botao_espessura.setIconSize(QSize(50, 50))
        self.botao_espessura.setStyleSheet(u"background-color:#ffffff")
        
        self.botao_escolher_cor = QPushButton(self)
        self.botao_escolher_cor.setGeometry(10, 270, 50, 50)
        self.botao_escolher_cor.clicked.connect(self.show_color_dialog)
        self.botao_escolher_cor.setIcon(QIcon(os.path.join(caminho_pasta_imagens, 'cor.png')))
        self.botao_escolher_cor.setIconSize(QSize(48, 48))
        self.botao_escolher_cor.setStyleSheet(u"background-color:#ffffff")
        
        self.botao_borracha = QPushButton(self)
        self.botao_borracha.setGeometry(10, 330, 50, 50)
        self.botao_borracha.clicked.connect(self.borracha)
        self.botao_borracha.setIcon(QIcon(os.path.join(caminho_pasta_imagens, 'borracha.png')))
        self.botao_borracha.setIconSize(QSize(48, 48))
        self.botao_borracha.setStyleSheet(u"background-color:#ffffff")
        
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
            #self.save()

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
        #comparar_print_imagem()
        self.pixmap = QPixmap(caminho_screenshot)
        self.retornaTextoImagem()
        '''self.label.setPixmap(self.pixmap)
        self.label.setGeometry(69, 0, self.pixmap.width(), self.pixmap.height()) 
        self.show()
        self.label.setStyleSheet(f"background-image: url({caminho_screenshot})")
        self.label.setStyleSheet(u"background-color:#ffffff; border : 1px solid black")'''
        
    def clear(self):
        self.image.fill(Qt.white)
        self.update()

    def show_color_dialog(self):
        color = QColorDialog.getColor(initial=self.brush_color)
        
        if color.isValid():
            self.brush_color = color
            
    def borracha(self):
        self.brush_color = QColor("#FFFFFF")

    def show_brush_size_dialog(self):
        brush_size_dialog = BrushThicknessDialog()
        result = brush_size_dialog.exec_()

        if result == QDialog.Accepted:
            self.brush_size = brush_size_dialog.get_selected_thickness()

    def retornaTextoImagem(self):

        caminho_pasta_imagens = os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'View', 'Imagens', 'screenshot.png'))
        retornaClasse = RetornaClasse()
        letraDigitalizada = retornaClasse.prever_letra(caminho_pasta_imagens)

        self.tela_digitalizada.setHtml(
            u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
            f"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-family: Calibri\">{letraDigitalizada}</span></p></body></html>")

class BrushThicknessDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Escolher Espessura do Pincel")
        self.setFixedSize(200, 150)

        layout = QVBoxLayout()
        self.brush_size = 2
        options = ["Fina (10px)", "Média (20px)", "Grossa (30px)"]
        self.radio_buttons = []

        for option in options:
            radio_button = QRadioButton(option, self)
            layout.addWidget(radio_button)
            self.radio_buttons.append(radio_button)

        button = QPushButton("OK", self)
        button.clicked.connect(self.accept)

        layout.addWidget(button)
        self.setLayout(layout)

    def get_selected_thickness(self):
        for index, radio_button in enumerate(self.radio_buttons):
            if radio_button.isChecked():
                return [10, 20, 30][index]

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()