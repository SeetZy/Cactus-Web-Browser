from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 550)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setStyleSheet("QWidget#widget {\n"
"    border: 4px solid black;\n"
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
"    background-color: rgb(20, 20, 20);\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    color: rgb(144, 144, 144);\n"
"    font: bold;\n"
"    font-size: 15px;\n"
"    font-family: entypo;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color: rgb(142, 176, 27);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    padding-top: 5px;\n"
"    padding-left: 5px;\n"
"    color: rgb(91, 88, 53);\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setContentsMargins(12, -1, 12, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(144, 144, 144);")
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_2.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_2.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_3.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_3.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_5.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_5.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 0, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_4.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_4.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lineEdit.setStyleSheet("border-radius: 5px;\n"
"padding-;eft: 5px;")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 3, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_6.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_6.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 0, 2, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_7.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_7.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 0, 5, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_8.setMinimumSize(QtCore.QSize(25, 25))
        self.pushButton_8.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 0, 4, 1, 1)
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
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "Orchid Web"))
        self.pushButton.setText(_translate("Form", "-"))
        self.pushButton_2.setText(_translate("Form", ""))
        self.pushButton_3.setText(_translate("Form", "✕"))
        self.pushButton_5.setText(_translate("Form", "→"))
        self.pushButton_4.setText(_translate("Form", "←"))
        self.pushButton_6.setText(_translate("Form", "⟲"))
        self.pushButton_7.setText(_translate("Form", ""))
        self.pushButton_8.setText(_translate("Form", ""))
