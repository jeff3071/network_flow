import socket
import requests
from bs4 import BeautifulSoup
import re

from datetime import datetime
import time

from pygame import mixer


def getflow(n):
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        localip = s.getsockname()[0]

        url = 'http://netflow.dorm.ccu.edu.tw/flows/' + str(localip)
#         url = 'http://netflow.dorm.ccu.edu.tw/flows/'+ '140.123.222.100'

        res = requests.get(url)
        soup = BeautifulSoup(res.content, 'html.parser')
        flow = soup.find('h3')

        dr = re.compile(r'<[^>]+>', re.S)
        dd = dr.sub('', str(flow))

        MB = re.sub("[^0-9 ^.]", "", dd)

    #     print(dd)
    #     print(float(MB))
        if float(MB) > 10000:
            print('流量警告 現有流量' + MB + 'MB')
            mixer.init()
            mixer.music.load('warning.mp3')
            mixer.music.play()
        else:
             print('現有流量' + MB + 'MB')

        s.close()
        time.sleep(n)


getflow(30)
