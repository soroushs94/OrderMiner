from PyQt5.QtWidgets import *
import sys
from ui.ui_functions import MyMainWindow

app = QApplication(sys.argv)
window = MyMainWindow()
window.showMaximized()
sys.exit(app.exec_())
