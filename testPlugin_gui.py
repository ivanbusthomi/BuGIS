# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\dummy_folder\testPlugin.ui'
#
# Created: Thu Aug 21 11:31:45 2014
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import helpDialog

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(445, 324)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(262, 14, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 3)
        self.doubleSpinBox = QtGui.QDoubleSpinBox(Dialog)
        self.doubleSpinBox.setMinimum(0.01)
        self.doubleSpinBox.setMaximum(10000.0)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.gridLayout.addWidget(self.doubleSpinBox, 2, 3, 1, 1)
        self.comboInputA = QtGui.QComboBox(Dialog)
        self.comboInputA.setObjectName(_fromUtf8("comboInputA"))
        self.gridLayout.addWidget(self.comboInputA, 0, 0, 1, 4)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 4, 1, 1)
        self.comboInputB = QtGui.QComboBox(Dialog)
        self.comboInputB.setObjectName(_fromUtf8("comboInputB"))
        self.gridLayout.addWidget(self.comboInputB, 1, 0, 1, 4)
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 4, 1, 1)
        self.lineInput = QtGui.QLineEdit(Dialog)
        self.lineInput.setObjectName(_fromUtf8("lineInput"))
        self.gridLayout.addWidget(self.lineInput, 3, 0, 1, 4)
        self.browseButton = QtGui.QPushButton(Dialog)
        self.browseButton.setObjectName(_fromUtf8("browseButton"))
        self.gridLayout.addWidget(self.browseButton, 3, 4, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(Dialog)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.gridLayout.addWidget(self.pushButton_3, 4, 0, 1, 1)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 4, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(100, 14, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 4, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 4, 3, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout.addWidget(self.pushButton_2, 4, 2, 1, 1)
        self.textBrowser = QtGui.QTextBrowser(Dialog)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.gridLayout.addWidget(self.textBrowser, 6, 0, 1, 5)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 5, 0, 1, 1)

        self.retranslateUi(Dialog)
        # these 2 connect functions are not important
        #QtCore.QObject.connect(self.comboInputA, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), self.label.setNum)
        #QtCore.QObject.connect(self.comboInputB, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), self.label_2.setText)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.close)

        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.comboInputA, self.comboInputB)
        Dialog.setTabOrder(self.comboInputB, self.lineInput)
        Dialog.setTabOrder(self.lineInput, self.browseButton)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_3.setText(_translate("Dialog", "Interval (m)", None))
        self.label.setText(_translate("Dialog", "Input Layer A", None))
        self.lineInput.setPlaceholderText(_translate("Dialog", "Define directory for output shapefile", None))
        self.browseButton.setText(_translate("Dialog", "Browse...", None))
        self.pushButton_3.setText(_translate("Dialog", "Help", None))
        self.label_2.setText(_translate("Dialog", "Input Layer B", None))
        self.pushButton.setText(_translate("Dialog", "Close", None))
        self.pushButton_2.setText(_translate("Dialog", "Run", None))
        self.label_4.setText(_translate("Dialog", "processing logs", None))