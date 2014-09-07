# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\dummy_folder\helpDialog.ui'
#
# Created: Thu Aug 21 11:15:35 2014
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class ui_helpDialog(object):
    def setupUi(self, hDialog):
        hDialog.setObjectName(_fromUtf8("Dialog"))
        hDialog.resize(400, 300)
        self.gridLayout = QtGui.QGridLayout(hDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.textBrowser = QtGui.QTextBrowser(hDialog)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(298, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.pushButton = QtGui.QPushButton(hDialog)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout.addWidget(self.pushButton, 1, 1, 1, 1)

        self.retranslateUi(hDialog)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), hDialog.close)
        QtCore.QMetaObject.connectSlotsByName(hDialog)

    def retranslateUi(self, hDialog):
        hDialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:14px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,Helvetica,sans\'; font-size:8pt; color:#000000;\">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam ut metus nec ante vestibulum pretium nec et quam. Nam mollis a lacus non suscipit. Vivamus ac tempus est, vel lobortis nibh. Suspendisse potenti. Cras lectus sem, pharetra eu purus non, adipiscing adipiscing quam. Phasellus a sapien adipiscing ante malesuada suscipit quis ut odio. Donec at vestibulum purus. Maecenas quis risus pulvinar, tempus lectus sit amet, placerat felis. Aenean faucibus sem ut nulla vestibulum facilisis. Aenean mi nunc, elementum eget congue vitae, adipiscing eget mauris. Curabitur non condimentum mi. Quisque a dui eleifend, mattis est sed, tincidunt leo. Duis non arcu eu tellus ultricies euismod sed vitae quam.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:14px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,Helvetica,sans\'; font-size:8pt; color:#000000;\">Nullam enim augue, sodales a urna eu, iaculis ultrices massa. Nulla iaculis quis nisi id eleifend. Donec ornare odio vel dolor tempor aliquam. Donec tincidunt nibh in porta tempor. In hac habitasse platea dictumst. Praesent suscipit erat sed sollicitudin vestibulum. Suspendisse potenti. Nullam bibendum eros sem, non rutrum mauris ultricies ut.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:14px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,Helvetica,sans\'; font-size:8pt; color:#000000;\">Curabitur vel porttitor turpis, et volutpat neque. Sed et sem dictum, euismod lectus nec, iaculis metus. Duis vestibulum egestas velit, sit amet porttitor neque vehicula at. Ut pharetra porta sem a pharetra. Phasellus congue mauris nec lectus lobortis aliquam. Curabitur augue lacus, porta at imperdiet ac, lobortis non tellus. Donec rutrum dui ac tellus posuere, ac aliquam magna sollicitudin. Praesent porta ligula at turpis aliquet, sed sagittis enim suscipit. Fusce ultrices iaculis libero, id tempor est laoreet sed. Nulla elit justo, rhoncus at tempus et, vehicula sed purus. Vivamus aliquet imperdiet blandit. Suspendisse neque sapien, volutpat eu ipsum tempor, varius fringilla elit. Quisque gravida nibh et erat pellentesque, ut commodo lectus posuere.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:14px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,Helvetica,sans\'; font-size:8pt; color:#000000;\">Sed semper convallis gravida. In hac habitasse platea dictumst. Nam eget vehicula urna. Suspendisse rhoncus lobortis mauris, non volutpat nibh volutpat id. Morbi ut rhoncus felis. Sed feugiat vitae augue non mattis. Donec a blandit neque, vel sodales orci. Duis quis nibh gravida, convallis magna a, scelerisque justo.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:14px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial,Helvetica,sans\'; font-size:8pt; color:#000000;\">Ut sodales diam a neque molestie rhoncus. Suspendisse potenti. Curabitur dictum nisl sed tortor tempor, eu vehicula nisl volutpat. Nam sem turpis, lacinia nec ornare at, adipiscing at magna. Aliquam eu ullamcorper risus. Praesent tempor ligula at sollicitudin consectetur. Nulla facilisi. Suspendisse non viverra urna. Duis sit amet tristique leo. Mauris iaculis interdum mattis. Aliquam erat volutpat. Etiam malesuada nulla ipsum, in gravida leo iaculis sed. Donec hendrerit tempor congue.</span></p></body></html>", None))
        self.pushButton.setText(_translate("Dialog", "Close", None))
