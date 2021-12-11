from gpiozero import LEDBarGraph
from time import sleep

led_bar = LEDBarGraph(16, 12, 7, 8, 25, 24, 23, 18, 15, 14)

led_bar.on()
sleep(1)
led_bar.off()

for i in range(1, len(led_bar) + 1):
    led_bar.value = i / len(led_bar)
    sleep(0.5)

for i in range(1, len(led_bar) + 1):
    led_bar.value = -i / len(led_bar)
    sleep(0.5)

led_bar.off()
for idx, led in enumerate(led_bar):
    if idx % 2 == 0:
        led.on()
sleep(1)

led_bar.off()

led_bar.off()
for idx, led in enumerate(led_bar):
    if idx % 2 != 0:
        led.on()
sleep(1)

