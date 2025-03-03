from PyQt6.QtWidgets import QMainWindow, QApplication

from USER_INTERFACE.MainWindowAdminExt import MainWindowAdminExt

app=QApplication([])
mainwindow=QMainWindow()
myui=MainWindowAdminExt()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()