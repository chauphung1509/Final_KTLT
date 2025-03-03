from PyQt6.QtWidgets import QMainWindow

from USER_INTERFACE.MainWindowAddAdminExt import MainWindowAddAdminExt
from USER_INTERFACE.MainWindowAdmin import Ui_MainWindow
from USER_INTERFACE.MainWindowVendorExt import MainWindowVendorExt

class MainWindowAdminExt(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupSignalAndSlot()

        self.vendor_window = None  # Khởi tạo biến để lưu cửa sổ Vendor

    def setupSignalAndSlot(self):
        self.pushButtonVendor.clicked.connect(self.openVendor)
        self.pushButtonNew.clicked.connect(self.openAddNew)

    def openAddNew(self):
        self.add_window = MainWindowAddAdminExt()
        self.add_window.show()

    def openVendor(self):
        if self.vendor_window is None:  # Kiểm tra nếu cửa sổ Vendor chưa được tạo
            self.vendor_window = MainWindowVendorExt(self)  # Truyền self để có thể quay lại

        self.hide()  # Ẩn cửa sổ hiện tại thay vì đóng
        self.vendor_window.show()  # Hiển thị cửa sổ Vendor

    def showWindow(self):
        self.show()  # Hiển thị cửa sổ Admin