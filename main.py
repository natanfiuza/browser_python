from PyQt5.QtWidgets import *
import sys
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):


    def go_home(self):
        self.browser.setUrl(QUrl('http://www.google.com'))

    def go_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, url):    
        self.url_bar.setText(url.toString())

    def __init__(self):
        super(MainWindow, self).__init__()
        self.stylesheet = 'QToolBar{padding:5;border: 1px solid #C8D0D3;}'
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        #Barra navegacao
        navbar = QToolBar()        
        navbar.setStyleSheet(self.stylesheet)
        self.addToolBar(navbar)

        #Botao Voltar
        btn_voltar = QAction('🔙',self)
        btn_voltar.triggered.connect(self.browser.back)
        navbar.addAction(btn_voltar)

        #Botao Reload
        btn_reload = QAction('🔃',self)
        btn_reload.triggered.connect(self.browser.reload)
        navbar.addAction(btn_reload)


        #Botao avancar
        btn_avancar = QAction("🔜",self)
        btn_avancar.triggered.connect(self.browser.forward)
        navbar.addAction(btn_avancar)

        #Botao Home
        btn_home = QAction('🏠',self)
        btn_home.triggered.connect(self.go_home)
        navbar.addAction(btn_home)

        #Barra de endereco
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.go_url)
        navbar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.update_url)

app = QApplication(sys.argv)
QApplication.setApplicationName('Browser Exemplo')
windows = MainWindow()

app.exec()