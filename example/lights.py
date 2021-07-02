# Add your Python code here. E.g.
from microbit import display, sleep, pin2
import neopixel as np
from random import randint

def my_display(x_num=5, y_num=5, L=9, delay=200):
    for y in range(y_num):
        for x in range(x_num):
            display.set_pixel(x, y, L)
            sleep(delay)
    display.clear()

def my_ring(pin=pin2, num=24, delay=200, max_value=10):
    ring = np.NeoPixel(pin, num)
    for i in range(num):
        r = randint(0, max_value)
        g = randint(0, max_value)
        b = randint(0, max_value)
        ring[i] = (r, g, b)
        ring.show()
        sleep(delay)
    ring.clear()

RI = 0
def both_v1(pin=pin2, num=24, delay=200, max_value=10):
    global RI
    x_num = 5
    y_num = 5
    L = 9
    ring = np.NeoPixel(pin, num)
    for y in range(y_num):
        for x in range(x_num):
            display.set_pixel(x, y, L)
            r = randint(0, max_value)
            g = randint(0, max_value)
            b = randint(0, max_value)
            ring[RI] = (r, g, b)
            ring.show()
            sleep(delay)
            RI = RI + 1
            if RI >= num:
                RI = 0
    display.clear()

X = 0
Y = 0
def one_mbit_led(x_num=5, y_num=5, L=9):
    global X, Y
    display.set_pixel(X, Y, L)
    X = X + 1
    if X >= x_num:
        Y = Y + 1
        X = 0
    if Y >= y_num:
        Y = 0
        display.clear()

I = 0
NUM = 24
RING = np.NeoPixel(pin2, NUM)
def one_ring_led(max_value=10):
    global I, NUM, RING
    r = randint(0, max_value)
    g = randint(0, max_value)
    b = randint(0, max_value)
    RING[I] = (r, g, b)
    RING.show()
    I = I + 1
    if I >= NUM:
        I = 0
        RING.clear()

func_list = [my_display, my_ring]

while True:
    #both_v1()
    one_mbit_led()
    one_ring_led()
    sleep(200)
  
# EOF.
