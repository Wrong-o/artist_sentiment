from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import time
import json
import os

artist = input("Input artist as seen on genius.com: ")
firefox_options = Options()
firefox_options.add_argument("--headless")  
firefox_binary_path = r'C:\Program Files\Mozilla Firefox\firefox.exe'  
firefox_options.binary_location = firefox_binary_path
gecko_driver_path = r'C:\Users\jayb\Desktop\blogg\tools\geckodriver-v0.34.0-win32\geckodriver.exe'  

service = Service(gecko_driver_path)
driver = webdriver.Firefox(service=service, options=firefox_options)

url = f"https://genius.com/artists/{artist}/songs"
driver.get(url)

last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    time.sleep(3)
    
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


html_content = driver.page_source


driver.quit()


soup = BeautifulSoup(html_content, 'html.parser')


urls = [a['href'] for a in soup.find_all('a', class_='ListItem__Link-sc-122yj9e-1 klWOzg')]


os.makedirs(f'./{artist}', exist_ok=True)


with open(f'./{artist}/song_list.json', 'w', encoding='utf-8') as f:
    json.dump(urls, f, ensure_ascii=False, indent=4)

for url in urls:
    print(url)
