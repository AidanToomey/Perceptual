import pyautogui as mouse
import time
import matplotlib.pyplot as plt

screenY = 540

#x = []
#y = []
#count = 0
#t = 1
#inc = .1
#check1, check2, check3 = 0, 1, 2

# Set mouse to point 0 
mouse.moveTo(0, screenY)

while True:
    pValues = mouse.position()

    #----->-> RESET MOUSE POSITION

    # This code assumes the screen being used is 
    # 1920 x 1080. See solutions at later date.

    if pValues[0] >= 1910: mouse.moveTo(1, screenY)
    if pValues[0] <= 0: mouse.moveTo(1919, screenY)


"""
    count += 1
    t += 1
    if count > 2:
        if (y[check2] < y[check1] and y[check2] < y[check3]) or (y[check2] == y[check1] and y[check2] < y[check3]):
            print(f'{y[check2]} is the relative minimum.')
            continue
        if (y[check2] > y[check1] and y[check2] > y[check3]) or (y[check2] == y[check1] and y[check2] > y[check3]):
            print(f'{y[check2]} is the relative maximum.')
            continue
        check1 += 1
        check2 += 1
        check3 += 1

    if count > 200:
        control = False
        plt.plot(x, y)
        plt.xlabel('time')
        plt.ylabel('distance turned')
        plt.show()
    time.sleep(inc)
"""