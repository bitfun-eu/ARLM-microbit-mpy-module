# Note: code NOT tested, for Constantin to check out
from tinybit import measure
from utime import ticks_ms, ticks_diff
import display
from microbit import button_a

D = 40 # 40 cm
T = 3000 # 3 seconds -> 3000 ms
start = None
end = None
N = 0

while True:
    d = measure()
    display.show(N)
    if button_a.is_pressed():
        N = 0
    if (d < D) and (start is None):
        start = ticks_ms()
    elif (d < D) and (start is not None): # time measurement started
        end = ticks_ms()
        delta = ticks_diff(end, start)
        if delta > T:
            print("too close ....")
            N = N + 1
            # start beep
    else:
        start = None
        end = None
        # stop beep
     
