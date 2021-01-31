import time
import datetime
import traceback
from log import*
from adc import*
from motor import*

if __name__ == "__main__":
    pi = pigpio.pi()
    if not pi.connected:
        exit(0)
    adc = ADC(pi, ref_volts=3.3)
    motor = Motor(18, 19)

    try:
        #--- Initialization ---#
        print("\n#----- Initialization -----#")
        logName = fileName("log/log", "txt")
        now = datetime.datetime.fromtimestamp(time.time())
        saveLog(logName, logName, now.strftime('%Y/%m/%d %H:%M:%S'))
        print("Log File Name : " + logName)
        print(now.strftime('%Y/%m/%d %H:%M:%S') + " UTC")

        #--- Main Process ---#
        print("\n\n#----- Main Process -----#")
        for i in range(170):
            volt74 = adc.GetVoltage(ch=0) * 3.75
            volt37 = adc.GetVoltage(ch=1) * 2.0
            motor.setSpeed(100)
            saveLog(logName, time.time(), i, volt74, volt37)
            time.sleep(0.1)
            print(i)

    except KeyboardInterrupt:
        print("\n\n#----- Keyboard Interrupt -----#")
    except:
        print("\n\n#----- Error -----#")
        errorLogName = fileName("log/errorLog", "txt")
        print("Error Log File : " + errorLogName)
        print(traceback.format_exc())
        saveLog(errorLogName, time.time(), "Error")
        saveLog(errorLogName, traceback.format_exc())
        saveLog(errorLogName, "\n")
    finally:
        motor.stop()
        adc.Cleanup()
        print("\n#----- Exit program -----#\n\n")
