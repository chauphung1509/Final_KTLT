from PyQt6.QtWidgets import QMainWindow, QApplication

from USER_INTERFACE.Admin.MainWindowAdminExt import MainWindowAdminExt
app=QApplication([])
mainwindow=QMainWindow()
myui=MainWindowAdminExt()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()