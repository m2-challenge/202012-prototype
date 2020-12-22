import time
import pigpio

# MCP3208から値を取得するクラス


class ADC:
    channel = 1
    baud = 50000
    flags = 0

    def __init__(self, pi, ref_volts):
        """Initialize Motor Class
        Args:
            pi: 
            ref_volts (float): Reference Volt of MCP3208
        """
        self.pi = pi
        self.ref_volts = ref_volts
        self.h = pi.spi_open(self.channel, self.baud, self.flags)

    def GetVoltage(self, ch):
        """Get Voltage
        Args:
            ch (int): Channel of MCP3208
        """
        #c, raw = self.pi.spi_xfer(self.h,[0x6,(8+ch)<<4,0])
        #c, raw = self.pi.spi_xfer(self.h,[0x6,ch<<6,0])
        c, raw = self.pi.spi_xfer(self.h, [1, (8 + ch) << 4, 0])
        #print("c: {0} raw: {1}".format(c, raw))
        raw2 = ((raw[1] & 3) << 8) + raw[2]
        volts = (raw2 * self.ref_volts) / float(1023)
        volts = round(volts, 4)
        return volts

    def Cleanup(self):
        """Cleanup
        """
        self.pi.spi_close(self.h)


if __name__ == '__main__':
    pi = pigpio.pi()

    if not pi.connected:
        exit(0)

    adc = ADC(pi, ref_volts=3.3)
    try:
        while True:
            volts = adc.GetVoltage(ch=0)
            print("volts ch0: {:8.2f}".format(volts))
            volts = ADC.GetVoltage(ch=1)
            print("volts ch1: {:8.2f}".format(volts))
            time.sleep(1)
    except KeyboardInterrupt:  # Ctl+Cが押されたらループを終了
        print("\nCtl+C")
    except Exception as e:
        print(str(e))
    finally:
        adc.Cleanup()
        print("\nexit program")
