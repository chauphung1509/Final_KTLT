from PyQt6.QtWidgets import QMainWindow

from MODELS.Admin import Staff
from USER_INTERFACE.MainWindowAddAmin import Ui_MainWindowAddAdmin


class MainWindowAddAdminExt(QMainWindow, Ui_MainWindowAddAdmin):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupSignalAndSlot()
        self.a = Staff()
        self.admins = []

    def setupSignalAndSlot(self):
        self.pushButtonSave.clicked.connect(self.process_save)
        self.pushButtonCancel.clicked.connect(self.process_cancel)
    def process_save(self):
        adid = self.lineEditStaffID.text()
        adname = self.lineEditName.text()
        adpos = self.lineEditPosition.text()
        adphone = self.lineEditPhone.text()
        ademail = self.lineEditEmail.text()
        a = Staff(adid,adname,adpos,adphone,ademail)
        self.admins.append(a)
        self.clear_layout()

    def clear_layout(self):
        self.lineEditStaffID.setText("")
        self.lineEditName.setText("")
        self.lineEditPosition.setText("")
        self.lineEditPhone.setText("")
        self.lineEditEmail.setText("")
        self.lineEditStaffID.setFocus()

    def process_cancel(self):
        self.close()
    def showWindow(self):
        self.show()  # Hiển thị cửa sổ
