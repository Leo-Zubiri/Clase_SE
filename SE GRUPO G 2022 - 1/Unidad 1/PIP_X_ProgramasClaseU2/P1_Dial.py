import sys

from PyQt5 import uic, QtWidgets, QtGui

qtCreatorFile = "P1_Dial.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.dial.setMinimum(-10)
        self.dial.setMaximum(10)
        self.dial.setSingleStep(1)
        self.dial.setValue(0)

        self.dial.valueChanged.connect(self.cambiaValor)

        valor = self.dial.value()
        print(valor)
        self.txt_valor.setText(str(valor))

    def cambiaValor(self):
        valor = self.dial.value()
        print(valor)
        self.txt_valor.setText(str(valor))


    def msj(self, text):
        m = QtWidgets.QMessageBox()
        m.setText(text)
        m.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

