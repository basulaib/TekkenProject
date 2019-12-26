#!/usr/bin/python

from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv

chars = pd.read_csv('files/chars.csv')
for char in chars.values:
    print(char[1])
    url = 'http://rbnorway.org/' + char[1] + '-t7-frames/'
    headers = {'Content-type': 'application/json', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0'}
    print(url)
    page = requests.get(url, headers=headers)
    print(page)
    if page.status_code:
        soup = BeautifulSoup(page.content, 'html.parser')
        h3 = soup.find_all('h3')
        print(h3)
        tb = soup.find('tr')
        print(tb[0].getText())
        break
    else:
        print("error")
        break