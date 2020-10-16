import requests
from bs4 import BeautifulSoup as bs
import csv
import pandas as pd
from time import sleep 

#Load a webpage content:Check URL
url = "https://crowdworks.jp/public/jobs/skill/21"
r = requests.get(url)

#Convert to a beautiful soup object
soup = bs(r.text, "html.parser")

#Load the table data:Check the webpage structure
crw = soup.find_all("div", {'class':'job_data_column summary'})
i = 0
names = []
infos = []

#Get company's name, addreess, infomation from the webpage:Check the webpage structure.
for theme in crw:
    name = str(theme.find('a').string).strip()
    info = str(theme.find('p').string).strip()
    names.append(name)
    infos.append(info) 
    i += 1
    print(str(i) + '個のデータを取得しました。')   
    sleep(2)

#Make DataFrame
df = pd.DataFrame(names, columns=['name'])
df.insert(1, 'info', infos, True)

#Save the DataFrame as CSV files.
df.to_csv('search_crw.csv', index=False)
print('エクセルに出力しました。')

