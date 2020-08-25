import csv
import pandas
import sys
import time
import request
from bs4 import BeautifulSoup
import base64

def read_cell(x, y):
    with open('D:/00課程/大二下學期/競賽/bike-analysis/driect/http.csv','r', encoding = 'utf-8') as f:
        reader = csv.reader(f)
        y_count = 0
        for n in reader:
            if y_count == y:
                cell = n[x]
                return cell
            y_count += 1

for v in range(451):
  #print (read_cell(6, v)) 
  herf=read_cell(15, v)
  from selenium import webdriver
  driver = webdriver.Chrome('D:/00課程/大二下學期/競賽/bike-analysis/driect/chromedriver.exe')
  print(herf)
  #print(type(herf))
  #driver.get(herf)
  #time.sleep(5)
  #driver.close()