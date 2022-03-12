from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from ui_browser import Ui_Form
import sys


class MoveWeb(QtWidgets.QWidget):
    def __init__(self):
        super(MoveWeb, self).__init__()

    def mouse_clicked(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouse_moved(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()


class CactusWeb(MoveWeb, Ui_Form):
    def __init__(self):
        super(CactusWeb, self).__init__()
        self.setupUi(self)

        # minimize, window, exit
        self.btn_minimize.clicked.connect(self.showMinimized)
        self.btn_resize.clicked.connect(self.maxed_window)
        self.btn_exit.clicked.connect(sys.exit)

        # back, forward, refresh
        self.btn_back.clicked.connect(self.backward)
        self.btn_forward.clicked.connect(self.forward)
        self.btn_reload.clicked.connect(self.refresh)

        # history, downloads
        # self.btn_downloads.clicked.connect()
        # self.btn_history.clicked.connect()

        self.lineEdit.returnPressed.connect(self.load)

        self.webEngineView.urlChanged.connect(self.update_url)

    def load(self):
        url = QtCore.QUrl.fromUserInput(self.lineEdit.text())
        if url.isValid():
            self.webEngineView.load(url)
        else:
            pass

    def backward(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Back)

    def forward(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Forward)

    def refresh(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Reload)

    def update_url(self, q):
        self.lineEdit.setText(q.toString())

    def maxed_window(self):
        if self.btn_resize.isChecked():
            self.showMaximized()
            self.btn_resize.setText("")
        else:
            self.showNormal()
            self.btn_resize.setText("")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = CactusWeb()
    Form.show()
    sys.exit(app.exec_())
