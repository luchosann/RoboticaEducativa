from random import random
import sys
sys.path.insert(0, '/usr/share/sugar/activities/TurtleBots.activity/plugins/butia')
import random
from pybot import usb4butia
import time

robot = usb4butia.USB4Butia()

boton1 = robot.getButton(1)
boton2 = robot.getButton(2)
boton3 = robot.getButton(3)

numBoton = 0
sonido = 0

def girar(x):
    robot.set2MotorSpeed(0, 200, 1, 200)
    time(x)
    robot.set2MotorSpeed(1, 0, 1, 0)

def adelante(x):
    robot.set2MotorSpeed(1, 200, 1, 200)
    time(x)
    robot.set2MotorSpeed(1, 0, 1, 0) 

def tirar():
    girar = 90
    time(1)
    girar = -90

def botones():
    while numBoton == 0:
        if boton1 == 1:
            numBoton = 1
        if boton2 == 1:
            numBoton = 2
        if boton2 == 1:
            numBoton = 3
        
def reciclar():
    girar(1)
    if numBoton == 1:
        adelante(0)
        tirar()
    if numBoton == 2:
        adelante(1)
        tirar()
    if numBoton == 3:
        adelante(2)
        tirar()


def seguidorDeLinea():
    if robot.getGray() < 38200:
        #Izquierda
        time(0.3)
    if robot.getGray() < 24000:
        #Derecha
        time(0.3)
    
    adelante(0.1)



def main():
    while True:
        seguidorDeLinea()

        if sonido > 7000 and numBoton == 0:
            botones()
        elif sonido > 7000:
            time(3)

        if robot.getDistance() < 12 and numBoton != 0:
            reciclar()
            numBoton = 0