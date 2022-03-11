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


class OrchidWeb(MoveWeb, Ui_Form):
    def __init__(self):
        super(OrchidWeb, self).__init__()
        self.setupUi(self)

        # minimize, window, exit
        self.pushButton.clicked.connect(self.showMinimized)
        self.pushButton_2.clicked.connect(self.maxed_window)
        self.pushButton_3.clicked.connect(sys.exit)

        # back, forward, refresh
        self.pushButton_4.clicked.connect(self.backward)
        self.pushButton_5.clicked.connect(self.forward)
        self.pushButton_6.clicked.connect(self.refresh)

        self.lineEdit.returnPressed.connect(self.load)

        self.webEngineView.urlChanged.connect(self.update_url)

    def load(self):
        url = QtCore.QUrl.fromUserInput(self.lineEdit.text())
        if url.isValid():
            self.webEngineView.load(url)

    def backward(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Back)

    def forward(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Forward)

    def refresh(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.Reload)

    def update_url(self, q):
        self.lineEdit.setText(q.toString())

    def maxed_window(self):
        if self.pushButton_2.isChecked():
            self.showMaximized()
            self.pushButton_2.setText("")
        else:
            self.showNormal()
            self.pushButton_2.setText("")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = OrchidWeb()
    Form.show()
    sys.exit(app.exec_())
