import requests
import time
from Params import Params, ReadParameters
import json
import tkinter as tk


class Update:
    def __init__(self):
        window = tk.Tk()
        with open('params.json', 'r') as f:
            a = json.load(f)
        par = Params('params.json')
        read_parameters = ReadParameters()
        read_parameters.read_params(par)
        # print(read_parameters.URL_var.get())
        self.url=read_parameters.URL_var.get()
        self.gateNo=read_parameters.GateNum_var.get()
        self.headers={'Content-Type': 'application/json'}
        self.key = "gateNo"
        # self.gateNo = "ZD101"
        self.passInfoNum = 1
        self.passtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        self.direction = "1"
        self.checkInfoType = "0"
        self.sign = "A96D48AE69F46BD0E1B17F10316086F3"
        self.timestamp = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        self.postdata = {self.key: self.gateNo, "passInfoNum": self.passInfoNum, "direction": self.direction,
                        "checkInfoType": self.checkInfoType, "sign": self.sign, "timestamp": self.timestamp}
        # self.url = "http://192.168.20.235:8321/updateGatePassInfoAction/updateGatePassInfo"

    def post_send(self):
        try:
            r = requests.post(url=self.url, data=json.dumps(self.postdata), headers=self.headers,timeout=2)
            print(r.text)
            if '"code":"200"' in r.text:
                return '1'
        except Exception as e:
            print(e)
            return '0'

if __name__ == '__main__':
    ud=Update()
    ud.post_send()
         
