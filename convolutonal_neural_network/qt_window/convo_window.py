# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'convo_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(964, 858)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 751, 81))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_5 = QtWidgets.QFrame(self.layoutWidget)
        self.frame_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.comboBox = QtWidgets.QComboBox(self.frame_5)
        self.comboBox.setGeometry(QtCore.QRect(20, 30, 331, 31))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(self.frame_5)
        self.label.setGeometry(QtCore.QRect(20, 0, 181, 16))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.frame_5)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setMaximumSize(QtCore.QSize(200, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 100, 901, 711))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(self.layoutWidget1)
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(3)
        self.frame.setObjectName("frame")
        self.MplImageWidget = MplImageWidget(self.frame)
        self.MplImageWidget.setGeometry(QtCore.QRect(10, 10, 421, 331))
        self.MplImageWidget.setObjectName("MplImageWidget")
        self.horizontalLayout_2.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.layoutWidget1)
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(3)
        self.frame_2.setObjectName("frame_2")
        self.MplImageConvoWidget = MplImageConvoWidget(self.frame_2)
        self.MplImageConvoWidget.setGeometry(QtCore.QRect(10, 10, 421, 331))
        self.MplImageConvoWidget.setObjectName("MplImageConvoWidget")
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_3 = QtWidgets.QFrame(self.layoutWidget1)
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.MplGraphWidget = MplGraphWidget(self.frame_3)
        self.MplGraphWidget.setGeometry(QtCore.QRect(10, 10, 421, 331))
        self.MplGraphWidget.setObjectName("MplGraphWidget")
        self.horizontalLayout_3.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.layoutWidget1)
        self.frame_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.MplGraphConvoWidget = MplGraphConvoWidget(self.frame_4)
        self.MplGraphConvoWidget.setGeometry(QtCore.QRect(10, 10, 421, 331))
        self.MplGraphConvoWidget.setObjectName("MplGraphConvoWidget")
        self.horizontalLayout_3.addWidget(self.frame_4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 964, 26))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_Open = QtWidgets.QAction(MainWindow)
        self.action_Open.setObjectName("action_Open")
        self.menu_File.addAction(self.action_Open)
        self.menubar.addAction(self.menu_File.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "フィルターを選択してください"))
        self.pushButton.setText(_translate("MainWindow", "畳み込み演算開始"))
        self.menu_File.setTitle(_translate("MainWindow", "&Image"))
        self.action_Open.setText(_translate("MainWindow", "&Open"))
from .mplgraphconvowidget import MplGraphConvoWidget
from .mplgraphwidget import MplGraphWidget
from .mplimageconvowidget import MplImageConvoWidget
from .mplimagewidget import MplImageWidget
