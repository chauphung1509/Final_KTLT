from LIBRARY.JsonFileFactory import JsonFileFactory
from MODELS.Vendor import Vendor
import os
vendors=[]
v1=Vendor("V1","Vendor 1","Address 1","099119234","vendor1@gmail.com")
v2=Vendor("V2","Vendor 2","Address 2","098343623","vendor2@gmail.com")
v3=Vendor("V3","Vendor 3","Address 3","098372482","vendor3@gmail.com")
v=[v1,v2,v3]
vendors.extend(v)
jff=JsonFileFactory()
file_path = '../Dataset/vendors.json'
jff.write_data(vendors,file_path)