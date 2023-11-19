from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from gui.uis import *

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		
		# SET TITLE
		self.setWindowTitle('JG')
		
		# SET UI
		self.ui = UI()
		self.ui.setupUI(self)

if __name__ == '__main__':
	from sys import (argv, exit)
	app = QApplication(argv)
	mwin = MainWindow()
	mwin.show()
	exit(app.exec_())