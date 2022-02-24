import sys

from PyQt5 import uic, QtWidgets, QtGui

qtCreatorFile = "P5_CambioColoresBoton.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btn_accion.clicked.connect(self.accion)

        self.valR = 240
        self.valG = 255
        self.valB = 120

    def obtieneColores(self):
        self.valR = self.txt_R.text()
        self.valG = self.txt_G.text()
        self.valB = self.txt_B.text()

    def accion(self):
        self.obtieneColores()
        print(self.valR, " ", self.valG, " ", self.valB)

        try:

            comando = "background-color:rgb(" \
                      + str(self.valR) + "," \
                      + str(self.valG) + "," \
                      + str(self.valB) + ");"
            self.ObjetoCambiaColor.setStyleSheet(comando)
        except Exception as ex:
            print(ex)

    def msj(self, text):
        m = QtWidgets.QMessageBox()
        m.setText(text)
        m.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

