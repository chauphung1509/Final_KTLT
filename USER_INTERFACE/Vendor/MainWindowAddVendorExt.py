from PyQt6.QtWidgets import QMainWindow

from MODELS.Vendor import Vendor
from USER_INTERFACE.Vendor.MainWindowAddVendor import Ui_MainWindowAddAdmin



class MainWindowAddVendorExt(QMainWindow,Ui_MainWindowAddAdmin):
#### them moi o day parent 1
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupSignalAndSlot()
    # o day se goi list vendor len1
        self.list=[]
    def showWindow(self):
        self.show()
    def setupSignalAndSlot(self):
        self.pushButtonSave.clicked.connect(self.process_save)
        self.pushButtonCancel.clicked.connect(self.process_cancel)
    def process_save(self):
        vendor_id=self.lineEditVendorID.text()
        vendor_name=self.lineEditName.text()
        vendor_email=self.lineEditEmail.text()
        vendor_address=self.lineEditAddress.text()
        vendor_phone=self.lineEditPhone.text()
        new_vendor=Vendor(vendor_id,vendor_name,vendor_phone,vendor_address,vendor_email)
        self.list.append(new_vendor)
        #luu lai xuong bo nho 2
        #mo lai vendorwindow
        from USER_INTERFACE.Vendor.MainWindowVendorExt import MainWindowVendorExt
        self.parent=MainWindowVendorExt()
        self.parent.show()
        self.close()

# them o day parent 2
    def process_cancel(self):
        self.close()
        from USER_INTERFACE.Vendor.MainWindowVendorExt import MainWindowVendorExt
        self.parent = MainWindowVendorExt()
        self.parent.show()
        self.close()
