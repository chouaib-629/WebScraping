# Web Scraping Projects

This repository contains a collection of websites that I have scraped for learning and experimentation purposes. The scraped data is organized into subfolders, where each subfolder corresponds to a specific website. These websites were scraped using different techniques, including Beautiful Soup (bs4) for static content, Selenium for dynamic content, and a mix of both for certain cases.

## Folder Structure

- **Main Folder**: Contains subfolders, each representing a scraped website.
- **Subfolders**: Named based on the website they were scraped from. Each subfolder contains:
  - The Python code used to scrape the website in two formats: `.py` and `.ipynb`.
  - The CSV file containing the scraped data.

## Scraping Techniques

1. **Static Websites**:
   - Scraped using **Beautiful Soup (bs4)**.
   - These websites have static HTML content that can be directly accessed and parsed.

2. **Dynamic Websites**:
   - Scraped using **Selenium**.
   - These websites load data dynamically through JavaScript, requiring a browser simulation to fetch the content.

3. **Mixed Approach**:
   - Some websites required a combination of **Selenium** and **bs4**.
   - Selenium was used to render the dynamic content, and Beautiful Soup was used for parsing the HTML.

## Classification of Websites

Below is the list of websites classified by the scraping technique used:

### Beautiful Soup (bs4)

- [yallakora](https://www.yallakora.com/match-center/%d9%85%d8%b1%d9%83%d8%b2-%d8%a7%d9%84%d9%85%d8%a8%d8%a7%d8%b1%d9%8a%d8%a7%d8%aa#nav-menu)
- [wuzzuf](https://wuzzuf.net/jobs/egypt)
- [wikipedia](https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue)

### Selenium

- [cookieClicker](https://orteil.dashnet.org/cookieclicker/)

### Mixed Approach

- [coinMarketCap](https://coinmarketcap.com/)

## Requirements

To replicate or run the scraping scripts used in this project, the following Python libraries are required:

- **Beautiful Soup**: `bs4`
- **Selenium**
- **Requests**
- **lxml**
- **html.parser**

Ensure you have Python installed, along with the necessary libraries. For Selenium, download the appropriate browser driver (e.g., ChromeDriver for Google Chrome).

## Getting Started

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/chouaib-629/WebScraping.git
   ```

2. Navigate to the desired subfolder to inspect the scraped data or associated scripts.

## Notes

- The data scraped from these websites is for educational purposes only. Please adhere to the terms and conditions of the websites before scraping.
- The scripts and data are provided "as is" without warranty of any kind.

## Author

This project is managed by a data science enthusiast and full-stack developer experimenting with web scraping techniques.

## Contact Information

For questions or support, please contact [Me](mailto:chouaiba629@gmail.com).
