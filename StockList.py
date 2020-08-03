import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
result = requests.get(url)
src = result.content
soup = BeautifulSoup(src, 'html.parser')
table_list = soup.find('tbody')
tr_list = table_list.find_all('tr')
td_list = table_list.find_all('td')
a_list = table_list.find_all('a')
#for i in tr_list:
    #print(tr_list[tr_list.index(i)].)
stock_file = open("s&pStocks.txt", "a")
for x in a_list:
    if(len(x.string) <= 5):
        print(x.string)
        stock_file.write(x.string + "\n")
        
stock_file.close()