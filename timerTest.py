import time

mint = 60
timer = mint

while (timer != 0):
    timer = timer-1
    time.sleep(1)
    if timer == 50:
        print('you are running out of time')
        timer.cancel()
    print(f'you finished on {timer} seconds')

