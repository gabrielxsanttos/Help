from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

import os

class Push(QPushButton):
	def __init__(self,
	    TEXT       ='',
	    COLOR      ='#E6BF41',
	    HOVER      ='#272727',
	    ICON       ='',
		COLOR_ICON ='#FFF',
	):
		super().__init__()
		
		self.setText(TEXT)
		
		self.setMinimumHeight(60)
		
		self.COLOR = COLOR
		self.ICON = ICON
		self.COLOR_ICON = COLOR_ICON
		self.HOVER = HOVER
		
		self.setStyling()
		
		self.clicked.connect(lambda: self.setStyling(True))
			
			
	def setStyling(self, IS_ACTIVE=False):
		style = f"""
		QPushButton {{
		    color: #FFF;
		    background-color: {self.COLOR};
		    padding-left: 60px;
		    text-align: left;
		    border: none;
		
		}}
		QPushButton:hover {{
		    background-color: {self.HOVER};
		
		}}
		
		QPushButton:pressed {{
		    background-color: {self.HOVER};
		    
		}}
		"""
		
		active = f"""
		QPushButton {{
		    background-color: {self.HOVER};
		    border-left: 8px solid #E6BF41;
		}}
		
		"""
		if not IS_ACTIVE:
			self.setStyleSheet(style)
		else:
			self.setStyleSheet(style + active)
	
	def paintEvent(self, event):
		QPushButton.paintEvent(self, event)
		qp = QPainter(self)
		qp.setRenderHint(QPainter.Antialiasing)
		qp.setPen(Qt.NoPen)
		
		rect = QRect(0,0,60,self.height())
		
		self.drawIcon(qp, self.ICON, rect, self.COLOR_ICON)
		
		qp.end()
		
	def drawIcon(self, QP, IMAGE, RECT, COLOR):
		abspath = os.path.abspath(os.getcwd())
		folder = "assets/"
		path = os.path.join(abspath, folder)
		iconpath = os.path.normpath(os.path.join(path, IMAGE))
		icon = QPixmap(iconpath)
		qp = QPainter(icon)
		qp.setCompositionMode(QPainter.CompositionMode_SourceIn)
		qp.fillRect(icon.rect(), QColor(COLOR))
		
		QP.drawPixmap(
            (RECT.width() - icon.width()) / 2,
            (RECT.height() - icon.height()) / 2,
            icon
		)
		
		qp.end()
		