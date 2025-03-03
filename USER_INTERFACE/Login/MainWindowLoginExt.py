from PyQt6.QtWidgets import QMainWindow, QMessageBox

from LIBRARY.DataConnector import DataConnector
from USER_INTERFACE.Login.MainWindowLogin import Ui_Login
from USER_INTERFACE.Login.MainWindowSignupExt import MainWindowSignupExt
from USER_INTERFACE.Product.MainWindowProductExt import MainWindowProductExt


class MainWindowLoginExt(Ui_Login):

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonLogin.clicked.connect(self.process_login)
        self.pushButtonLogin_2.clicked.connect(self.process_create_account)
    def process_login(self):
        dc=DataConnector()
        uid = self.lineEditUsername.text()
        pwd = self.lineEditPassword.text()
        emp = dc.login(uid, pwd)
        if emp != None:
            self.MainWindow.close()#close login window
            self.mainwindow = QMainWindow()
            self.myui = MainWindowProductExt()
            self.myui.setupUi(self.mainwindow)
            self.myui.showWindow()
        else:
            self.msg = QMessageBox(self.MainWindow)
            self.msg.setText("Đăng nhập thất bại")
            self.msg.exec()
    def process_create_account(self):
        self.MainWindow.close()
        self.mainwindow=QMainWindow()
        self.myui=MainWindowSignupExt()
        self.myui.setupUi(self.mainwindow)
        self.myui.showWindow()
        #khi bấm create account thì nó chuyển qua trang create account thành công rùi



