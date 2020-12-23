import time
import datetime
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
        logName = fileName("log/log", "txt")
        now = datetime.datetime.fromtimestamp(time.time())
        saveLog(logName, logname, now.strftime('%Y/%m/%d %H:%M:%S'))

        #--- Main Process ---#
        for i in range(100):
            volt74 = adc.GetVoltage(ch=0) * 3.75
            volt37 = adc.GetVoltage(ch=1) * 2.0
            saveLog(logName, time.time(), i, volt74, volt37)
            time.sleep(0.1)
            print(i)

    except KeyboardInterrupt:
        print("\nKeyboard Interrupt")
    except:
        print(traceback.format_exc())
        errorLogName = fileName("log/errorLog", "txt")
        saveLog(errorLogName, time.time(), "Error")
        saveLog(errorLogName, traceback.format_exc())
        saveLog(errorLogName, "\n")
    finally:
        motor.stop()
        adc.Cleanup()
        print("\nexit program")
