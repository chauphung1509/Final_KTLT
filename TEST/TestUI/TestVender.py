from PyQt6.QtWidgets import QApplication, QMainWindow

from USER_INTERFACE.Vendor.MainWindowVendorExt import MainWindowVendorExt

app=QApplication([])
mainwindow=QMainWindow()
myui=MainWindowVendorExt()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()
