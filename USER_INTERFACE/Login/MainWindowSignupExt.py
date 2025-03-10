from PyQt6.QtWidgets import QMainWindow

from MODELS.Admin import Staff
from USER_INTERFACE.Login.MainWindowLoginExt import MainWindowLoginExt
from USER_INTERFACE.Login.MainWindowSignup import Ui_Signup


class MainWindowSignupExt(Ui_Signup):
    def setupUi(self,MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonCreate.clicked.connect(self.process_create)
        self.pushButtonCancel.clicked.connect(self.process_cancel)
        self.pushButtonClear.clicked.connect(self.process_clear)
    def process_create(self):
        staff_id = self.lineEditStaffID.text()
        name = self.lineEditName.text()
        position=self.lineEditPosition.text()
        phone=str(self.lineEditPhone.text())
        email=str(self.lineEditEmail.text())
        username=str(self.lineEditUsername.text())
        pword=str(self.lineEditPassword.text())
        user = Staff(staff_id, name, position, phone, email)
        self.listofstaff.append(user) #cái nì mốt có staff dataset thì fix sau
        #cần lưu lại cơ sở dữ liệu:
        '''jff = JsonFileFactory()
        filename = "../dataset/assets.json"
        jff.write_data(self.listofstaff, filename)'''
        #cái này ai viết lại dùm để nó lưu vào file excel dataset với ạaa
    def process_clear(self):
        self.lineEditStaffID.clear()
        self.lineEditName.clear()
        self.lineEditPosition.clear()
        self.lineEditPhone.clear()
        self.lineEditEmail.clear()
        self.lineEditUsername.clear()
        self.lineEditPassword.clear()
        self.lineEditPasswordagain.clear()
        self.lineEditStaffID.setFocus()

    def process_cancel(self):
        from USER_INTERFACE.Login.MainWindowLoginExt import MainWindowLoginExt
        self.MainWindow.close()
        self.mainwindow = QMainWindow()
        self.myui = MainWindowLoginExt()
        self.myui.setupUi(self.mainwindow)
        self.myui.showWindow()

    '''def process_cancel(self):
        # Đóng cửa sổ hiện tại và gọi phương thức để hiển thị lại cửa sổ đăng nhập
        self.MainWindow.close()  # Đóng cửa sổ Create Account
        self.open_login_window()

    def open_login_window(self):
        # Mở cửa sổ đăng nhập
        login_window = MainWindowLoginExt()  # Tạo mới đối tượng Login Window
        login_window.showWindow() '''

    #button Cancel vẫn đang lỗi, KC sẽ ráng fix sauu nhe