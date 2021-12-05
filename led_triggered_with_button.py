# https://youtu.be/4F41YkUmq7c

from gpiozero import LED
from time import sleep
from gpiozero import Button

button = Button(2)
led = LED(25)

while True:
    button.wait_for_active()
    print('Button pressed')
    led.on()
    sleep(3)
    led.off()