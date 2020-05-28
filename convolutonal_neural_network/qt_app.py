from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QFileDialog
from PyQt5.QtWidgets import QMessageBox
from .qt_window import Ui_MainWindow
from convolutonal_neural_network import Convolution
from PIL import Image
import numpy as np
import random
import os


class MatplotlibWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MatplotlibWindow, self).__init__(parent)
        self.file_name = None
        self.im = None
        self.gray_im = None
        self.gray_array = None
        self.filter_name = None
        self.kernel = None
        self.convo = Convolution()
        self.extensions = ['.jpg', '.png']

        # UI設定
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.action_Open.triggered.connect(self.open)
        self.ui.comboBox.addItem("None")
        self.ui.comboBox.addItem("HighPass")
        self.ui.comboBox.activated[str].connect(self.on_combo_activated)
        self.ui.pushButton.clicked.connect(self.update_graph)

    def open(self):
        (fileName, selectedFilter) = QFileDialog.getOpenFileName(self,
            'Open file', os.path.expanduser('~'))
        if fileName != "" and os.path.splitext(fileName)[1] in self.extensions:
            self.file_name = fileName
            self.im = Image.open(self.file_name)
            self.gray_im = self.im.convert('L')
            self.gray_array = np.array(self.gray_im)
            QMessageBox.information(self, "Open", "Open ImageFile")
            self.ui.MplImageWidget.canvas.axes.clear()
            self.ui.MplImageWidget.canvas.axes.imshow(self.gray_im)
            self.ui.MplImageWidget.canvas.draw()
            self.ui.MplGraphWidget.canvas.axes.clear()
            self.ui.MplGraphWidget.canvas.axes.hist(
                    self.gray_array.flatten(), 128)
            self.ui.MplGraphWidget.canvas.draw()
        else:
            QMessageBox.information(self, "Open", "Open Filed ImageFile")

    def on_combo_activated(self, text):
        self.filter_name = text
        if self.filter_name == "HighPass":
            sharp_kernel = lambda k: np.array([[0, -k, 0],
                                               [-k, 1+4*k, -k],
                                               [0, -k, 0]])
            self.kernel = sharp_kernel(3)

    def update_graph(self):
        if (self.filter_name is not None) and (self.file_name is not None):
            output = self.convo.convolve2d(self.gray_array, self.kernel)
            img_array = np.clip(output, 0, 255).astype(np.uint8)
            self.ui.MplImageConvoWidget.canvas.axes.imshow(img_array)
            self.ui.MplImageConvoWidget.canvas.draw()
            self.ui.MplGraphConvoWidget.canvas.axes.hist(
                    img_array.flatten(), 128)
            self.ui.MplGraphConvoWidget.canvas.draw()

        else:
            QMessageBox.information(self, "Convolution", "Convolution Failed")
