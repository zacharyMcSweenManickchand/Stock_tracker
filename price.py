import requests
from bs4 import BeautifulSoup
import main

# Getting the price of the stock
def getPrice(url):
    result = requests.get(url)
    #print(result.status_code) # to see if the link is valid
    src = result.content
    soup = BeautifulSoup(src, 'html.parser')
    links = soup.find_all('div', {'My(6px) Pos(r) smartphone_Mt(6px)'})
    #table_list = soup.find_all('tr', {'Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px) '})
    table_list = soup.find('tbody')
    span_list = table_list.find_all('span')
    #print(links)
    #print(span_list)
    try:
        price_span = links[0].find('span')
        vol_span = span_list[11].string
    except:
        print("Error")
        main.loging()
    #print(price_span)
    #print(vol_span)
    out = price_span.text + " | " + vol_span
    #print(out)
    return out