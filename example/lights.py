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

func_list = [my_display, my_ring]

while True:
    for func in func_list:
        func()
  
# EOF.
