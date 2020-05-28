from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QFileDialog
from PyQt5.QtWidgets import QMessageBox
from .qt_window import Ui_MainWindow
import numpy as np
import random
import os


class MatplotlibWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MatplotlibWindow, self).__init__(parent)
        self.file_name = None
        self.combo_select = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.action_Open.triggered.connect(self.open)
        self.ui.comboBox.activated[str].connect(self.on_combo_activated)

    def open(self):
        (fileName, selectedFilter) = QFileDialog.getOpenFileName(self,
            'Open file', os.path.expanduser('~'))
        if fileName != "":
            self.file_name = fileName

    def on_combo_activated(self, text):
        self.combo_select = text

