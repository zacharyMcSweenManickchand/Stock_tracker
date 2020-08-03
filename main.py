from datetime import datetime
import schedule
import time
import price

#Boots program at certain time
def bootTimer():
    while True:
        if((dayOfWeek != 6 and dayOfWeek != 0) and (datetime.now().strftime("%H:%M") == "09:30")):
            loging()
            break

schedule.every().day.at("09:00").do(bootTimer)

def loging():
    while True:
        try:
            now = datetime.now()
            today = now.strftime("%y-%m-%d")
            local_db = open("Data/Facebook/"  + str(today) +".txt", "a")
            current_time = now.strftime("%H:%M:%S : ")
            sentence = str(current_time) + str(price.getPrice("https://ca.finance.yahoo.com/quote/FB?p=FB&.tsrc=fin-srch"))
            local_db.write(str(sentence) + "\n")
            print(sentence)
            local_db.close()
        except ValueError as err:
            print(err)
        if(int(datetime.now().strftime("%H")) == 4):
            break

while True:
    dayOfWeek = int(time.strftime("%w"))
    schedule.run_pending()
    time.sleep(1)