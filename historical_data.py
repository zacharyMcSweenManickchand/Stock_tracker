import requests
import json
#import jsonpickle
#from json import JSONEncoder

print("Wait for it")

def alphaVantage(function, symbol, interval, outputsize):
    apiKey = open("apikey.txt", "r")
    key = apiKey.readline()
    apiKey.close()
    intervalout = ""
    if (interval != ""):
        intervalout = "&interval=" + interval
    result = requests.get("https://www.alphavantage.co/query?function=" + function + "&symbol=" + symbol + intervalout + "&outputsize=" + outputsize + "&apikey=" + key).json()
    #print(result)
    with open( "Data/Historical/" + function + "/" + symbol + ".json", "w") as json_file:
        json.dump(result, json_file, indent=4, separators=(',', ': '))
    

alphaVantage("TIME_SERIES_INTRADAY", "IBM", "1min", "full")
#alphaVantage("TIME_SERIES_DAILY", "IBM", "", "full")

print("Done")