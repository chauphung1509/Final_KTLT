from USER_INTERFACE.Login.MainWindowSignup import Ui_Signup


class MainWindowSignupExt(Ui_Signup):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        pass