from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd
import random
import time

DRIVER_PATH = '../utils/chromedriver-win64/chromedriver.exe' # Update this with your actual path
service = Service(DRIVER_PATH)  

df_1 = pd.read_csv('../dump/flipkart_products_input.csv')

driver = webdriver.Chrome(service=service)

for row in df_1.iterrows():
    id = row[1]['id']
    href = row[1]['href']
    print(id, href)

    try:
        driver.get(href)
        time.sleep(random.choice(
            [i for i in range(1,5)]
        ))
        html = driver.page_source
        with open(f'../htmls/{id}.html', 'w', encoding='utf-8') as file:
            file.write(html)
            print(f'saved>> {id}')
    except Exception as e:
        print(e)

driver.close()