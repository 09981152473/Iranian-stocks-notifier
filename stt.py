#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib3
import urllib
from datetime import datetime
import time
import winsound
import logging
from settings import *
from pytz import timezone



sound_file_name = "tm4.wav"
tehran = timezone('Asia/Tehran')
statTime = datetime.now(tehran).replace(hour=8, minute=30, second=0, microsecond=0)
finishTime = datetime.now(tehran).replace(hour=12, minute=30, second=1, microsecond=0)

def send_notification(stockname, message):
    if sendSmsEnable:
        sendTextMessage(stockname, message)
    playSound(stockname)


def buy_price_queu_is_less_than(stockobj, desire):
    if int(stockobj.buy_top_price) <= int(desire):
        return True
    return False


def buy_price_queu_is_more_than(stockobj, desire):
    if int(stockobj.buy_top_price) >= int(desire):
        return True
    return False


def buy_volume_queu_is_less_than(stockobj, desire):
    if int(stockobj.buy_top_Volume) <= int(desire):
        return True
    return False


def buy_volume_queu_is_more_than(stockobj, desire):
    if int(stockobj.buy_top_Volume) >= int(desire):
        return True
    return False


def last_price_trade_is_less_than(stockobj, desire):
    if int(stockobj.last_price) <= int(desire):
        return True
    return False


def last_price_trade_is_more_than(stockobj, desire):
    if int(stockobj.last_price) >= int(desire):
        return True
    return False


def final_price_trade_is_more_than(stockobj, desire):
    if int(stockobj.final_price) >= int(desire):
        return True
    return False


def final_price_trade_is_less_than(stockobj, desire):
    if int(stockobj.final_price) <= int(desire):
        return True
    return False


def calculate_method(stockobj, desire, fun):
    return fun(stockobj, desire)


def sendTextMessage(stockName, message):
    http = urllib3.PoolManager()
    mystring = smsUrlSend + urllib.parse.quote(message)
    status = "trying to send sms"
    logNotification(stockName, status)
    print(status)
    r = http.request('POST', mystring)
    if r.status == 200:
        if r.data.decode("utf-8") == '1':
            status = "sent sms for " + stockName
            logNotification(stockName, status)
            print(status)
        else:
            status = "failed to send sms for " + stockName
            logNotification(stockName, status)
            print(status)
    else:
        status = "failed to send sms for " + stockName + ' status code: ' + r.status
        logNotification(stockName, status)
        print(status)


def playSound(stockName):
    status = 'playing sound for ' + stockName
    logNotification(stockName, status)
    print(status)
    winsound.PlaySound(sound_file_name, winsound.SND_FILENAME)
    status = 'done'
    logNotification(stockName, status)
    print(status)


def logNotification(stockName, status):
    logging.basicConfig(filename='Output.txt', level=logging.INFO)
    text = str(datetime.now()) + " :" + stockName + ' >> ' + status
    logging.info(text)

def log( status):
    logging.basicConfig(filename='Output.txt', level=logging.INFO)
    text = str(datetime.now()) + ' >> ' + status
    logging.info(text)


def main():
    http = urllib3.PoolManager()
    while True:
        tehranTimeNow = datetime.now(tehran)
        if tehranTimeNow > statTime and tehranTimeNow < finishTime:
            i = 0
            while i < len(Data):
                stock_obj = Stock(http, Data[i]['url'])
                if stock_obj.status:
                    j = 0
                    while j < len(Data[i]['desire_methods']):
                        if calculate_method(stock_obj, Data[i]['desires'][j], eval(Data[i]['desire_methods'][j])):
                            send_notification(Data[i]['stockName'], Data[i]['message'][j])
                            Data[i]['message'].pop(j)
                            Data[i]['desire_methods'].pop(j)
                            Data[i]['desires'].pop(j)
                            j -= 1
                            if len(Data[i]['desires']) == 0:
                                Data.pop(i)
                                i -= 1
                                break
                        j += 1
                    if len(Data) == 0:
                        return
                i += 1
        time.sleep(time_delay)


class Stock:
    yesterday_price = -1

    def __init__(self, http, url):
        try:
            r = http.request('GET', url)
            if r.status == 200:
                data = r.data.decode("utf-8")
                result = data.split(';')[2].split(',')[0]
                result = result.split('@')
                self.buy_top_number = result[0]
                self.buy_top_Volume = result[1]
                self.buy_top_price = result[2]
                self.sell_top_price = result[3]
                self.sell_top_Volume = result[4]
                self.sell_top_number = result[5]
                result = data.split(';')[0].split(',')
                self.last_price = result[2]
                self.final_price = result[3]
                self.yesterday_price = result[5]
                self.status = True
            else:
                print(r.status)
                log(r.status)

        except:
            self.status = False
            log("exception in Stock class")

if __name__ == "__main__":
    for m in range(len(Data)):
        print(Data[m]['stockName'] + ': ' + str(Data[m]['desires'][:]) + 'R')
    main()
    print('done')
