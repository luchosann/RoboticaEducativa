from random import random
import sys
sys.path.insert(0, '/usr/share/sugar/activities/TurtleBots.activity/plugins/butia')
import random
from pybot import usb4butia
import time

robot = usb4butia.USB4Butia()


estado = "linea"
# negroIzq = 28000
# negroDer = 24000
pGrisDer=1
pGrisIzq=6

negroIzq = robot.getGray(pGrisIzq) + 2000
negroDer = robot.getGray(pGrisDer) + 2000

blancoIzq = 26000
blancoDer = 33000

def seguidor_linea():
        print("Izq:  " + str(robot.getGray(pGrisIzq)))
        print("Der:  " + str(robot.getGray(pGrisDer)))    

        if robot.getGray(pGrisIzq) > negroIzq:
            print("si")
            robot.set2MotorSpeed(1, 200, 0 , 200)
            time.sleep(0.1)
        elif robot.getGray(pGrisDer) > negroDer:
            print("si")
            robot.set2MotorSpeed(0, 200, 1 , 200)
            time.sleep(0.1)

        robot.set2MotorSpeed(1, 500, 1 , 500)

def rotar():
    robot.set2MotorSpeed(0, 500, 0 , 500)#atras
    time.sleep(1)
    robot.set2MotorSpeed(1, 500, 0 , 500)
    time.sleep(random.randrange(1,3))


def cajas():
    print("1: "+ str(robot.getGray(pGrisIzq)))
    print("2:" + str(robot.getGray(pGrisDer)))

    if(robot.getGray(pGrisIzq) > blancoIzq and robot.getGray(pGrisDer) > blancoDer):
        robot.set2MotorSpeed(1, 400, 1 ,400) #adelante
    else:
        time.sleep(0.4)
        rotar()

def color():
    global estado
    if (robot.getGray(pGrisDer) >= negroDer and robot.getGray(pGrisIzq) >= negroIzq):
        estado = "cajas"
        time.sleep(2)

while True:
    if (estado == "linea"):
        color()
        seguidor_linea()
        print(estado)
    elif (estado == "cajas"):
        print("cajas")
        cajas()

