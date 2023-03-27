# -*- coding: utf-8 -*-

import pyshorteners
from PySide2 import (QtCore, QtGui, QtWidgets)
from ui_interface import *
import sys

class Encurtador(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		# ADICIONA UM TÍTULO AO SOFTWARE
		self.setWindowTitle("Encurtador de urls com Python")

		#ADICIONA UM ÍCONE AO SOFTWARE
		self.setWindowIcon(QtGui.QIcon('icone.ico'))

		# BOTÃO PARA ENCURTAR
		self.ui.btn_Encurtar.clicked.connect(self.Encurtar)


		# FUNÇÃO ENCURTADOR
	def Encurtar(self):

		# URL INSERIDA
		url_encurtar = self.ui.le0_link_encurtar.text()

		# ENCURTA A URL
		encurtar_url = pyshorteners.Shortener()

		# SE O CAMPO ESTIVER VAZIO, IRÁ ABRIR UM POPUP
		if url_encurtar == '':
			msg = QMessageBox()
			msg.setIcon(QMessageBox.Warning)
			msg.setWindowIcon(QtGui.QIcon('icone.ico'))
			msg.setWindowTitle('Encurtando Url')
			msg.setText('Url inválida ou vazia')
			msg.setStandardButtons(QMessageBox.Ok)
			x = msg.exec_()

		# CASO TENHA UMA URL VÁLIDA, ENTÃO IRÁ ENCURTAR
		else:

			# FORMATA A URL PARA TINYURL
			link_encurtado = f'{encurtar_url.tinyurl.short(url_encurtar)}'

			# ADICIONA A URL NO CAMPO LINK ENCURTADO
			self.ui.le1_link_encurtado.setText(link_encurtado)
			
			# CRIA UM ARQUIVO CHAMADO 'Links Encurtados.txt' E ESCREVE A URL ORIGINAL E URL ENCURTADA
			f = open("Links Encurtados.txt", "a")
			f.write(f"\n{url_encurtar} - {link_encurtado}")


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = Encurtador()
	window.show()
	sys.exit(app.exec_())