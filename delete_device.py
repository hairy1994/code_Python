import requests
import json
import sys
from tabulate import tabulate

import pgpd
import get_network_device

#Lay danh sach cac thiet bi
result = get_network_device.network_device_list()
print(tabulate(result,
            headers = ['number','hostname','ip','type','mac address','id'], tablefmt="rst"))
#####################################
def get_device_id():
    inputString= input("Nhap so thu tu cua thiet bi can xoa:")
    number=0
    device =[]
    resp = pgpd.get(api="network-device")
    response_json = resp.json() 
    device = response_json["response"]
    for item in device:
        number +=1
        if number==int(inputString):
            id_selete= item["id"]
    return id_selete
#Xoa thiet bi
def delete_device():
    id=get_device_id()
    try:
        resp = pgpd.delete(api="network-device/"+id)
        status = resp.status_code
        response_json = resp.json()
        r = response_json["response"]
        print(r)
    except:
        print("Something wrong")
        sys.exit()

result2 = delete_device()
