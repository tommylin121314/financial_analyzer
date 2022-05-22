from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.utils import ChromeType
import time
import pandas as pd

opts = webdriver.ChromeOptions()
opts.add_argument('headless')
cap = DesiredCapabilities.CHROME
cap["pageLoadStrategy"] = "none"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.set_window_size(1280,720)
driver.get('https://finviz.com/news.ashx')
time.sleep(5)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

hrefs = soup.find_all('a', {"class": "nn-tab-link"})
headlines = []
for href in hrefs:
    headlines.append(href.text)
headlines = headlines[1:]

df = pd.DataFrame(headlines, columns=['headline'])
df.to_csv('headlines.csv')