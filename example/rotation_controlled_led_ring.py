from microbit import pin0, pin1, pin2
import neopixel as np

NUM = 24
ring = np.NeoPixel(pin2, NUM)

def rotation_control(pin=pin0, num=NUM, max_num=1000):
    n = pin.read_analog()
    m = int(n*NUM/max_num)
    if m > NUM: m = NUM
    for i in range(m):
        ring[i] = (10, 0, 0)
    ring.show()
    ring.clear()

while True:
    rotation_control()
