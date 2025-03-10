import pandas as pd

from LIBRARY.JsonFileFactory import JsonFileFactory
from MODELS.Admin import Staff
from MODELS.Vendor import Vendor


class DataConnector:
    def get_all_staff(self):
        filename = "../dataset/staffs.xlsx"
        df = pd.read_excel(filename)

        listofstaff = []
        for _, row in df.iterrows():
            staff = Staff(row['UserName'], row['Password'])
            listofstaff.append(staff)
        return listofstaff

    def login(self, username, password):
        listofstaff = self.get_all_staff()
        if username in self.valid_accounts and self.valid_accounts[username] == password:
            print("Đăng nhập thành công!")
            return True
        else:
            print("Sai tên đăng nhập hoặc mật khẩu.")
            return False

#ê nha nó đang hơi lộn xộn
    def get_all_vendors(self):
        jff=JsonFileFactory()
        filename="../testModel/vendors.json"
        vendors=jff.read_data(filename,Vendor)
        return vendors
    