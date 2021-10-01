from microbit import pin0, pin2, button_a, button_b
from microbit import display, Image
import neopixel as np
import radio
radio.on()
NUM = 24
ring = np.NeoPixel(pin2, NUM)

def send(pin=pin0):
    display.show(Image.HEART)
    n = pin.read_analog()
    s = str(n)
    b = s.encode()
    radio.send(b)

def receive(max_num=1020):
    display.show(Image.SMILE)
    try:
        b = radio.receive()
        s = b.decode()
        n = int(s)
    except:
        return
    step = max_num // NUM
    m = n // step
    if m > NUM:
        m = NUM
    for i in range(m):
        ring[i] = (10, 0, 0)
    ring.show()
    ring.clear()

MODE = 0 # 0: send, 1: receive

while True:
    if button_a.was_pressed():
        MODE = 0
    if button_b.was_pressed():
        MODE = 1
    if MODE == 0:
        send()
    else:
        receive()
