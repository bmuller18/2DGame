import time


grow = False
grainTime = 0
def grain():
    global grainTime
    grow = True
    if grow == True:
        for i in range(5,0,-1):
            time.sleep(1)
        grainTime = grainTime + 1
        print(grainTime)
    grow = False