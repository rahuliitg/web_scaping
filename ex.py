import urllib.request
from bs4 import BeautifulSoup

date = input('Enter date in YYYY/MM/DD format. (2014/jan/23)     ')
print("\n")
page_source = 'http://news.rediff.com/commentary/'+ date + '/liveupdates.htm'
page = urllib.request.urlopen(page_source)
soup = BeautifulSoup(page,'html.parser')
latest = soup.find_all('a' , attrs = {'class':'black'})
for news in latest[0:9]:
    head = news.contents[0]
    print(head)
print("\n")