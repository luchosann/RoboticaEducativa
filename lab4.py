from ctypes import sizeof
from operator import length_hint
import random
import sys
import time
sys.path.insert(0, '/usr/share/sugar/activities/TurtleBots.activity/plugins/butia')

from pybot import usb4butia

robot = usb4butia.USB4Butia()

prom = []

# robot.set2MotorSpeed(0, 200, 0 , 0)
# robot.getDistance(3)
algoD = 40000
numS = 1
numA = 6

def rotar():
    robot.set2MotorSpeed(0, 500, 0 , 500)#atras
    time.sleep(1)
    robot.set2MotorSpeed(1, 500, 0 , 500)
    time.sleep(random.randrange(1,2))
    

while True:
    print("1: "+ str(robot.getDistance(numS)))
    print("2:" + str(robot.getDistance(numA)))

    if(robot.getDistance(numS) < 55000 and robot.getDistance(numA) < 55000):
        robot.set2MotorSpeed(1, 400, 1 ,400) #adelante
    else:
        rotar()
        




