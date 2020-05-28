from convolutonal_neural_network import Convolution
from PIL import Image
import numpy as np
import random
import pytest


class TestConvolution(object):
    """
    Convolutionクラスのテストを行う。
    """
    def setup_method(self, method):
        print('method_start {}:'.format(method.__name__))
        self.convo = Convolution()
        self.input_test = np.array([[1, 2, 3, 4],
                                    [0, 1, 2, 3],
                                    [3, 0, 1, 2],
                                    [2, 3, 0, 1]])
        self.filter_test = np.array([[0, 1, 2],
                                     [2, 1, 1],
                                     [1, 0, 2]])
        self.input_test2 = np.array([[0, 1, 2, 3, 4],
                                     [1, 2, 3, 4, 5],
                                     [0, 1, 2, 3, 4],
                                     [1, 2, 3, 4, 5],
                                     [0, 1, 2, 3, 4]])
        self.filter_test2 = np.array([[0, -1, 0],
                                      [-1, 1, -1],
                                      [0, -1, 0]])

    def teardown_method(self, method):
        print('method_end {}:'.format(method.__name__))

    def test_outputsize_calculation(self):
        """ 出力サイズの計算テスト """
        self.convo.convolve2d(self.input_test, self.filter_test)
        width, height = self.convo.output_size
        assert width == 2
        assert height == 2


    def test_filter_calculation(self):
        """ フィルターで掛け合わせ計算のテスト """
        output_test = self.convo.convolve2d(self.input_test, self.filter_test)
        assert output_test[0][0] == 16
        assert output_test[0][1] == 22
        assert output_test[1][0] == 14
        assert output_test[1][1] == 16

    def test_filter_calculation_middle(self):
        """ 上記のテスト結果より大きい行列で試す """
        output_test = self.convo.convolve2d(self.input_test2, self.filter_test2)
        assert output_test[0][0] == -4
        assert output_test[0][1] == -7
        assert output_test[0][2] == -10
        assert output_test[1][0] == -5
        assert output_test[1][1] == -8
        assert output_test[1][2] == -11
        assert output_test[2][0] == -4
        assert output_test[2][1] == -7
        assert output_test[2][2] == -10


class TestImageConvolution(object):
    """
    class_name: ImageConvolution
    description:
        画像を用いて、畳み込み演算を行うテスト
    """
    def setup_method(self, method):
        print('method_start {}:'.format(method.__name__))
        self.im = Image.open('./tests/sample/substrate.png')
        self.convo = Convolution()
        self.gray_img = self.im.convert('L')
        self.gray_array = np.array(self.gray_img)
        self.img_array = np.array(self.im)
        self.test_filter = np.array([[-1, -1, -1],
                                 [-1, 8, -1],
                                 [-1, -1, -1]])

    def teardown_method(self, method):
        print('method_end {}:'.format(method.__name__))

    def test_gray_img_convolution_size(self):
        """ 画像の畳み込み演算後のサイズを確認 """
        output = self.convo.convolve2d(self.gray_array, self.test_filter)
        oh, ow = self.convo.output_size
        ih, iw = self.gray_array.shape
        assert oh == ih - 2
        assert ow == iw - 2

    def test_gray_img_convolution_show(self):
        """ 畳み込み演算後の画像を表示する """
        output = self.convo.convolve2d(self.gray_array, self.test_filter)
        img_array = np.clip(output,0,255).astype(np.uint8)
        img = Image.fromarray(img_array)
        img.show()
