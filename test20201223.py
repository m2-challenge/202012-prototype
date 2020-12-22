import time
import datetime
from log import*
#from dac import*
#from motor import*

if __name__ == "__main__":
    logname = fileName("log/log", "txt")
    now = datetime.datetime.fromtimestamp(time.time())
    saveLog(logname, logname, now.strftime('%Y/%m/%d %H:%M:%S'))

    for i in range(100):
        saveLog(logname, time.time(), i)
        time.sleep(0.1)
        print(i)
