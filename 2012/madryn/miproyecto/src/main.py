'''
Created on 18/10/2012

@author: Diego
'''
from PyQt4.QtGui import QApplication
from ui.ventana import MiVentana
import sys

def main():
    app = QApplication(sys.argv)
    win = MiVentana()
    win.show()
    app.exec_()
    
    
if __name__ == '__main__':
    main()
