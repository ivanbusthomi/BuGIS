# -*- coding: utf-8 -*-
"""
/***************************************************************************
 testPluginDialog
                                 A QGIS plugin
 testing plugin
                             -------------------
        begin                : 2014-07-05
        git sha              : $Format:%H$
        copyright            : (C) 2014 by private
        email                : testing@adasd.cosaf
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from qgis.core import *
import testPlugin_gui
import helpDialog
from test_plugin_library import lineToPoint,nextPoint




class testPluginDialog(QDialog,testPlugin_gui.Ui_Dialog):
    def __init__(self, parent=None):
        """Constructor."""
        super(testPluginDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect


        self.setupUi(self)

        # connect comboBox
        #QObject.connect(self.dlg.ui.KeterdampakanComboBox,SIGNAL('currentIndexChanged(int)'), self.bacaKeterdampakan)

        # connect browse button
        self.connect(self.browseButton, SIGNAL("clicked()"),self.browseOutfile)
        self.connect(self.pushButton_2, SIGNAL("clicked()"),self.runYouFools)

    def runYouFools(self):
        indexA= self.comboInputA.currentIndex()
        indexB= self.comboInputB.currentIndex()
        inputA= self.comboInputA.itemData(indexA)
        inputB= self.comboInputA.itemData(indexB)
        #intv =  str(self.doubleSpinBox.value())
        #nameA= unicode(inputA.name())
        #nameB= unicode(inputB.name())
        #self.textBrowser.append(nameA + " , " +nameB + " , " + intv)

        #convert line input to point layer
        pLayerA = lineToPoint(inputA,"A")
        pLayerB = lineToPoint(inputB,"B")
        threePointList=[]
        midPointList=[]
        #iteration ------------------------------------------>  check this section
        while startA!=endA and startB!=endB:
            m,n = nextPoint(startA,startB,100)                  # m= mid point, n = next point for iteration
            threePointList.append([startA,startB,n])
            midPointList.append(m)
            if n['ket']='A':        # <--- not sure if working.
                startA=n
            elif n['ket']='B':      # <--- not sure if working.
                startB=n
        #<----------------------------------------------------------

        # line_from_point with midPointList as input. output ed_line_v1

        # circumCenter function with threePointList as input. output cc_midPointList

        # line_from_point with cc_midPointList as input. output ed_line_v2

        # compare ver1 vs ver2


        #self.textBrowser.append(str(pLayerA) + " " + str(pLayerB))

    def browseOutfile(self):
        outName = QFileDialog.getSaveFileName(self, "Output Shapefile",self.lineInput.displayText(), "Shapefile (*.shp)")
        if outName != None:
           self.lineInput.setText(outName)

class help_testPluginDialog(QDialog,helpDialog.ui_helpDialog):
    def __init__(self, parent=None):
        """Constructor."""
        super(help_testPluginDialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect


        self.setupUi(self)