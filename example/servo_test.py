from microbit import pin1, sleep

def servo_test(d=10, start=30, end=160):
    for i in range(30, 160):
        pin1.write_analog(i)
        sleep(d)
    for i in range(160, 30, -1):
        pin1.write_analog(i)
        sleep(d)

while True:
    servo_test(20)
