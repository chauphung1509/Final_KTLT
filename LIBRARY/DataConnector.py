from LIBRARY.JsonFileFactory import JsonFileFactory
from MODELS.Customer import Customer


class DataConnector:
    def get_all_customers(self):
        jff = JsonFileFactory()
        filename = "../dataset/employees.json" #chưa có
        customers = jff.read_data(filename, Customer)
        return customers

    def login(self,username,password):
        employees=self.get_all_customers()
        for e in employees:
            if e.UserName==username and e.Password==password:
                return e
        return None