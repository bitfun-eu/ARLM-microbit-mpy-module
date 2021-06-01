# Need FourDigitDisplay and sonar
from microbit import sleep, pin0, pin1
from FourDigitDisplay import FourDigitDisplay
from sonar import measure

d = FourDigitDisplay()

while True:
    r = measure(pin0, pin1)
    r = int(r)
    d.show(r)
    sleep(100)
