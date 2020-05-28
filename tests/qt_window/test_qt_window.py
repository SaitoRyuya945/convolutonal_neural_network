import pytest
from PyQt5.QtWidgets import QApplication
import numpy as np
import random
from convolutonal_neural_network import MatplotlibWindow
from PIL import Image


class TestQtApplication(object):
    """
    class_name: QtApplication
    description:
        グラフ表示用のQtアプリのテスト
    """
    def setup_method(self, method):
        print('method_start {}:'.format(method.__name__))
        self.app = QApplication([])
        self.window = MatplotlibWindow()
        self.im = Image.open('./tests/sample/substrate.png')
        self.gray_img = self.im.convert('L')
        self.gray_array = np.array(self.gray_img)
        self.img_array = np.array(self.im)

    def teardown_method(self, method):
        print('method_end {}:'.format(method.__name__))

    def test_app_exe(self):
        # アプリの起動テスト
        self.window.show()
        self.app.exec_()
        assert True

    def update_graph(self):
        f = random.randint(1, 100)
        length = 100
        t = np.linspace(0,1,length)
        cos_signal = np.cos(2*np.pi*f*t)
        sin_signal = np.sin(2*np.pi*f*t)

        self.window.ui.MplGraphWidget.canvas.axes.clear()
        self.window.ui.MplGraphWidget.canvas.axes.plot(t, cos_signal)
        self.window.ui.MplGraphWidget.canvas.axes.legend(('cos'),
            loc='upper left')
        self.window.ui.MplGraphWidget.canvas.axes.set_title('Cos Signal')
        self.window.ui.MplGraphWidget.canvas.draw()

        self.window.ui.MplGraphConvoWidget.canvas.axes.clear()
        self.window.ui.MplGraphConvoWidget.canvas.axes.plot(t, sin_signal)
        self.window.ui.MplGraphConvoWidget.canvas.axes.legend(('sin'),
            loc='upper left')
        self.window.ui.MplGraphConvoWidget.canvas.axes.set_title('Sin Signal')
        self.window.ui.MplGraphConvoWidget.canvas.draw()

    def test_app_clicked_graph(self):
        # グラフをボタンを押して表示する
        self.window.ui.pushButton.clicked.connect(self.update_graph)
        self.window.show()
        self.app.exec_()
        assert True

    def test_app_clicked_image(self):
        # 画像を表示する
        self.window.ui.MplImageWidget.canvas.axes.clear()
        self.window.ui.MplImageWidget.canvas.axes.imshow(self.gray_array)
        self.window.ui.MplImageConvoWidget.canvas.axes.clear()
        self.window.ui.MplImageConvoWidget.canvas.axes.imshow(self.img_array)

        self.window.show()
        self.app.exec_()
        assert True

    def test_app_open_file(self):
        # ./sample/substrate.pngを選択してみる
        self.window.show()
        self.app.exec_()
        assert self.window.file_name != None

    def test_app_combo(self):
        # comboboxのテスト
        self.window.ui.comboBox.addItem("select")
        self.window.ui.comboBox.addItem("Combo")
        self.window.show()
        self.app.exec_()
        assert True
