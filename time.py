import schedule
import time
import loger

dayOfWeek = int(time.strftime("%w"))
def checkdayOfWeek():
    global dayOfWeek
    dayOfWeek = int(time.strftime("%w"))

schedule.every().day.at("09:00").do(checkdayOfWeek)

if(dayOfWeek != 6 and dayOfWeek != 0):
	schedule.every().day.at("09:30").do(loger.workingTrue)
	schedule.every().day.at("16:00").do(loger.workingFalse)

#print(time.strftime("%w"))
while True:
    schedule.run_pending()
    time.sleep(1)