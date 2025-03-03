from PyQt6.QtWidgets import QMainWindow, QApplication

from USER_INTERFACE.HomeUi import homeUi
from USER_INTERFACE.MainWindowAdminExt import MainWindowAdminExt

app=QApplication([])
mainwindow = homeUi()
mainwindow.setupUi(mainwindow)  # Đảm bảo setupUi được gọi trên đúng đối tượng
mainwindow.showWindow()
app.exec()