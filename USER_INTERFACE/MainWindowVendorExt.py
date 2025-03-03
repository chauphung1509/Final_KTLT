from PyQt6.QtWidgets import QMainWindow
from USER_INTERFACE.DEFAULT.MainWindowVendor import Ui_MainWindowVendor

class MainWindowVendorExt(QMainWindow, Ui_MainWindowVendor):
    def __init__(self, parent=None):  # Nhận parent để quay lại
        super().__init__()
        self.setupUi(self)
        self.parent_window = parent  # Lưu tham chiếu đến cửa sổ Admin
        self.setupSignalAndSlot()

    def setupSignalAndSlot(self):
        pass
    def showWindow(self):
        self.show()  # Hiển thị cửa sổ Vendor
