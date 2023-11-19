from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from .layouts import *

class UI(object):
	@staticmethod
	def setupUI(parent):
		if not parent.objectName():
			parent.setObjectName('MainWindow')
		
		central = QWidget()
		layout = QHBoxLayout(central)
		layout.setContentsMargins(0,0,0,0)
		layout.setSpacing(0)
		
		# CONTENTS
		contents = QFrame()
		contentsLAYOUT = QVBoxLayout(contents)
		contentsLAYOUT.setContentsMargins(0,0,0,0)
		contentsLAYOUT.setSpacing(0)
		
		# CONTENTS <STYLE>
		contents.setStyleSheet("background-color: #383838;")
		
		sidebar = SideBar()
		
		# TOP BAR
		topbar = QFrame()
		topbar.setMinimumHeight(60)
		topbar.setMaximumHeight(60)
		topbarLAYOUT = QHBoxLayout(topbar)
		topbarLAYOUT.setContentsMargins(0,0,0,0)
		topbarLAYOUT.setSpacing(0)
		
		# TOP BAR <STYLE>
		topbar.setStyleSheet("""
		background-color: #E6BF41;
		""")
		
		pages = QStackedWidget()
		
		# BOTTOM BAR
		bottombar = QFrame()
		bottombar.setMinimumHeight(60)
		bottombar.setMaximumHeight(60)
		bottombarLAYOUT = QHBoxLayout(bottombar)
		bottombarLAYOUT.setContentsMargins(0,0,0,0)
		bottombarLAYOUT.setSpacing(0)
		
		# BOTTOM BAR <STYLE>
		bottombar.setStyleSheet("""
		background-color: #E6BF41;
		""")
		
		
		# CENTRAL ADD WIDGETS
		layout.addWidget(sidebar)
		layout.addWidget(contents)
		
		
		
		
		
		# CONTENTS ADD WIDGETS
		contentsLAYOUT.addWidget(topbar)
		contentsLAYOUT.addWidget(pages)
		contentsLAYOUT.addWidget(bottombar)
		
		# TOP ADD WIDGETS
		
		# PAGES ADD WIDGETS
		
		# BOTTOM ADD WIDGETS
		
		
		parent.setCentralWidget(central)
		
		
	

