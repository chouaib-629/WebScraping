# pip/pip3 install beautifulsoup4 requests lxml pandas
from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"

# Send a GET request
page = requests.get(url)

# Parse the HTML content of the page with BeautifulSoup using lxml parser
soup = BeautifulSoup(page.text, "lxml")

# Find all table rows
Top100publiclyTradedCompanies = soup.find("table", {"class": "wikitable sortable"})

# Extract the titles of the columns
titles = [title.text.strip() for title in Top100publiclyTradedCompanies.find_all("th")]

# Set the titles as the column names of the DataFrame
df = pd.DataFrame(columns=titles)

# Loop through each row in the table, and extract the data of each cell
for row in Top100publiclyTradedCompanies.find("tbody").find_all("tr")[1:]:
    rowData = [data.text.strip() for data in row.find_all("td")]

    # Append the row data to the DataFrame at the end
    df.loc[len(df)] = rowData

# Export the data to a CSV file
df.to_csv('Top100publiclyTradedCompanies.csv', index=False)
    