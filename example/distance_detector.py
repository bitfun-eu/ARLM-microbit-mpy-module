# Note: code NOT tested, for Constantin to check out
from tinybit import measure
from utime import ticks_ms, ticks_diff

D = 40 # 40 cm
T = 3000 # 3 seconds -> 3000 ms
start = None
end = None

while True:
    d = measure()
    if (d < D) and (start is None):
        start = ticks_ms()
    elif (d < D) and (start is not None): # time measurement started
        end = ticks_ms()
        delta = ticks_diff(end, start)
        if delta > T:
            print("too close ....")
            # start beep
    else:
        start = None
        end = None
        # stop beep
