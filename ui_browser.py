from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1200, 750)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setStyleSheet("QWidget#widget {\n"
"    border: 4px solid rgb(45, 45, 45);\n"
"}")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 80))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 80))
        self.widget_2.setStyleSheet("QWidget#widget_2 {\n"
"    background-color: #171332;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    color:#fff;\n"
"    font-size: 15px;\n"
"    font-family: entypo;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: #D3D3D3;\n"
"}\n"
"\n"
"QPushButton#pushButton_3:hover {\n"
"    color: #FF0000;\n"
"}\n"
"\n"
"QPushButton#pushButton_3:pressed {\n"
"    color: #FF0000;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    padding-top: 5px;\n"
"    padding-left: 5px;\n"
"    color: #D3D3D3;\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setContentsMargins(12, -1, 12, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.logo = QSvgWidget("cactus.svg", self.widget_2)
        self.logo.setMinimumSize(QtCore.QSize(25, 25))
        self.logo.setMaximumSize(QtCore.QSize(25, 25))
        self.logo.setObjectName("logo")
        self.horizontalLayout.addWidget(self.logo)
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: #fff;")
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.btn_minimize = QtWidgets.QPushButton(self.widget_2)
        self.btn_minimize.setMinimumSize(QtCore.QSize(25, 25))
        self.btn_minimize.setMaximumSize(QtCore.QSize(25, 25))
        self.btn_minimize.setObjectName("btn_minimize")
        self.horizontalLayout.addWidget(self.btn_minimize)
        self.btn_resize = QtWidgets.QPushButton(self.widget_2)
        self.btn_resize.setMinimumSize(QtCore.QSize(25, 25))
        self.btn_resize.setMaximumSize(QtCore.QSize(25, 25))
        self.btn_resize.setCheckable(True)
        self.btn_resize.setObjectName("btn_resize")
        self.horizontalLayout.addWidget(self.btn_resize)
        self.btn_exit = QtWidgets.QPushButton(self.widget_2)
        self.btn_exit.setMinimumSize(QtCore.QSize(25, 25))
        self.btn_exit.setMaximumSize(QtCore.QSize(25, 25))
        self.btn_exit.setObjectName("btn_exit")
        self.horizontalLayout.addWidget(self.btn_exit)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btn_forward = QtWidgets.QPushButton(self.widget_2)
        self.btn_forward.setMinimumSize(QtCore.QSize(25, 25))
        self.btn_forward.setMaximumSize(QtCore.QSize(25, 25))
        self.btn_forward.setObjectName("btn_forward")
        self.gridLayout.addWidget(self.btn_forward, 0, 1, 1, 1)
        self.btn_back = QtWidgets.QPushButton(self.widget_2)
        self.btn_back.setMinimumSize(QtCore.QSize(25, 25))
        self.btn_back.setMaximumSize(QtCore.QSize(25, 25))
        self.btn_back.setObjectName("btn_back")
        self.gridLayout.addWidget(self.btn_back, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lineEdit.setStyleSheet("border-radius: 5px;\n"
"margin-left: 5px;\n"
"margin-right: 5px;")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 3, 1, 1)
        self.btn_reload = QtWidgets.QPushButton(self.widget_2)
        self.btn_reload.setMinimumSize(QtCore.QSize(25, 25))
        self.btn_reload.setMaximumSize(QtCore.QSize(25, 25))
        self.btn_reload.setObjectName("btn_reload")
        self.gridLayout.addWidget(self.btn_reload, 0, 2, 1, 1)
        self.btn_downloads = QtWidgets.QPushButton(self.widget_2)
        self.btn_downloads.setMinimumSize(QtCore.QSize(25, 25))
        self.btn_downloads.setMaximumSize(QtCore.QSize(25, 25))
        self.btn_downloads.setObjectName("btn_downloads")
        self.gridLayout.addWidget(self.btn_downloads, 0, 5, 1, 1)
        self.btn_history = QtWidgets.QPushButton(self.widget_2)
        self.btn_history.setMinimumSize(QtCore.QSize(25, 25))
        self.btn_history.setMaximumSize(QtCore.QSize(25, 25))
        self.btn_history.setObjectName("btn_history")
        self.gridLayout.addWidget(self.btn_history, 0, 4, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.webEngineView = QWebEngineView(self.widget)
        self.webEngineView.setUrl(QUrl('http://google.com'))
        self.webEngineView.setObjectName("webEngineView")
        self.verticalLayout_2.addWidget(self.webEngineView)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cactus Web"))
        self.label_4.setText(_translate("Form", "Cactus Web"))
        self.btn_minimize.setText(_translate("Form", "-"))
        self.btn_resize.setText(_translate("Form", ""))
        self.btn_exit.setText(_translate("Form", "✕"))
        self.btn_forward.setText(_translate("Form", "→"))
        self.btn_back.setText(_translate("Form", "←"))
        self.btn_reload.setText(_translate("Form", "⟲"))
        self.btn_downloads.setText(_translate("Form", ""))
        self.btn_history.setText(_translate("Form", ""))
