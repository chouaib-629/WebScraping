# CoinMarketCap Data Scraper

The CoinMarketCap Data Scraper is a Python-based project that automates the process of extracting cryptocurrency data from the CoinMarketCap website. It utilizes Selenium for dynamic content interaction and BeautifulSoup for efficient HTML parsing. This tool can extract vital cryptocurrency information, such as coin name, code, price, market cap, and more, along with the timestamp of data extraction.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [Contact Information](#contact-information)

## Features

- Dynamically extracts cryptocurrency data across multiple pages.
- Includes fields such as:
  - Coin name
  - Coin code
  - Price
  - Hourly, daily, and weekly price changes
  - Market cap
  - Volume
  - Circulating supply
  - Scraping timestamp
- Handles lazy-loaded content using smart scrolling.
- Saves the extracted data in a CSV file for easy analysis.
- Output file includes the date and time of scraping in the filename.

## Technologies Used

- Python
- Selenium
- BeautifulSoup
- CSV
- Jupyter Notebook

## Getting Started

### Prerequisites

- Python 3.7 or higher installed.
- Google Chrome browser.
- Compatible version of ChromeDriver added to your system PATH.
- Required Python libraries: selenium beautifulsoup4

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/chouaib-629/WebScraping.git
   ```

2. Navigate to the project directory:

   ```bash
   cd WebScraping/coinMarketCap
   ```

3. Install the required libraries:

   ```bash
   pip install selenium beautifulsoup4
   ```

## Usage

1. Ensure that `functions.py`, the Python script, and the Jupyter Notebook are in the same directory.
2. To run the Python script:

   ```bash
   python coinMarketCap_scraper.py
   ```

3. To use the Jupyter Notebook, open it in your Jupyter environment:

   ```bash
   jupyter notebook coinMarketCap_scraper.ipynb
   ```

4. The extracted data will be saved in a CSV file with a name like `crypto_data_{date of scraping}_{time of scraping}.csv` in the project directory.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.

2. Create a new branch:

   ```bash
   git checkout -b feature/feature-name
   ```

3. Commit your changes:

   ```bash
   git commit -m "Add feature description"
   ```

4. Push to the branch:

   ```bash
   git push origin feature/feature-name
   ```

5. Open a pull request.

## Contact Information

For questions or support, please contact [Me](mailto:chouaiba629@gmail.com).
