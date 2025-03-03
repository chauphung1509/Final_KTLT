from PyQt6.QtWidgets import QMainWindow, QApplication

from USER_INTERFACE.MainWindowLoginExt import MainWindowLoginExt

app=QApplication([])
mainwindow=QMainWindow()
myui=MainWindowLoginExt()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()