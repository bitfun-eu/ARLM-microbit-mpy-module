from microbit import pin1, sleep

def servo_test(d=10, start=30, end=160, step=10):
    for i in range(start, end, step):
        pin1.write_analog(i)
        sleep(d)
    for i in range(end, start, -step):
        pin1.write_analog(i)
        sleep(d)

while True:
    servo_test(100, 30, 160, 20)
