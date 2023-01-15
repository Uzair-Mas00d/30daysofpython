# Day 22 - 30DaysOfPython Challenge
import requests
from bs4 import BeautifulSoup
import json
import csv
from os import remove

# Question 1

url = 'http://www.bu.edu/president/boston-university-facts-stats/'
response = requests.get(url)
contents = response.content
soup = BeautifulSoup(contents, "html.parser")
data = soup.find_all("div",{"class": "facts-wrapper"})

header_tag = soup.find_all("h5")
headers = [header.text.strip() for header in header_tag]

dic = {}
for wrapper in data:
    data_points = wrapper.find_all('li', class_='list-item')
    for data_point in data_points:     
        text = data_point.find('p', class_='text').text
        value = data_point.find('span', class_='value').text
        dic[text] = value

 
with open("Bu_edu.json","w") as f:
    f.write(json.dumps(dic,indent=2))     

# Question 2

url = "https://archive.ics.uci.edu/ml/datasets.php"
response = requests.get(url)
contents = response.content
soup = BeautifulSoup(contents, "html.parser")
tables = soup.find("table",{"cellpadding": "5"})

header_tag = tables.find_all("p", class_="whitetext")
headers = [header.text.strip().replace("#","") for header in header_tag]

rows = []
data_row = tables.find_all("tr")  
for row in data_row: 
    value = row.find_all("p",class_="normal")
    beutified_value = [dp.text.strip() for dp in value]
    
    if len(beutified_value) == 1:
        continue 
    
    rows.append(beutified_value)

with open("UCI.csv","w",newline="",encoding="utf-8") as f1:
    writer = csv.writer(f1)
    writer.writerow(headers)
    for row in rows:
        writer.writerow(row)

data = {}
with open("UCI.csv", encoding="utf-8") as f2:
    csvReader = csv.DictReader(f2)

    for rows in csvReader:
        key = rows["Name"]
        data[key] = rows

with open("UCI_DATASET.json", "w",encoding="utf-8") as f3:
    f3.write(json.dumps(data, indent=4))

remove("UCI.csv")


# Question 3
url = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"
response = requests.get(url)
contents = response.content
soup = BeautifulSoup(contents, "html.parser")
tables = soup.find("table")

header_tag = tables.find_all("th")
headers = [header.get_text().strip() for header in header_tag][2:7]

rows = []
data_rows = tables.find_all("tr")
for row in data_rows:
    value = row.find_all("td")
    
    beautified_value = [dp.text.strip() for dp in value][1:]   
    if len(beautified_value) == 0:
        continue
    
    rows.append(beautified_value)
    
with open("president.csv","w",newline="",encoding="utf-8-sig") as f1:
    writer = csv.writer(f1)
    writer.writerow(headers)
    for row in rows:
        writer.writerow(row)

data = {}
with open("president.csv", encoding="utf-8-sig") as f2:
    csvReader = csv.DictReader(f2)
    
    for rows in csvReader:
        key = rows["Name(Birth–Death)"]
        data[key] = rows

with open("president.json", "w",encoding="utf-8-sig") as f3:
    f3.write(json.dumps(data, indent=4))

remove("president.csv")