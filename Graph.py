import pyautogui as mouse
import time
import matplotlib.pyplot as plt

control = True

x = []
y = []
count = 0
t = 1
inc = .1
check1, check2, check3 = 0, 1, 2

mouse.moveTo(960, 540)
while control:
    thing = mouse.position()
    y.append(thing[0] - 960)
    x.append(inc * t)
    if thing[1] > 540 or thing[1] < 540:
        mouse.moveTo(thing[0], 540)
    count += 1
    t += 1
    if count > 2:
        if (y[check2] < y[check1] and y[check2] < y[check3]) or (y[check2] == y[check1] and y[check2] < y[check3]):
            print(f'{y[check2]} is the relative minimum.')
        if (y[check2] > y[check1] and y[check2] > y[check3]) or (y[check2] == y[check1] and y[check2] > y[check3]):
            print(f'{y[check2]} is the relative maximum.')
        check1 += 1
        check2 += 1
        check3 += 1

    if count > 100:
        break
        # control = False
        # plt.plot(x, y)
        # plt.xlabel('time')
        # plt.ylabel('distance turned')
        # plt.show()
    time.sleep(inc)