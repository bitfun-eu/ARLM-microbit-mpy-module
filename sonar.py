from microbit import pin0, pin1
from machine import time_pulse_us
from utime import sleep_us as usleep

def measure(echo=pin0, trigger=pin1, loops=1):
    echo.read_digital()
    r = []
    num = loops
    while num:
        trigger.write_digital(0)
        usleep(5)
        trigger.write_digital(1)
        usleep(30)
        trigger.write_digital(0)
        micros = time_pulse_us(echo, 1)
        if micros == -2:
            #raise Exception("waiting pin to be value 1 timeout")
            pass
        elif micros == -1:
            #raise Exception("waiting pin to be value 0 timeout")
            pass
        elif micros < 0:
            #raise Exception("unknown error")
            pass
        else:
            t_echo = micros / 1000000
            dist_cm = (t_echo / 2) * 34300
            r.append(dist_cm)
            num -= 1

    return sum(r)/loops
