import numpy as np
from numpy.lib.stride_tricks import as_strided


class Convolution():
    def __init__(self, padding=0, stride=1):
        self.__output_size = None
        self.__padding = padding
        self.__stride = stride
        self.__output = None

    @property
    def output_size(self):
        pass

    @output_size.getter
    def output_size(self):
        return self.__output_size

    @property
    def output(self):
        pass

    @output.getter
    def output(self):
        return self.__output

    def convolve2d(self, img, kernel):
        """ 2次元の畳み込み演算 """

        # 出力サイズの計算(部分行列の大きさでもある 計算式はpdfに記載)
        sub_shape = tuple(np.add(np.subtract(
            np.add(img.shape, 2*self.__padding),kernel.shape)/self.__stride,
            1).astype(np.int64))
        self.__output_size = sub_shape

        # 入力行列を部分行列に変換
        submatrix = as_strided(img, kernel.shape + sub_shape,
                img.strides * (1 + self.__stride))

        # 部分行列とフィルターの掛け合わせ計算(
        # アインシュタイン和：詳細はpdfを参照)
        self.__output = np.einsum('ij,ijkl->kl', kernel, submatrix)

        return self.__output
