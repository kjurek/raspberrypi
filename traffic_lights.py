# https://youtu.be/QDmiB5WsLUU

from time import sleep
from itertools import cycle
from gpiozero import Button, Buzzer, LED


def led_red_trigger():
    buzzer.on()
    led_red.on()
    sleep(2)
    led_red.off()
    buzzer.off()


def led_yellow_trigger():
    led_yellow.on()
    sleep(1)
    led_yellow.off()

def led_green_trigger():
    led_green.on()
    buzzer.on()
    sleep(0.5)
    buzzer.off()
    sleep(0.5)
    buzzer.on()
    sleep(0.5)
    buzzer.off()
    sleep(0.5)
    buzzer.on()
    sleep(0.5)
    buzzer.off()
    led_green.off()


button = Button(2)
buzzer = Buzzer(15)
led_red = LED(25)
led_yellow = LED(8)
led_green = LED(7)
led_cycle = cycle([led_green, led_yellow, led_red, led_yellow])
led_triggers = {
    led_red: led_red_trigger,
    led_yellow: led_yellow_trigger,
    led_green: led_green_trigger,
}

button.wait_for_active()
for led_current in led_cycle:
    trigger = led_triggers[led_current]
    trigger()
