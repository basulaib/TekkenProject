#!/usr/bin/python

from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv
import os.path

chars = pd.read_csv('char_id.csv')
for char in chars.values:
    url = 'http://rbnorway.org/' + char[1] + '-t7-frames/'
    headers = {'Content-type': 'application/json', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0'}
    page = requests.get(url, headers=headers)
    if page.status_code:
        soup = BeautifulSoup(page.content, 'html.parser')
        path = 'data/' + char[1] + '.csv'
        headers = ['Command', 'Hit level', 'Damage', 'Start up frame', 'Block frame', 'Hit frame', 'Counter hit frame', 'Notes']
        if not os.path.isfile(path):
            with open(path, 'a+', newline='', encoding='utf-16') as f:
                writer = csv.writer(f)
                writer.writerow(headers)
                tr = soup.find_all('tr')
                for row in tr:
                    td = row.find_all('td')
                    if len(td) == 0:
                        continue
                    td = [x.text.strip() for x in td]
                    if td[0] == 'Command':
                        continue
                    writer.writerow(td)
            print(char[1] + " done")
        else:
            print(char[1] + " csv exists")
    else:
        print("error on " + char[1])