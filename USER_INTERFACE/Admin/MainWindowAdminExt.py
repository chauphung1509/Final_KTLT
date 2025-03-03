from PyQt6.QtWidgets import QMainWindow

from USER_INTERFACE.Admin.MainWindowAddAdminExt import MainWindowAddAdminExt
from USER_INTERFACE.Admin.MainWindowAdmin import Ui_MainWindow
from USER_INTERFACE.Vendor.MainWindowVendorExt import MainWindowVendorExt

class MainWindowAdminExt(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupSignalAndSlot()
    def setupSignalAndSlot(self):
        self.pushButtonVendor.clicked.connect(self.openVendor)
        self.pushButtonNew.clicked.connect(self.openAddNew)
        # Kết nối sự kiện khi nhấn nút "pushButtonVendor"
        self.pushButtonVendor.clicked.connect(self.openVendor)
    def openAddNew(self):
        self.add_window = MainWindowAddAdminExt()  # Tạo cửa sổ Vendor
        self.add_window.show()
    def openVendor(self):
        self.vendor_window = MainWindowVendorExt()  # Tạo cửa sổ Vendor
        self.vendor_window.show()  # Hiển thị cửa sổ Vendor
        self.close()  # Đóng cửa sổ hiện tại (Admin)

    def showWindow(self):
        self.show()  # Hiển thị cửa sổ Admin
