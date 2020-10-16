import requests
from bs4 import BeautifulSoup as bs
import csv
import pandas as pd
from time import sleep 

#Load a webpage content:Check URL
url = "https://web-kanji.com/search/ehime"
r = requests.get(url)

#Convert to a beautiful soup object
soup = bs(r.text, "html.parser")

#Load the table data:Check the webpage structure
ehime = soup.find_all("div", {"class":"companies-item-summary"})

names = []
addresses = []
infos = []

#Get company's name, addreess, infomation from the webpage:Check the webpage structure.
for company in ehime:
    name = str(company.find('h3').string).strip()
    address = str(company.find('div', {'class':'companies-item-address'}).string).strip()
    info = str(company.find('p', {'class':'companies-item-introduction'}).string).strip()
    names.append(name)
    addresses.append(address)
    infos.append(info)    
    sleep(2)

#Make DataFrame
df = pd.DataFrame(names, columns=['name'])
df.insert(1, 'address', addresses, True)
df.insert(2, 'info', infos, True)

#Save the DataFrame as CSV files.
df.to_csv('job_search.csv', index=False)

