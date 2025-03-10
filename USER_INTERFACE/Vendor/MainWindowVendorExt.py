from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem

from LIBRARY.DataConnector import DataConnector
from MODELS.Vendor import Vendor
from USER_INTERFACE.Vendor.MainWindowAddVendorExt import MainWindowAddVendorExt
from USER_INTERFACE.Vendor.MainWindowEditVendorExt import MainWindowEditVendorExt
from USER_INTERFACE.Vendor.MainWindowVendor import Ui_MainWindowVendor

class MainWindowVendorExt(QMainWindow, Ui_MainWindowVendor):
    def __init__(self, parent=None):  # Nhận parent để quay lại
        self.dc=DataConnector()
        self.vendors=self.dc.get_all_vendors()
        self.selected_vendor = None
        super().__init__()
        self.setupUi(self)
        self.parent_window = parent  # Lưu tham chiếu đến cửa sổ Admin
        self.setupSignalAndSlot()
        self.show_vendors_on_gui()

    def setupSignalAndSlot(self):
#        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.pushButtonNew.clicked.connect(self.openNew)
        self.pushButtonEdit.clicked.connect(self.openEdit)
        self.pushButtonDelete.clicked.connect(self.process_Delete) #cho 1 function delete
#        self.tableWidget.itemSelectionChanged.connect(self.process_selected_vendor) #cho 1 function delete
        self.pushButton.clicked.connect(self.process_find)
    def showWindow(self):
        self.show()  # Hiển thị cửa sổ Vendor
    def openNew(self):
        self.add_vendor=MainWindowAddVendorExt()
        self.add_vendor.show()
        self.close()
    def openEdit(self):
        self.edit_vendor=MainWindowEditVendorExt()
        self.edit_vendor.show()
        self.close()
    def show_vendors_on_gui(self):
        self.tableWidget.setRowCount(0)
        for vendor in self.vendors:
            row=self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            col_id=QTableWidgetItem(vendor.vendor_number)
            col_name=QTableWidgetItem(vendor.name)
            col_address=QTableWidgetItem(vendor.address)
            col_phone=QTableWidgetItem(vendor.contact_number)
            col_email=QTableWidgetItem(vendor.email)
            self.tableWidget.setItem(row,0,col_id)
            self.tableWidget.setItem(row, 1, col_name)
            self.tableWidget.setItem(row, 2, col_address)
            self.tableWidget.setItem(row, 3, col_phone)
            self.tableWidget.setItem(row, 4, col_email)
    def process_Delete(self):# khong chay duoc vao day duoc
        print("aaaa")
#        index = self.selected_vendor
        index=self.tableWidget.currentRow()
        if index < 0 or index >= len(self.vendors):
            return  # Nếu chưa chọn hoặc chỉ số không hợp lệ, thoát hàm
        print(f"Xoá vendor: {self.vendors[index]}")
        # Xóa vendor khỏi danh sách
        self.vendors.pop(index)
        # Cập nhật lại table widget
        self.show_vendors_on_gui()
        ''' def process_selected_vendor(self):
        print("aaa")
        index=self.tableWidget.currentRow()
        self.selected_vendor=self.vendors[index]
        #self.selected_vendor=index
        print(f"{self.selected_vendor}")'''
    def process_find(self):
        if self.comboBox.text()=="All":
            #load het tat ca kia:
            self.show_vendors_on_gui()
            pass
        elif self.comboBox.text()=="Vendor ID":
            #load het cac co id giong vay
            vendor_id=self.lineEdit.text()
            for vendor in self.vendors:
                if vendor.vendor_number==vendor_id:
                    self.vendors=self.dc.get_vendor_by_id(vendor_id)
                else:
                    return
            self.show_vendors_on_gui()

            pass
        elif self.comboBox.text()=="Name":
            #load cac co name giong vay
            vendor_name=self.lineEdit.text()
            for vendor in self.vendors:
                if vendor.name==vendor_name:
                    self.vendors=self.dc.get_vendor_by_name(vendor_name)
                else:
                    return
            self.show_vendors_on_gui()
            pass


