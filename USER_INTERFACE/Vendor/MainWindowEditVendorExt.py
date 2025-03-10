from PyQt6.QtWidgets import QMainWindow

from MODELS.Vendor import Vendor
from USER_INTERFACE.Vendor.MainWindowEditVendor import Ui_MainWindowAddAdmin



class MainWindowEditVendorExt(QMainWindow,Ui_MainWindowAddAdmin):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupSignalAndSlot()
        self.list=[]
    def showWindow(self):
        self.show()
    def setupSignalAndSlot(self):
        self.pushButtonSave.clicked.connect(self.process_save)
        self.pushButtonCancel.clicked.connect(self.process_cancel)
    def process_save(self):
        vendor_id = self.lineEditVendorID.text()
        vendor_name = self.lineEditName.text()
        vendor_email = self.lineEditEmail.text()
        vendor_address = self.lineEditAddress.text()
        vendor_phone = self.lineEditPhone.text()
        vendor_edited=Vendor(vendor_id,vendor_name,vendor_phone,vendor_address,vendor_email)
        for i in range(len(self.list)):
            vendor=self.list[i]
            if vendor.vendor_number==vendor_edited.vendor_id:
                self.list[i]=vendor_edited
                break
        from USER_INTERFACE.Vendor.MainWindowVendorExt import MainWindowVendorExt
        self.parent=MainWindowVendorExt()
        self.parent.show()
        self.close()

    def process_cancel(self):
        self.close()
        from USER_INTERFACE.Vendor.MainWindowVendorExt import MainWindowVendorExt
        self.parent = MainWindowVendorExt()
        self.parent.show()
        self.close()



