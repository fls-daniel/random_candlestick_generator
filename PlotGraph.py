import random
import pandas as pd
from datetime import datetime
import csv
import mplfinance as mpf
from mplfinance.original_flavor import candlestick_ohlc
import matplotlib.pyplot as plt
import time as t
from pynput import keyboard
import os 
user = str(os.getlogin())
 
def check1():
    if lclose[5] > lclose[6]:
        keyboard.wait('down arrow')
        plt.close()
def check2():
    if lclose[5] < lclose[6]:
        keyboard.wait('up arrow')
        plt.close()
while True:
    while True:    
        
        csv_reader = csv.DictReader(open('C:/Users/' + user + '/Downloads/EURUSDCHART.csv', mode='r'))

        num = random.randint(1, 245439)
        dopen = []
        high = []
        low = []
        close = []
        lopen = []
        lhigh = []
        llow = []
        lclose = []
        for i in range(6):
            for row in csv_reader:
                dopen.append(row['Open'])
                high.append(row['High'])
                low.append(row['Low'])
                close.append(row['Close'])

            lopen.append(float(dopen[num+i]))
            lhigh.append(float(high[num+i]))
            llow.append(float(low[num + i]))
            lclose.append(float(close[num+ i]))
        if lopen == lclose:
            break
            
        fopen = float(dopen[num+6])
        fhigh = float(high[num+6])
        flow = float(low[num + 6])
        fclose = float(close[num+ 6])
        d = {'Time': [1,2,3,4,5,6], 'Open': lopen, 'High': lhigh, 'Low': llow, 'Close': lclose}
        df = pd.DataFrame(data=d)
        fig, ax = plt.subplots()
        candlestick_ohlc(ax, df.values, width = 0.6, colorup = 'green', colordown = 'red', alpha = 0.8)
        lopen.append(fopen)
        lhigh.append(fhigh)
        llow.append(flow)
        lclose.append(fclose)
        plt.pause(5)
        plt.show(block=False)
        if lclose[5] > lclose[6]:
            plt.close(fig)
        if lclose[5] < lclose[6]:
            plt.close(fig)

        d = {'Time': [1,2,3,4,5,6,7], 'Open': lopen, 'High': lhigh, 'Low': llow, 'Close': lclose}
        df = pd.DataFrame(data=d)
        fig, ax = plt.subplots()
        candlestick_ohlc(ax, df.values, width = 0.6, colorup = 'green', colordown = 'red', alpha = 0.8)

        plt.pause(0.001)
        plt.show(block=False)
        plt.pause(3)
        plt.close(fig)