# pip/pip3 install requests beautifulsoup4 lxml datetime
import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

date = "12/2/2024" # Change this to the date you want to scrape. Use the format "MM/DD/YYYY" to match the website's format.

url = f"https://www.yallakora.com/match-center/%D7%85%D8%B1%D9%83%D8%B2-%D8%A7%D9%84%D9%85%D8%A8%D8%A7%D8%B1%D9%8A%D8%A7%D8%AA?date={date}#days" 

page = requests.get(url) # Send a GET request to the URL

soup = BeautifulSoup(page.content, "lxml") # Parse the HTML content of the page with BeautifulSoup

championShips = soup.findAll("div", class_="matchesList") # Find all div elements with class "matchesList"

matchesDetails = [] # Create a list to store the matches details

# Loop through each championShip
for championShip in championShips:
    championShip_title = championShip.contents[1].find("h2").text.strip() 
    
    # Find all match details in the ChampionShip
    for match in championShip.contents[3].find_all("div", class_="allData"):
        matchChanel = match.find("div", class_="channel")
        matchChanel = matchChanel.text.strip() if matchChanel else ''
        matchTour = match.find("div", class_="topData").contents[1].text.strip()
        matchStatus = match.find("div", class_="topData").contents[3].contents[1].text.strip()
        teamA = match.find("div", class_="teamA").find("p").text.strip()
        teamB = match.find("div", class_="teamB").find("p").text.strip()
        scoreA, scoreB = match.find("div", class_="MResult").findAll("span", class_="score")
        scoreA = scoreA.text.strip()
        scoreB = scoreB.text.strip()
        matchTime = match.find("div", class_="MResult").find("span", class_="time").text.strip()
        
        # Append the match details to the list
        matchesDetails.append({"ChampionShip Title": championShip_title, "Match Tour": matchTour, "Team A": teamA, "Score A": scoreA, "Time": matchTime, "Score B": scoreB, "Team B": teamB, "Match Status": matchStatus, "Match Channel": matchChanel})

# Convert the string to a datetime object
date = datetime.strptime(date, "%m/%d/%Y")  # Use the correct format for parsing

formatted_date = date.strftime("%d-%m-%Y")  # Change to a valid format (in my case, I used DD-MM-YYYY) 

# Write the matches details to a CSV file
with open(f'matches_details_{formatted_date}.csv', 'w', newline='', encoding='utf-8') as csvfile:
    keys = matchesDetails[0].keys() # Use the keys from the first dictionary in the list
    writer = csv.DictWriter(csvfile, fieldnames=keys)
    writer.writeheader()
    writer.writerows(matchesDetails)

print("CSV File Created Succesfully.")