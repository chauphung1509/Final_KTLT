from USER_INTERFACE.MainWindowAdmin import Ui_MainWindow


class MainWindowAdminExt(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow

    def showWindow(self):
        self.MainWindow.show()
