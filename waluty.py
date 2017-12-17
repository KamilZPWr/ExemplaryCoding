#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_waluty import Ui_MainWindow
from core_waluty import CurrencyConverter

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
   
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    def btn_click():
        toConvert = window.valueToConvert.value()
        currencySymbol = window.currency.text()
        rate = CurrencyConverter.getValue(currencySymbol)
        if rate==None:
            window.statusbar.showMessage("Błąd w pobieraniu kursu!")
            window.currencyRate.setText("")
            window.convertedValue.setText("")
        else:
            window.currencyRate.setText(str(rate))
            window.convertedValue.setText(str(rate * toConvert))
            window.statusbar.showMessage("OK")
    window.calculate.clicked.connect(btn_click)
    sys.exit(app.exec_())
	
