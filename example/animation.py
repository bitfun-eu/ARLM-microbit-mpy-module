from microbit import display, sleep

A = [
        [0, 0, 0, 0, 0],
        [0, 0, 9, 0, 0],
        [0, 0, 9, 0, 0],
        [0, 9, 0, 9, 0],
        [0, 0, 0, 0, 0],
    ]

def show(a):
    for y, row in enumerate(a):
        for x, v in enumerate(row):
            display.set_pixel(x, y, v)

show(A)

def move_down(a):
    last_row = a[4]
    a[4] = a[3]
    a[3] = a[2]
    a[2] = a[1]
    a[1] = a[0]
    a[0] = last_row

def move_up(a):
    first_row = a[0]
    a[0] = a[1]
    a[1] = a[2]
    a[2] = a[3]
    a[3] = a[4]
    a[4] = first_row
    
while True:
    move_up(A) # or move_down(A)
    show(A)
    sleep(100)


