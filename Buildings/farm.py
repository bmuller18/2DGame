import time
import Buildings.my_resources


grow = False
grainTime = 0
def grain():
    time.sleep(2)
    Buildings.my_resources.grain = Buildings.my_resources.grain + 1
    print(Buildings.my_resources.grain)