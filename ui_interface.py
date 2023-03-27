# -*- coding: utf-8 -*-

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(460, 288)
        MainWindow.setMinimumSize(460, 288)
        MainWindow.setMaximumSize(460, 288)
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Frame_Principal = QFrame(self.centralwidget)
        self.Frame_Principal.setObjectName(u"Frame_Principal")
        self.Frame_Principal.setStyleSheet(u"background-color: rgb(240, 240, 240);")
        self.Frame_Principal.setFrameShape(QFrame.StyledPanel)
        self.Frame_Principal.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.Frame_Principal)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame = QFrame(self.Frame_Principal)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Titulo_Encurtador = QLabel(self.frame)
        self.Titulo_Encurtador.setObjectName(u"Titulo_Encurtador")
        self.Titulo_Encurtador.setStyleSheet(u"font: 8pt \"Arial\";")

        self.horizontalLayout_3.addWidget(self.Titulo_Encurtador, 0, Qt.AlignHCenter)


        self.verticalLayout_4.addWidget(self.frame)

        self.frame_2 = QFrame(self.Frame_Principal)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_Vazio_esqA = QFrame(self.frame_2)
        self.frame_Vazio_esqA.setObjectName(u"frame_Vazio_esqA")
        self.frame_Vazio_esqA.setFrameShape(QFrame.StyledPanel)
        self.frame_Vazio_esqA.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_Vazio_esqA)

        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_8)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl1_Link_para_encurtar = QLabel(self.frame_8)
        self.lbl1_Link_para_encurtar.setObjectName(u"lbl1_Link_para_encurtar")
        self.lbl1_Link_para_encurtar.setStyleSheet(u"font: 10pt \"Arial\";\n"
"color: #343434;\n"
"")

        self.verticalLayout_2.addWidget(self.lbl1_Link_para_encurtar)

        self.le0_link_encurtar = QLineEdit(self.frame_8)
        self.le0_link_encurtar.setObjectName(u"le0_link_encurtar")
        self.le0_link_encurtar.setStyleSheet(u"border: 1px solid #343434;\n"
"font: 9pt \"Arial\";\n"
"")

        self.verticalLayout_2.addWidget(self.le0_link_encurtar)

        self.lbl2_link_encurtado = QLabel(self.frame_8)
        self.lbl2_link_encurtado.setObjectName(u"lbl2_link_encurtado")
        self.lbl2_link_encurtado.setStyleSheet(u"font: 10pt \"Arial\";\n"
"color: #343434;\n"
"")

        self.verticalLayout_2.addWidget(self.lbl2_link_encurtado)

        self.le1_link_encurtado = QLineEdit(self.frame_8)
        self.le1_link_encurtado.setObjectName(u"le1_link_encurtado")
        self.le1_link_encurtado.setStyleSheet(u"border: 1px solid #343434;\n"
"font: 9pt \"Arial\";\n"
"")

        self.verticalLayout_2.addWidget(self.le1_link_encurtado)


        self.horizontalLayout_2.addWidget(self.frame_8)

        self.frame_vazio_dirA = QFrame(self.frame_2)
        self.frame_vazio_dirA.setObjectName(u"frame_vazio_dirA")
        self.frame_vazio_dirA.setFrameShape(QFrame.StyledPanel)
        self.frame_vazio_dirA.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_vazio_dirA)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.Frame_Principal)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_vazio_esqB = QFrame(self.frame_3)
        self.frame_vazio_esqB.setObjectName(u"frame_vazio_esqB")
        self.frame_vazio_esqB.setFrameShape(QFrame.StyledPanel)
        self.frame_vazio_esqB.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_vazio_esqB)

        self.frame_9 = QFrame(self.frame_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_9)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_Encurtar = QPushButton(self.frame_9)
        self.btn_Encurtar.setObjectName(u"btn_Encurtar")
        self.btn_Encurtar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_Encurtar.setStyleSheet(u"QPushButton {\n"
"	font: 10pt \"Arial\";\n"
"	color: #fff;\n"
"	outline: 0;\n"
"	border: 5px solid #343434;\n"
"	background-color: rgb(52, 52, 52);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	color: #000000;\n"
"	border: 5px solid #8d8d8d;\n"
"	background-color: rgb(141, 141, 141);\n"
"}\n"
"\n"
"\n"
"QPushButton#btn_Encurtar:pressed {\n"
"	padding-left: 2px;\n"
"	padding-top: 2px;\n"
"	color: #000000;\n"
"	border: 5px solid #fff;\n"
"	background-color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_Encurtar, 0, Qt.AlignTop)


        self.horizontalLayout.addWidget(self.frame_9, 0, Qt.AlignTop)

        self.frame_vazio_dirB = QFrame(self.frame_3)
        self.frame_vazio_dirB.setObjectName(u"frame_vazio_dirB")
        self.frame_vazio_dirB.setFrameShape(QFrame.StyledPanel)
        self.frame_vazio_dirB.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_vazio_dirB)


        self.verticalLayout_4.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.Frame_Principal)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Titulo_Encurtador.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Encurtador simples de url com python</span></p></body></html>", None))
        self.lbl1_Link_para_encurtar.setText(QCoreApplication.translate("MainWindow", u"Link para encurtar", None))
        self.le0_link_encurtar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"URL", None))
        self.lbl2_link_encurtado.setText(QCoreApplication.translate("MainWindow", u"Link encurtado", None))
        self.le1_link_encurtado.setPlaceholderText(QCoreApplication.translate("MainWindow", u"URL", None))
        self.btn_Encurtar.setText(QCoreApplication.translate("MainWindow", u"Encurtar", None))
    # retranslateUi

