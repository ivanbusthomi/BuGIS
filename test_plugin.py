# -*- coding: utf-8 -*-
"""
/***************************************************************************
 testPlugin
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
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from test_plugin_dialog import testPluginDialog, help_testPluginDialog
import testPlugin_gui
import os.path


class testPlugin:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'testPlugin_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = testPluginDialog()


        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&Test Plugin')
        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar(u'testPlugin')
        self.toolbar.setObjectName(u'testPlugin')

        #-----------------------------------------------------add layer list in table of content to comboBox
        layers = QgsMapLayerRegistry.instance().mapLayers().values()
        for layer in layers:
            if layer.type() == QgsMapLayer.VectorLayer and layer.geometryType() == 1:
                self.dlg.comboInputA.addItem( layer.name(),layer)
                self.dlg.comboInputB.addItem( layer.name(),layer)

        #QObject.connect(self.dlg.comboInputA, SIGNAL("currentIndexChanged(int)"),self.inputShpA)
        #QObject.connect(self.dlg.comboInputB, SIGNAL("currentIndexChanged(int)"),self.inputShpB)





    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('testPlugin', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/testPlugin/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'test plugin'),
            callback=self.run,
            parent=self.iface.mainWindow())


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&Test Plugin'),
                action)
            self.iface.removeToolBarIcon(action)

    '''def inputShpA(self):                                       #----------------- this line of code need to be concerned
        index = self.dlg.comboInputA.currentIndex()
        layerA = self.dlg.comboInputA.itemData(index)
        return layerA


    def inputShpB(self):
        index = self.dlg.comboInputB.currentIndex()
        layerB = self.dlg.comboInputB.itemData(index)
        return layerB                                          #--------------------------------------------------------
    '''
    def run(self):
        """Run method that performs all the real work"""
        self.dlg.show()                                                                             # show the dialog
        QObject.connect(self.dlg.pushButton_3, SIGNAL("clicked()"), self.showhelp)                  # call the show help dialog function
        # Run the dialog event loop
        #result = self.dlg.exec_()
        # See if OK was pressed
        #if result:
            # Do something useful here - delete the line containing pass and
            # substitute with your code.
        #    pass

        #layers = QgsMapLayerRegistry.instance().mapLayers().values()
        #for layer in layers:
        #    if layer.type() == QgsMapLayer.VectorLayer and layer.geometryType() == QGis.Line:
        #        self.dlg.ui.layerCombo.addItem( layer.name(), layer )

    def showhelp(self):
        """ fungsi untuk menampilkan kotak dialog help"""
        self.hdlg = help_testPluginDialog()
        self.hdlg.show()
