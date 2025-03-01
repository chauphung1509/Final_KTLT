from USER_INTERFACE.MainWindowLogin import Ui_Login


class MainWindowLoginExt(Ui_Login):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow

    def showWindow(self):
        self.MainWindow.show()
