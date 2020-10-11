import requests
from bs4 import BeautifulSoup as bs
from time import sleep 

#Load a webpage content:Check URL
url = "https://www.jpx.co.jp/markets/statistics-equities/investor-type/05.html"
r = requests.get(url)

#Convert to a beautiful soup object
soup = bs(r.text, "html.parser")

#Load the table data:Check HTML & CSS structure
table = soup.find("div", {"class":"component-normal-table"})
link = table.find_all("a")

#Download files from the webpage
for links in link:
    try:
        download_url = 'https://www.jpx.co.jp' + links['href']
        data = download_url.rsplit('/',1)[1]
        r = requests.get(download_url, allow_redirects=True)
        with open(data, 'wb') as f:
            f.write(r.content)
        sleep(2)
        
    except KeyError:
        print('***no href***')

