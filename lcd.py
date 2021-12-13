# simplified example from https://raw.githubusercontent.com/UCTRONICS/Arducam_Starter_Kit_Python_Code_for_RPi/master/11_lcd1602.py
# https://youtu.be/28xGHZE9yts

from gpiozero import OutputDevice
from time import sleep


class LCD:
    CLEARDISPLAY = 0x01
    ENTRYMODESET = 0x04
    ENTRYLEFT = 0x02
    ENTRYSHIFTDECREMENT = 0x00

    def __init__(self, pins_memory=[23, 18, 15, 14], pin_e=24, pin_rs=25):
        self.pins_memory = [OutputDevice(p) for p in pins_memory]
        self.pin_e = OutputDevice(pin_e)
        self.pin_rs = OutputDevice(pin_rs)

        self.write_bits(0x33) # initialization
        self.write_bits(0x32) # initialization
        self.write_bits(0x28) # 2 line 5x7 matrix
        self.write_bits(0x0C) # turn cursor off 0x0E to enable cursor
        self.write_bits(0x06) # shift cursor right
        self.write_bits(self.ENTRYMODESET | self.ENTRYLEFT | self.ENTRYSHIFTDECREMENT)
        self.clear()

    @staticmethod
    def sleep_microseconds(microseconds):
        MICROSECOND = .000001
        sleep(microseconds * MICROSECOND)

    def pulse_enable(self):
        self.pin_e.off()
        self.sleep_microseconds(1)
        self.pin_e.on()
        self.sleep_microseconds(1)
        self.pin_e.off()
        self.sleep_microseconds(1)

    def write_bits(self, bits, char_mode=False):
        self.sleep_microseconds(1000)
        self.pin_rs.value = char_mode
        reversed_pins = list(reversed(self.pins_memory))

        for p in reversed_pins:
            p.off()

        bits = bin(bits)[2:].zfill(8)
        for i, pin in zip(range(4), reversed_pins):
            if bits[i] == "1":
                pin.on()

        self.pulse_enable()

        for p in reversed_pins:
            p.off()

        for i, pin in zip(range(4,8), reversed_pins):
            if bits[i] == "1":
                pin.on()

        self.pulse_enable()

    def clear(self):
        self.write_bits(self.CLEARDISPLAY)
        self.sleep_microseconds(3000)

    def message(self, text):
        for c in text:
            if c == '\n':
                self.write_bits(0xC0) # next line
            else:
                self.write_bits(ord(c), char_mode=True)

if __name__ == '__main__':
    lcd = LCD()
    lcd.clear()
    lcd.message('Hello LCD')
    try:
        while True:
            sleep(0.5)
    finally:
        lcd.clear()
