# pip/pip3 install selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Set up the Chrome driver
os.environ['PATH'] += r"C:/SeleniumDrivers"
driver = webdriver.Chrome()

url = 'https://orteil.dashnet.org/cookieclicker/'
driver.get(url)

# Wait for the cookie clicker page to load
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "English")]'))
)

language = driver.find_element(By.XPATH, '//*[contains(text(), "English")]')
language.click()

# Wait for the cookie clicker page to load
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, 'bigCookie'))
)

cookie = driver.find_element(By.ID, 'bigCookie')

while True:
    cookie.click()
    cookies_count = driver.find_element(By.ID, 'cookies').text.split(' ')[0]
    cookies_count = int(cookies_count.replace(',', ''))
    
    for i in range(4):
        product_price = driver.find_element(By.ID, 'productPrice' + str(i)).text.replace(',', '')
        
        if not product_price.isdigit():
            continue
        
        product_price = int(product_price)
        
        if cookies_count >= product_price:
            product = driver.find_element(By.ID, 'product' + str(i))
            product.click()
            break