#!/usr/bin/python

import csv
import os

import pandas as pd
import requests
import numpy as np
from bs4 import BeautifulSoup


class Scraper:
    def main(self):
         #self.character_scrape(global_bool)
         return 0
    def character_scrape(self) -> bool:
        chars = pd.read_csv('char_id.csv')
        browser_headers = {'Content-type': 'application/json', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0'}
        csv_headers = ['move_id', 'character', 'command', 'hit_level', 'damage', 'start_up_frame', 'block_frame', 'hit_frame', 'counter_hit_frame', 'notes']
        for char in chars.values:
            move_id = 0
            url = 'http://rbnorway.org/' + char[1] + '-t7-frames/'
            page = requests.get(url, headers=browser_headers)
            path = 'data/' + char[1] + '.csv'
            if page.status_code:
                soup = BeautifulSoup(page.content, 'html.parser')
                if os.path.isfile(path):
                    os.remove(path)
                with open(path, 'a+', newline='', encoding='utf-16') as f:
                    writer = csv.writer(f)
                    writer.writerow(csv_headers)
                    tr = soup.find_all('tr')
                    for row in tr:
                        tmp = []
                        tmp.append(move_id)
                        tmp.append(char[1])
                        move_id += 1
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
                        if len(tmp) > 10 or len(tmp) < 10:
                            continue
                        writer.writerow(tmp)
                print(char[1] + " done")
            else:
                print("error on " + char[1])

        return True

    def global_scrape(self) -> bool:
        chars = pd.read_csv('char_id.csv')
        move_id = 1
        csv_headers = ['move_id', 'character', 'command', 'hit_level', 'damage', 'start_up_frame', 'block_frame', 'hit_frame', 'counter_hit_frame', 'notes']
        if os.path.isfile('global_char_moves_list.csv'):
            os.remove('global_char_moves_list.csv')
        f = open('global_char_moves_list.csv', 'a+', newline='', encoding='utf-16')
        writer = csv.writer(f)
        writer.writerow(csv_headers)
        for char in chars.values:
            csv_path = 'data/' + char[1] + '.csv'
            f2 = pd.read_csv(csv_path, encoding='utf-16')
            f2 = f2.replace({np.nan: "NULL"})
            csv_list = f2.values.tolist()
            for lst in csv_list:
                lst[0] = move_id
                move_id += 1
                writer.writerow(lst)                
            
'''
    def character_scrape(self, global_bool: bool):
        chars = pd.read_csv('char_id.csv')
        move_id = 0
        browser_headers = {'Content-type': 'application/json', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0'}
        csv_headers = ['character', 'move_id', 'command', 'hit_level', 'damage', 'start_up_frame', 'block_frame', 'hit_frame', 'counter_hit_frame', 'notes']
        if global_bool:
            path = 'data/global_moves_list.csv'
            if os.path.isfile(path):
                os.remove(path)
            with open(path, 'a+', newline='', encoding='utf-16') as f:
            
        for char in chars.values:
            move_id = move_id if global_bool else 0
            url = 'http://rbnorway.org/' + char[1] + '-t7-frames/'
            headers = {'Content-type': 'application/json',
                       'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0'}
            page = requests.get(url, headers=headers)
            if page.status_code:
                soup = BeautifulSoup(page.content, 'html.parser')
                path = "global_moves.csv" if global_bool else 'data/' + \
                    char[1] + '.csv'
                headers = ['character', 'move_id', 'command', 'hit_level', 'damage', 'start_up_frame', 'block_frame',
                           'hit_frame', 'counter_hit_frame', 'notes']
                if os.path.isfile(path):
                    os.remove(path)
                with open(path, 'a+', newline='', encoding='utf-16') as f:
                    writer = csv.writer(f)
                    writer.writerow(headers)
                    tr = soup.find_all('tr')
                    for row in tr:
                        tmp = []
                        tmp.append(char[1])
                        tmp.append(move_id)
                        move_id += 1
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
                        writer.writerow(tmp)
                print(char[1] + " done")
            else:
                print("error on " + char[1])
    def nullCSV(self):
        for filename in os.listdir('data/'):
            path = 'data/' + filename
            with open(path, 'r', encoding='utf-16') as f:
    '''


if __name__ == "__main__":
    s = Scraper()
    s.global_scrape()