import os

import shutil

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time

import random
import csv

csv_file=open('result.csv')
csv_reader_lines = csv.reader(csv_file)
data=[]
count = 1
for line in csv_reader_lines:
    data.append(line)
    count=count+1
i=0
while i < count:
    chrome_options = Options()
    chrome_options.add_argument('headless')
    driver = webdriver.Chrome(r'C:\Program Files\Google\Chrome\Application\chromedriver.exe',chrome_options=chrome_options)
    picture_url = data[i][0]
    driver.get(picture_url)
    driver.maximize_window()
    width = driver.execute_script("return document.documentElement.scrollWidth")
    height = driver.execute_script("return document.documentElement.scrollHeight")
    print(width,height)
    driver.set_window_size(width, height)
    #time.sleep(1)
    #print(dir(driver))
    print(data[i][1])
    print(type(data[i][1]))
    driver.get_screenshot_as_file('D:\\test/%s.jpg' % data[i][1])
    print("%s：截图成功！！！" % picture_url)
    driver.close()
    i=i+1
