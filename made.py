# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources
import locale
locale.setlocale(locale.LC_ALL, '')
# Import the code for the dialog
from dalacalcdialog import DalaCalcDialog


class DalaCalc:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # menambahkan variable global untuk daftar layer
        self.layerids = []
        # initialize plugin directory
        self.plugin_dir = QFileInfo(QgsApplication.qgisUserDbFilePath()).path() + "/python/plugins/dalacalc"
        # initialize locale
        localePath = ""
        locale = QSettings().value("locale/userLocale").toString()[0:2]

        if QFileInfo(self.plugin_dir).exists():
            localePath = self.plugin_dir + "/i18n/dalacalc_" + locale + ".qm"

        if QFileInfo(localePath).exists():
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        # self.dlg = DalaCalcDialog(self.iface.mainWindow(), flags)

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(QIcon(":/plugins/dalacalc/icon.png"),"Hitung Dala", self.iface.mainWindow())
        self.action.setWhatsThis("Plugin untuk hitungan Kerusakan dan Kerugian")
        self.action.setStatusTip("Damages And Losses Plugin")
        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&Hitungan Kerusakan Kerugian", self.action)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&Hitungan Kerusakan Kerugian", self.action)
        self.iface.removeToolBarIcon(self.action)

    # run method that performs all the real work
    def run(self):

        # create and show the dialog
        flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint
        self.dlg = DalaCalcDialog(self.iface.mainWindow(), flags)
        # show the dialog
        self.dlg.show()
        # koneksi signal
        QObject.connect(self.dlg.ui.KeterdampakanComboBox,SIGNAL('currentIndexChanged(int)'), self.bacaKeterdampakan)
        QObject.connect(self.dlg.ui.BahayaComboBox,SIGNAL('currentIndexChanged(int)'), self.bacaBahaya)
        #QObject.connect(self.dlg.ui.KerugianLineEdit,SIGNAL('currentIndexChanged(int)'), self.bacaKerugian)
        QObject.connect(self.dlg.ui.helpPushButton,SIGNAL('clicked()'), self.bantuan)
        QObject.connect(self.dlg.ui.hitungPushButton,SIGNAL('clicked()'), self.hitungDala)
        quitbutton = self.dlg.ui.closePushButton
        QObject.connect(quitbutton, SIGNAL('clicked()'), self.dlg, SLOT('close()'))

        # membuat daftar layer yang ada di qgis
        self.layermap=QgsMapLayerRegistry.instance().mapLayers()
        for (name,layer) in self.layermap.iteritems():
            if type(layer).__name__ == "QgsVectorLayer":
                tempname = str(name).rstrip('01234567890')
                self.layerids.append(name)
                self.dlg.ui.KeterdampakanComboBox.addItem(tempname)
                self.dlg.ui.BahayaComboBox.addItem(tempname)

    def bacaKeterdampakan(self):
		# membaca layer yg akan digunakan sebagai keterdampakan
        try:
            comboindex = self.dlg.ui.KeterdampakanComboBox.currentIndex()
            layerKeterdampakan = self.layermap[self.layerids[comboindex]]
        except: #Crashes without valid shapefiles
            return


    def bacaBahaya(self):
        # membaca layer yg akan digunakan sebagai exposure
        try:
            comboindex = self.dlg.ui.BahayaComboBox.currentIndex()
            layerBahaya = self.layermap[self.layerids[comboindex]]
        except: #Crashes without valid shapefiles
            return

    def bantuan(self):
		# membaca menu bantuan
        QMessageBox.information(self.iface.mainWindow(),"Bantuan Dala","Hitungan kerugian disesuaikan dengan peraturan daerah yang berlaku, dan diasumsikan kerusakan sebesar 90 %", QMessageBox.Close)


    def hitungDala(self):
        # membaca isi nilai kerugian - menguji isinya apakah yang dimasukkan benar merupakan angka
        try:
            nilaiKerugian = self.dlg.ui.KerugianLineEdit.text()
            nilaiKerugian = float(nilaiKerugian)
        except ValueError:
            QMessageBox.warning(self.iface.mainWindow(),"Error","Nilai kerugian tidak boleh kosong dan harus berupa angka!", QMessageBox.Close)
            return

        # membaca layer exposure
        comboindex = self.dlg.ui.KeterdampakanComboBox.currentIndex()
        layerKeterdampakan = self.layermap[self.layerids[comboindex]]

        # membaca layer hazard
        comboindex = self.dlg.ui.BahayaComboBox.currentIndex()
        layerBahaya = self.layermap[self.layerids[comboindex]]
        # check apakah layer sudah bener masuk
        #QMessageBox.information(self.iface.mainWindow(),"Error","terdampak = "+str(layerKeterdampakan)+"\nBahaya = "+str(layerBahaya), QMessageBox.Close)

        # membuat spatial index untuk mempercepat proses
        dampakIndex = QgsSpatialIndex()   #index kosong untuk menampung layer dengan jumlah feature banyak
        bahayaIndex = QgsSpatialIndex()

        fbahaya = QgsFeature()    #variabel untuk menyimpan feature pada layer bahaya
        fdampak = QgsFeature()    #variabel untuk menyimpan feature pada layer dampak

        # dampak - buat penyimpanan feature menggunakan spatial index
        allAttrsDampak = layerKeterdampakan.pendingAllAttributesList()
        layerKeterdampakan.select(allAttrsDampak)
        allFeaturesDampak = {fdampak.id(): fdampak for fdampak in layerKeterdampakan}

        # bahaya - buat penyimpanan feature menggunakan spatial index
        allAttrsBahaya = layerBahaya.pendingAllAttributesList()
        layerBahaya.select(allAttrsBahaya)
        allFeaturesBahaya = {fbahaya.id(): fbahaya for fbahaya in layerBahaya}

        #mengisi dictionary dengan data keterdampakan
        for fd in allFeaturesDampak.values():
            dampakIndex.insertFeature(fd)

        #mengisi dictionary dengan data bahaya
        for fb in allFeaturesBahaya.values():
            bahayaIndex.insertFeature(fb)


        # --- MAIN ITERATION ---

        ids_D = {}
        ids_B = {}
        luasAkhirTerdampak = 0

        # loop untuk mengisi feature di layer dampak dengan spatial indexnya
        for fdampak in allFeaturesDampak.values():
            varA = fdampak.id()
            ids_D[varA] = dampakIndex.intersects(fdampak.geometry().boundingBox())
            #QMessageBox.information(self.iface.mainWindow(),"test", str(varA),QMessageBox.Close)

        # loop untuk mengisi feature di layer bahaya dengan spatial indexnya
        for fbahaya in allFeaturesBahaya.values():
            varB = fbahaya.id()
            ids_B[varB] = bahayaIndex.intersects(fbahaya.geometry().boundingBox())
            #QMessageBox.information(self.iface.mainWindow(),"test", str(varB),QMessageBox.Close)


        selection=[]
		# seleksi fitur yang terseleksi
        for id_D in ids_D:
            f_D = allFeaturesDampak[id_D]
            for id_B in ids_B:
                f_B = allFeaturesBahaya[id_B]
                intersct = f_D.geometry().intersects(f_B.geometry())
                #QMessageBox.information(self.iface.mainWindow(),"test1", "intersect pa gak?"+str(intersct),QMessageBox.Close)
                if intersct == True:
                    luasTerdampak = f_D.geometry().area()
                    luasAkhirTerdampak += luasTerdampak
                    selection.append(id_D)   # mendaftar feature yang terseleksi
                else:
                    pass

        layerKeterdampakan.setSelectedFeatures(selection)

        if varA == 1:
            self.zoomFeature()
        else:
            mc=self.iface.mapCanvas()
            mc.zoomToSelected(layerKeterdampakan)

        # menghitung perkalian antara nilai kerugian dengan luas area terdampak
        persentase = 90.0*(0.01)
        hasilKali = luasAkhirTerdampak * nilaiKerugian * persentase
        # menampilkan hasil
        stringHasil = ("Hasil analisis kerugian dan kerusakan: \n"
                        "\n- Total jumlah fasilitas terdampak      = "+str(len(selection))+
                        "\n- Total luas semua fasilitas terdampak  "
                        "\n   = "+str(luasAkhirTerdampak)+ " m2"
                        "\n- Dengan nilai kerugian per unit sebesar "
                        "\n      Rp. "+locale.format("%d",nilaiKerugian,grouping=True)+",- "
                        "\n dan dengan asumsi bahwa bangunan yang rusak "
                        "\n mengalami "+str(persentase*100)+"% kerusakan, diperoleh bahwa"
                        "\nNilai total kerugian = "
                        "\n      Rp. "+locale.format("%d",hasilKali,grouping=True)+",-")

        QMessageBox.information(self.iface.mainWindow(),"Hasil Hitungan", stringHasil, QMessageBox.Close)


    def zoomFeature(self):
        #Kalau hanya satu feature yang terpilih, zoom ke feature tersebut.

        try:
            comboindex = self.dlg.ui.KeterdampakanComboBox.currentIndex()
            layerKeterdampakan = self.layermap[self.layerids[comboindex]]

            rect = QgsRectangle(layerKeterdampakan.boundingBoxOfSelected())
            rect.setXMaximum(rect.xMaximum() + .5)
            rect.setXMinimum(rect.xMinimum() - .5)
            rect.setYMaximum(rect.yMaximum() + .5)
            rect.setYMinimum(rect.yMinimum() - .5)

            number = float(self.dlg.ui.scaleSpin.value())
            mc=self.iface.mapCanvas()

            #If the screen is longer than it is tall, scale based on width
            if mc.extent().height() > mc.extent().width():
                scalefactor = (mc.extent().width() / mc.scale())
            else: #otherwise use height
                scalefactor = (mc.extent().height() / mc.scale())
            rect.scale(number * scalefactor)
            mc.setExtent(rect)
            mc.refresh()
        #scalefactor = number / mc.scale()
        #mc.zoomByFactor(scalefactor)
        except:
            print "Tidak ada feature yang terseleksi"
