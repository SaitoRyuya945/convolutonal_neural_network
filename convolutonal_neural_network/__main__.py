import pytest
from PyQt5.QtWidgets import QApplication
from convolutonal_neural_network import MatplotlibWindow
import numpy as np
import sys

if __name__ == "__main__":
    app = QApplication([])
    window = MatplotlibWindow()
    window.show()
    sys.exit(app.exec_())
