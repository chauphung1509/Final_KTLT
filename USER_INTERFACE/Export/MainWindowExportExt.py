from PyQt6.QtWidgets import QMainWindow

from USER_INTERFACE.Admin.MainWindowAddAdminExt import MainWindowAddAdminExt
from USER_INTERFACE.Admin.MainWindowAdminExt import MainWindowAdminExt
from USER_INTERFACE.Export.MainWindowExport import Ui_MainWindowExport
from USER_INTERFACE.Import.MainWindowImportExt import MainWindowImportExt
from USER_INTERFACE.Product.MainWindowProductExt import MainWindowProductExt
from USER_INTERFACE.Vendor.MainWindowVendorExt import MainWindowVendorExt

class MainWindowExportExt(QMainWindow, Ui_MainWindowExport):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupSignalAndSlot()
    def setupSignalAndSlot(self):
        # Kết nối sự kiện khi nhấn nút "pushButtonVendor"
        self.pushButtonVendor.clicked.connect(self.openVendor)
        self.pushButtonProduct.clicked.connect(self.openProduct)
        self.pushButtonAdmin.clicked.connect(self.openAdmin)
        self.pushButtonReceipt.clicked.connect(self.openGoodReceipt)
        self.pushButtonInvoice.clicked.connect(self.openGoodInvoice)
        self.pushButtonInventory.clicked.connect(self.openInventory)
        self.pushButtonStatistic.clicked.connect(self.openStatistic)
        self.pushButtonImport.clicked.connect(self.openImport)
        self.pushButtonExport.clicked.connect(self.openExport)

    def openAddNew(self):
        self.add_window = MainWindowAddAdminExt()  # Tạo cửa sổ Vendor
        self.add_window.show()


    # ----- KHỐI HÀM LIÊN KẾT MÀN HÌNH -----
    def openVendor(self):
        self.vendor_window = MainWindowVendorExt()  # Tạo cửa sổ Vendor
        self.vendor_window.show()  # Hiển thị cửa sổ Vendor
        self.close()  # Đóng cửa sổ hiện tại (Admin)
    def openProduct(self):
        self.product_window = MainWindowProductExt()
        self.product_window.show()
        self.close()
    def openAdmin(self):
        self.admin_window = MainWindowAdminExt()
        self.admin_window.show()
        self.close()
    def openInventory(self):
        self.invoice_window = MainWindowInventoryExt()
        self.invoice_window.show()
        self.close()
    def openGoodReceipt(self):
        self.receipt_window = MainWindowGoodReceiptExt()
        self.receipt_window.show()
        self.close()
    def openGoodInvoice(self):
        self.invoice_window = MainWindowGoodInvoiceExt()
        self.invoice_window.show()
        self.close()
    def openStatistic(self):
        self.stt_window = MainWindowStatisticExt()
        self.stt_window.show()
        self.close()
    def openImport(self):
        self.ip_window = MainWindowImportExt()
        self.ip_window.show()
        self.close()
    def openExport(self):
        self.ep_window = MainWindowExportExt()
        self.ep_window.show()
        self.close()
    def showWindow(self):
        self.show()  # Hiển thị cửa sổ Admin
