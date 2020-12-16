import time
import pigpio

slct = 0  # +1 +1 # SPI接続機器の番号 chip select
baud = 50000     # 通信速度
flag = 0  # +256  # bin(256) = 0b100000000 は Aux SPI の利用フラグ
adch = 0         # MCP3208のCH0の番号

pi = pigpio.pi()
hndl = pi.spi_open(slct, baud, flag)  # デバイスオープン

try:
    while True:
        cmnd = (0b00011000 + adch) << 2
        c, raw = pi.spi_xfer(hndl, [cmnd, 0, 0])  # 最初の要素が命令の入力
        #
        #    [0][1][1][D2][D1][D0][0][0]
        #        |  |   |   |   |
        #        |  |  読み出しチャネルの指定
        #        | 1: シングルエンド
        #       [スタートビット]
        #
        data = ((raw[1] & 0b11111111) << 4) + \
               ((raw[2] & 0b11110000) >> 4)
        print(c, raw, bin(data), data)
        time.sleep(1)

except KeyboardInterrupt:
    pi.spi_close(hndl)
    pi.stop()
