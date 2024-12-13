from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

def extract_page_data(driver, page_number):
    """
    Extract data from a specific CoinMarketCap page by number.
    
    Parameters:
        driver (webdriver.Chrome): The Selenium WebDriver instance.
        page_number (int): The page number to navigate to.

    Returns:
        list: A list of rows containing the extracted data for the specified page.
    """
    # Navigate to the desired page
    url = f"https://coinmarketcap.com/?page={page_number}"
    driver.get(url)

    # Wait for the table rows to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "table tbody tr"))
    )

    # Scroll to the bottom of the page to ensure all rows are loaded
    scroll_pause_time = 0.5
    last_height = driver.execute_script("return document.body.scrollHeight")
    no_change_count = 0

    while True:
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
        time.sleep(scroll_pause_time)
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            no_change_count += 1
        else:
            no_change_count = 0

        if no_change_count == 2:
            break

        last_height = new_height

    # Get the page source
    html = driver.page_source

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Extract table rows
    rows = soup.select("table tbody tr")

    # Extract the required fields
    table_data = []
    for row in rows:
        try:
            coin_name = row.select_one('.coin-item-name').text.strip()
            coin_code = row.select_one('.coin-item-symbol').text.strip()
            price = row.select_one('td:nth-child(4) span').text.strip()
            hour_change = row.select_one('td:nth-child(5)').text.strip()
            day_change = row.select_one('td:nth-child(6)').text.strip()
            week_change = row.select_one('td:nth-child(7)').text.strip()
            market_cap = row.select_one('td:nth-child(8) span:nth-child(2)').text.strip()
            volume = row.select_one('td:nth-child(9) p:first-child').text.strip()
            circulating_supply = row.select_one('td:nth-child(10) p').text.strip()

            table_data.append([
                coin_name, coin_code, price, hour_change, day_change,
                week_change, market_cap, volume, circulating_supply
            ])
        except AttributeError:
            # Skip rows with missing data
            continue

    return table_data