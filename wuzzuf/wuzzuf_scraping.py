# pip/pip3 install requests beautifulsoup4 lxml
import requests
from bs4 import BeautifulSoup
import csv

searchedJob = "python"
url = f"https://wuzzuf.net/search/jobs?q={searchedJob}"

page = requests.get(url) # Send a GET request to the URL

soup = BeautifulSoup(page.content, "lxml") # Parse the HTML content of the page with BeautifulSoup

jobsCard = soup.find_all("div", class_="css-pkv5jc") # Find all the job cards on the page

jobsList = [] # Create an empty list to store the jobs

# Loop through each job card and extract the required information
for job in jobsCard:
    jobTitle = job.find("a", class_="css-o171kl").text.strip()
    companyName = job.find("a", class_="css-17s97q8").text.strip()
    companyLocation = job.find("span", class_="css-5wys0k").text.strip()
    jobPosted = job.find("div", class_="css-4c4ojb").text.strip() if job.find("div", class_="css-4c4ojb") else job.find("div", class_="css-do6t5g").text.strip()
    jobTime = job.find("span", class_="css-1ve4b75").text.strip()
    jobPlace = job.find("span", class_="css-o1vzmt").text.strip()
    jobExperience = job.find("div", class_="css-y4udm8").contents[1].find("span").text.strip()
    jobDescription = []
    for a in job.find("div", class_="css-y4udm8").contents[1].find_all("a"):
        jobDescription.append(a.text.strip())
    
    jobsList.append({"Job Title": jobTitle, "Company Name": companyName, "Company Location": companyLocation, "Job Posted": jobPosted, "Job Time": jobTime, "Job Place": jobPlace, "Job Experience": jobExperience, "Job Description": jobDescription})
    
# Write the matches details to a CSV file
with open(f"jobsList_{searchedJob}.csv", "w", newline="", encoding="utf-8") as csvfile:
    keys = jobsList[0].keys() # Use the keys from the first dictionary in the list
    writer = csv.DictWriter(csvfile, fieldnames=keys)
    writer.writeheader()
    writer.writerows(jobsList)

print("CSV File Created Succesfully.")