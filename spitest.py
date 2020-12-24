import time
import pigpio

# MCP3208から値を取得するクラス


class MCP3208_Class:
    channel = 1
    baud = 50000
    flags = 0

    """コンストラクタ"""

    def __init__(self, pi, ref_volts):
        self.pi = pi
        self.ref_volts = ref_volts
        self.h = pi.spi_open(self.channel, self.baud, self.flags)

    """電圧取得"""

    def GetVoltage(self, ch):
        #c, raw = self.pi.spi_xfer(self.h,[0x6,(8+ch)<<4,0])
        #c, raw = self.pi.spi_xfer(self.h,[0x6,ch<<6,0])
        c, raw = self.pi.spi_xfer(self.h, [1, (8 + ch) << 4, 0])
        print("c: {0} raw: {1}".format(c, raw))
        raw2 = ((raw[1] & 3) << 8) + raw[2]
        volts = (raw2 * self.ref_volts) / float(1023)
        volts = round(volts, 4)
        return volts

    """終了処理"""

    def Cleanup(self):
        self.pi.spi_close(self.h)


"""メイン関数"""
if __name__ == '__main__':
    pi = pigpio.pi()

    if not pi.connected:
        exit(0)

    ADC = MCP3208_Class(pi, ref_volts=3.3)
    try:
        while True:
            volts = ADC.GetVoltage(ch=0)
            print("volts ch0: {:8.2f}".format(volts*3.75))
            volts = ADC.GetVoltage(ch=1)
            print("volts ch1: {:8.2f}".format(volts*2.0))
            #volts = ADC.GetVoltage(ch=2)
            #print("volts ch2: {:8.2f}".format(volts))
            time.sleep(1)
    except KeyboardInterrupt:  # Ctl+Cが押されたらループを終了
        print("\nCtl+C")
    except Exception as e:
        print(str(e))
    finally:
        ADC.Cleanup()
        print("\nexit program")
