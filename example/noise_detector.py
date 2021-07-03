# Add your Python code here. E.g.
from microbit import pin1, pin2
import neopixel as np

NUM = 24
ring = np.NeoPixel(pin2, NUM)

def noise(pin=pin1, num=NUM, max_num=1024):
    n = pin.read_analog()
    step = max_num // NUM
    m = n // step
    for i in range(m):
        ring[i] = (100, 0, 0)
    ring.show()
    ring.clear()

while True:
    noise()
  
# EOF.
