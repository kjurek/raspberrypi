# https://youtu.be/8tpHbQwsIu4 

from gpiozero import LED
from time import sleep

led = LED(14)
while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
