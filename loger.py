import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json_parser

# Getting the price of the stock
def parse_price(url):
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
        parse_price()
    #print(price_span)
    #print(vol_span)
    out = price_span.text + " | " + vol_span
    #print(out)
    return out

json_parser.parse_json()

working = False
def workingTrue():
	working = True
def workingFalse():
	working = False

while working == True:
    try:
        for i in json_parser.url_list:
            now = datetime.now()
            today = now.strftime("%y-%m-%d")
            local_db = open("Data/" + str(json_parser.name_list[json_parser.url_list.index(i)]) + "/"  + str(today) +".txt", "a")
            current_time = now.strftime("%H:%M:%S : ")
            sentence = str(current_time) + str(parse_price(i))
            local_db.write(str(sentence) + "\n")
            print(sentence)
            local_db.close()
        print("Done")
    except ValueError as err:
        print(err)

