import pandas as pd

from MODELS.Admin import Staff


class DataConnector:
    def get_all_staff(self):
        filename = "../dataset/employees.xlsx"
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