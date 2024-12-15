# pip/pip3 selenium beautifulsoup4 
from selenium import webdriver
import csv
import os
from datetime import datetime
from functions import extract_page_data

# Set up the Selenium WebDriver
os.environ['PATH'] += r"C:/SeleniumDrivers"
driver = webdriver.Chrome()

driver.maximize_window()

current_time = datetime.now()
# File to save the extracted data
output_file = f'crypto_data_{current_time.strftime('%d-%m-%Y')}_{current_time.strftime('%H-%M')}.csv'

# Define headers for the CSV
headers = [
    "Coin Rank", "Coin Name", "Coin Code", "Price", "1h Change", "24h Change",
    "7d Change", "Market Cap", "Volume", "Circulating Supply", "Extraction Time"
]

# Open the CSV file for writing
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)

    # Extract data from pages 1 and 2
    for page_number in range(1, 3):
        table_data = extract_page_data(driver, page_number)
        writer.writerows(table_data)

    print(f"Data extraction completed. Check the '{output_file}' file.")

# Close the browser
driver.quit()
