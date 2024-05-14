from bs4 import BeautifulSoup as bs
from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from io import StringIO
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
service = Service()
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--disable-extensions')
options.add_argument('--disable-quic')
driver = webdriver.Chrome(service=service, options=options)
URL = "http://ecodata.kz:3838/dm_climat_ru/"
driver.get(URL)
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="sidebarItemExpanded"]/ul/li[4]/a').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="sidebarItemExpanded"]/ul/li[4]/ul/li[8]/a').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="sidebarItemExpanded"]/ul/li[4]/ul/li[8]/ul/li[1]/a').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="sidebarItemExpanded"]/ul/li[4]/ul/li[8]/ul/li[1]/ul/li[1]/a').click()
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="shiny-tab-amount_o"]/div/div[1]/div[1]/div/div/div/div[1]').click()
time.sleep(3)
pyautogui.click(472, 482)
driver.find_element(By.XPATH, '//*[@id="date_amount_o"]/div/input[1]').clear()
driver.find_element(By.XPATH, '//*[@id="date_amount_o"]/div/input[2]').clear()
driver.find_element(By.XPATH, '//*[@id="date_amount_o"]/div/input[1]').send_keys('2000-01-01')
driver.find_element(By.XPATH, '//*[@id="date_amount_o"]/div/input[1]').send_keys(Keys.RETURN)
driver.find_element(By.XPATH, '//*[@id="date_amount_o"]/div/input[2]').send_keys('2023-12-21')
driver.find_element(By.XPATH, '//*[@id="date_amount_o"]/div/input[2]').send_keys(Keys.RETURN)
time.sleep(30)
content = driver.page_source
t = 13
def scrap(content, t):
    soup = bs(content, "html.parser")
    table = soup.find_all("table", class_='cell-border stripe dataTable no-footer')
    df = pd.read_html(StringIO(str(table)))[1]
    df.to_csv(f'C:\\Users\\Rakon\\Desktop\\Final Project\\Table{t}.csv', index=False)
    return t + 1
t = scrap(content, t)
driver.find_element(By.XPATH, '//*[@id="shiny-tab-amount_o"]/div/div[1]/div[1]/div/div/div/div[1]').click()
time.sleep(3)
pyautogui.click(472, 450)
time.sleep(30)
content = driver.page_source
t = scrap(content, t)