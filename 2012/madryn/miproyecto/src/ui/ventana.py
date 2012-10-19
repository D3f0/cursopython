
# encoding: utf-8
'''
Created on 18/10/2012

@author: Diego
'''


from PyQt4.QtGui import  *
from PyQt4.QtSql import *
from ui_ventana import Ui_MainWindow
import os

class MiVentana(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MiVentana, self).__init__()
        self.setupUi(self)
        self.connectSignals()
        
        self.setupTablaDB()
    
    def connectSignals(self):
        self.actionArbir.triggered.connect(self.abrirArchivo)
        self.actionGuardar.triggered.connect(
                                             self.guardarArchivo
                                             )
        self.actionCerrar.triggered.connect(self.close)
        
        
    def abrirArchivo(self):
        f = QFileDialog.getOpenFileName(self, "Un archivo",
                                        "",
                                        "Archivos de texto (*.txt)")
        if os.path.exists(f):
            with open(f) as fp:
                self.textEdit.setPlainText(fp.read())
                
    
                
    def guardarArchivo(self):
        f = QFileDialog.getSaveFileName(self,
                                    "Guardar como",
                                    "",
                                    "Archivos de texto (*.txt);;"
                                    "Todos (*)")
        if f:
            with open(f, "w") as fp:
                fp.write(self.textEdit.toPlainText())
                self.statusbar.showMessage("Escribí %s" % f)
                
                
    def setupTablaDB(self):
        self.db = QSqlDatabase.addDatabase("QPSQL")
        self.db.setHostName("10.0.2.2");
        self.db.setDatabaseName("ipa");
        self.db.setUserName("postgres");
        #self.db.setPassword("J0a1m8");
        print self.db.open();
        self.modelo = QSqlTableModel(self, self.db)
        self.modelo.setTable('evarsa_medicion')
        self.modelo.select()
        self.modelo.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.tableView.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.tableView.setModel(self.modelo)
        
        
        