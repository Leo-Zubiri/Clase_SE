import sys

from PyQt5 import uic, QtWidgets, QtGui

qtCreatorFile = "P2_Sliders.ui"  # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.horizontalSlider.setMinimum(-10)
        self.horizontalSlider.setMaximum(10)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setValue(0)

        self.horizontalSlider.valueChanged.connect(self.cambiaValorHS)

        valor = self.horizontalSlider.value()
        print(valor)
        self.txt_valor.setText(str(valor))

        ######################################################################

        self.verticalSlider.setMinimum(-10)
        self.verticalSlider.setMaximum(10)
        self.verticalSlider.setSingleStep(1)
        self.verticalSlider.setValue(0)

        self.verticalSlider.valueChanged.connect(self.cambiaValorVS)

        valor2 = self.verticalSlider.value()
        print(valor2)
        self.txt_valor_2.setText(str(valor2))

    def cambiaValorHS(self):
        valor = self.horizontalSlider.value()
        print(valor)
        self.txt_valor.setText(str(valor))

    def cambiaValorVS(self):
        valor2 = self.verticalSlider.value()
        print(valor2)
        self.txt_valor_2.setText(str(valor2))


    def msj(self, text):
        m = QtWidgets.QMessageBox()
        m.setText(text)
        m.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

