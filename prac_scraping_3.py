from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

chrome_options = Options()
chrome_service = Service('./chromedriver.exe')

driver = webdriver.Chrome(service=chrome_service)

url = "https://www.spacex.com/launches/"
driver.get(url)
sleep(5)

sleep(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(10) 

req = driver.page_source

driver.quit()

soup = BeautifulSoup(req, 'html.parser')

items = soup.select('.item')

for item in items:
    date = item.select_one('.date').text.strip()
    label = item.select_one('.label').text.strip()
    print(date,label)
    