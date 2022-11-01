from ctypes import sizeof
from operator import length_hint
import sys
import time
sys.path.insert(0, '/usr/share/sugar/activities/TurtleBots.activity/plugins/butia')

from pybot import usb4butia

robot = usb4butia.USB4Butia()

prom = []

while len(prom) <= 50:
    print(robot.getDistance(6))
    prom.append(robot.getDistance(6))
    time.sleep(0.1)
    

print(prom)
print("prom: " + str(sum(prom)/len(prom)))
print("max: " + str(max(prom)))
print("min: " + str(min(prom)))