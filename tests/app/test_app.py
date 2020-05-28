"""
メインのアプリ用テスト
実際に実行したときにここに書かれているプログラムが動くようになっている。
選択できる画像はjpg,pngで白黒画像のみを扱うことができる（カラーを選択した場合、
自動で白黒になる）今後、RGBを扱うプログラムに変更していく。
"""

import pytest
from PyQt5.QtWidgets import QApplication
from convolutonal_neural_network import MatplotlibWindow
import numpy as np


class TestQtApplication(object):
    """
    class_name: QtApplication
    description:
        Qtを用いたアプリケーション
    """
    def setup_method(self, method):
        print('method_start {}:'.format(method.__name__))
        self.app = QApplication([])
        self.window = MatplotlibWindow()
        self.window.show()
        self.app.exec_()

    def teardown_method(self, method):
        print('method_end {}:'.format(method.__name__))

    def test_lowpass_fileter_select(self):
        # 画像の読み込みテスト(jpg, pngのみ)
        assert self.window.im != None
        assert self.window.gray_im != None

    def test_filter_select(self):
        # フィルターの選択をテスト(HighPassFilterの選択)
        assert self.window.filter_name == "HighPass"
        assert self.window.kernel[0][0] == 0
        assert self.window.kernel[0][1] == -3
        assert self.window.kernel[0][2] == 0
        assert self.window.kernel[1][0] == -3
        assert self.window.kernel[1][1] == 13
        assert self.window.kernel[1][2] == -3
        assert self.window.kernel[2][0] == 0
        assert self.window.kernel[2][1] == -3
        assert self.window.kernel[2][2] == 0

    def test_convolution(self):
        """ 畳み込み演算を行い結果を表示する
         テストフロー:
          1. tests/sample/substrate.pngを選択
          2. HightPassFilterを選択
          3. 畳み込み演算開始ボタンを押す
        """
        assert True
