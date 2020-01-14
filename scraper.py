#!/usr/bin/python

from bs4 import BeautifulSoup
import requests
import pandas as pd
import csv
import os


class Scraper:
    def scrape(self):
        t = 1
        chars = pd.read_csv('char_id.csv')
        for char in chars.values:
            url = 'http://rbnorway.org/' + char[1] + '-t7-frames/'
            headers = {'Content-type': 'application/json', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0'}
            page = requests.get(url, headers=headers)
            if page.status_code:
                soup = BeautifulSoup(page.content, 'html.parser')
                path = 'data/' + char[1] + '.csv'
                headers = ['move_id','character','command', 'hit_level', 'damage', 'start_up_frame', 'block_frame', 'hit_frame', 'counter_hit_frame', 'notes']
                if not os.path.isfile(path):
                    with open(path, 'a+', newline='', encoding='utf-16') as f:
                        writer = csv.writer(f)
                        writer.writerow(headers)
                        tr = soup.find_all('tr')
                        for row in tr:
                            tmp = []
                            td = row.find_all('td')
                            if len(td) == 0:
                                continue
                            for x in td:
                                x = x.text.strip()
                                if x == "":
                                    x = "NULL"
                                tmp.append(x)
                            # td = [x.text.strip() for x in td]
                            if tmp[0] == 'Command':
                                continue
                            tmp.insert(0,t)
                            t += 1
                            tmp.insert(1, char[1])
                            writer.writerow(tmp)
                    print(char[1] + " done")
                else:
                    print(char[1] + " csv exists")
            else:
                print("error on " + char[1])
    '''
    def nullCSV(self):
        for filename in os.listdir('data/'):
            path = 'data/' + filename
            with open(path, 'r', encoding='utf-16') as f:
    '''
if __name__ == "__main__":
    s = Scraper()
    s.scrape()