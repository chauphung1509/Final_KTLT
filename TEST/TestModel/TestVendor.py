from LIBRARY.JsonFileFactory import JsonFileFactory
from MODELS.Vendor import Vendor

jff=JsonFileFactory()
filename="../testModel/vendors.json"
vendor=jff.read_data(filename,Vendor)
for i in vendor:
    print(i)