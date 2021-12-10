# https://youtu.be/frWN6z5Ls2g

from gpiozero import OutputDevice
from time import sleep

# for some reason my pins are working in inverted way, not sure why but this helps
dot = OutputDevice(4, active_high=False)
a = OutputDevice(17, active_high=False)
b = OutputDevice(18, active_high=False)
c = OutputDevice(27, active_high=False)
d = OutputDevice(22, active_high=False)
e = OutputDevice(23, active_high=False)
f = OutputDevice(24, active_high=False)
g = OutputDevice(25, active_high=False)

mapping = {
    0: [a, b, c, d, e, f],
    1: [b, c],
    2: [a, b, g, e, d],
    3: [a, b, g, c, d],
    4: [f, g, b, c],
    5: [a, f, g, c, d],
    6: [a, f, e, d, c, g, dot],
    7: [a, b, c],
    8: [a, b, c, d, e, f, g],
    9: [f, a, b, g, c, d],
    'A': [a, f, b, g, e, c],
    'B': [a, b, c, d, e, f, g, dot],
    'C': [a, f, e, d],
    'D': [a, b, c, d, e, f, dot],
    'E': [a, f, g, e, d],
    'F': [a, f, g, e]
}


def reset():
    for dev in [dot, a, b, c, d, e, f, g]:
        dev.off()

for value, devices in mapping.items():
    reset()
    for dev in devices:
        dev.on()
    sleep(1)

reset()