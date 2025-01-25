import time #py builtin module, written in c
import os #py imported module, written in py
import pandas #py installed module, written in py

while True:
    if os.path.exists('txt_fl/temps_today.csv'):
        data = pandas.read_csv('txt_fl/temps_today.csv')
        print(data.mean())
    else:
        print('file does not exist')
    time.sleep(5)