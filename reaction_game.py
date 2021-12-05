# https://youtu.be/qFy4IB8xudo

from gpiozero import LED
from time import sleep
from gpiozero import Button
from enum import Enum, auto
import random

class State(Enum):
    NOT_STARTED = auto()
    STARTED = auto()
    FINISHED = auto()

class Game:
    button_blue = Button(14)
    button_red = Button(23)
    button_yellow = Button(25)
    led_blue = LED(15)
    led_red = LED(18)
    led_yellow = LED(24)

    def __init__(self) -> None:
        self.button_blue.when_activated = self._trigger_blue
        self.button_red.when_activated = self._trigger_red
        self.button_yellow.when_activated = self._trigger_yellow
        self.reset()

    def reset(self):
        self.state = State.NOT_STARTED
        self.winner = None
        self.led_red.off()
        self.led_blue.off()
        self.led_yellow.off()

    def _trigger_blue(self):
        if self.state == State.STARTED:
            self.state = State.FINISHED
            self.winner = 'Blue'
            self.led_blue.on()

    def _trigger_red(self):
        self.reset()
        sleep(random.randint(1, 10))
        self.state = State.STARTED
        self.led_red.on()

    def _trigger_yellow(self):
        if self.state == State.STARTED:
            self.state = State.FINISHED
            self.winner = 'Yellow'
            self.led_yellow.on()

game = Game()
while True:
    sleep(.1)