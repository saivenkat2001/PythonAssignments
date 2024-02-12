import schedule
import time
import pyautogui

starttime =time.time()
while True:
    x, y = pyautogui.position()
    time.sleep(1)
    print((x,y))
    endtime =time.time()
    if(endtime-starttime >10):
        break

def perform_windows_update():
    print("hello")


schedule = schedule.Scheduler()

schedule.every().day.at("12:00").do(perform_windows_update)

while True:
    schedule.run_pending()
    time.sleep(1)

