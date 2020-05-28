from .qt_app import MatplotlibWindow
from PyQt5.QtWidgets import QApplication
import sys


def execute():
    print("app start")
    app = QApplication([])
    window = MatplotlibWindow()
    window.show()
    sys.exit(app.exec_())
