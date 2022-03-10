import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *


class OrchidWeb(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(OrchidWeb, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        search_bar = QToolBar()
        self.addToolBar(search_bar)

        btn_back = QAction('←', self)
        btn_back.triggered.connect(self.browser.back)
        search_bar.addAction(btn_back)

        btn_forward = QAction('→', self)
        btn_forward.triggered.connect(self.browser.forward)
        search_bar.addAction(btn_forward)

        btn_refresh = QAction('↺', self)
        btn_refresh.triggered.connect(self.browser.reload)
        search_bar.addAction(btn_refresh)

        btn_home = QAction('⌂', self)
        btn_home.triggered.connect(self.home)
        search_bar.addAction(btn_home)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.to_url)
        search_bar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def home(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName("Orchid Web")
window = OrchidWeb()
app.exec_()

