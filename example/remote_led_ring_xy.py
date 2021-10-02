from microbit import pin0, pin2, button_a, button_b
from microbit import display, Image
import neopixel as np
import radio

NUM = 24
ring = np.NeoPixel(pin2, NUM)

def send(pin=pin0):
    display.show(Image.HEART)
    n = pin.read_analog()
    # homework: use rocker module, to control both LED count and color
    x = 3
    y = 5
    s = str(x) + " " + str(y)
    s = str(n)
    b = bytes(s, 'utf-8')
    radio.on()
    radio.send(s)
    radio.off()

def receive(max_num=1020):
    display.show(Image.SMILE)
    try:
        radio.on()
        b = radio.receive()
        radio.off()
        s = str(b, 'utf-8')
        x_str, y_str = s.split(" ")
        x = int(x_str)
        y = int(y_str)
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
    # 16:20
    if button_a.was_pressed(): # check 16:20:30
        MODE = 0
    if button_b.was_pressed(): # check if button was pressed before 16:20
        MODE = 1
    # now: 16:15
    if MODE == 0:
        send()
    else:
        receive()
