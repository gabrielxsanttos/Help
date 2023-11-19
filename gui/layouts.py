from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from .buttons import *

class SideBar(QWidget):
	def __init__(self):
		super().__init__()
		
		self.setMinimumWidth(60)
		self.setStyleSheet("background-color: #303030;")
		# LAYOUT
		self.layout = QVBoxLayout(self)
		self.layout.setContentsMargins(0,0,0,0)
		self.layout.setSpacing(0)
		
		# TOP
		self.top = QWidget()
		self.top.setMinimumHeight(60)
		self.topLAYOUT = QVBoxLayout(self.top)
		self.topLAYOUT.setContentsMargins(0,0,0,0)
		self.topLAYOUT.setSpacing(0)
		
		# TOP > MENU
		self.menu = Push(
		    TEXT = 'menu',
		    ICON = 'menu-icon.svg',
		    COLOR_ICON = '#fff',
		    
		)
		
		# TOP ADD WIDGETS
		self.topLAYOUT.addWidget(self.menu)
		
		
		# SPACER
		self.spacer = QSpacerItem(20,20, QSizePolicy.Minimum, QSizePolicy.Expanding)
		
		
		# BOTTOM
		self.bottom = QWidget()
		self.bottom.setMinimumHeight(60)
		self.bottomLAYOUT = QVBoxLayout(self.bottom)
		self.bottomLAYOUT.setContentsMargins(0,0,0,0)
		self.bottomLAYOUT.setSpacing(0)
		
		# BOTTOM > CONFIG
		self.config = Push(
		    TEXT= 'config',
		    ICON= 'config-icon.svg',
		)
		
		# BOTTOM ADD WIDGETS
		self.bottomLAYOUT.addWidget(self.config)
		
		# LAYOUT ADD WIDGETS
		self.layout.addWidget(self.top)
		self.layout.addItem(self.spacer)
		self.layout.addWidget(self.bottom)
		
		
		