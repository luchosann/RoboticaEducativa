from ctypes import sizeof
from operator import length_hint
import sys
import time
sys.path.insert(0, '/usr/share/sugar/activities/TurtleBots.activity/plugins/butia')

from pybot import usb4butia

robot = usb4butia.USB4Butia()

# robot.getButton(port)                    # obtiene el valor del sensor botón conectado en el puerto port
# robot.getDistance(port)                  # obtiene el valor del sensor de distancia conectado en el puerto port
# robot.getGray(port)                      # obtiene el valor del sensor de grises conectado en el puerto port
# robot.getLight(port)                     # obtiene el valor del sensor de luz conectado en el puerto port

# prom = []

robot.set2MotorSpeed(0, 500, 0 , 500)

    

# print(prom)


# import statistics

# blanco1B =  [17664, 17664, 17664, 17728, 17664, 17728]
# blanco2B = [17600, 17600, 17600, 17600, 17600, 17600]

# blanco1A = [37312, 37632, 37824, 37504, 37312, 37440]
# blanco2A = [37888, 37888, 37824, 37824, 37824, 37824]

# negro1B = [41408, 41408, 41344, 41344, 41344, 41344]
# negro2B = [42624, 42624, 42624, 42624, 42624, 42560]

# negro1A = [52288, 52160, 52352, 52288, 52160, 52160]
# negro2A = [51648, 51648, 51648, 51648, 51648, 51648]

# gris1B = [29888, 29952, 29952, 29888, 29888, 29888]
# gris2B = [29632, 29696, 29632, 29632, 29632, 29632]

# gris1A = [47040, 47296, 47040, 47040, 47296, 47232]
# gris2A = [47872, 47872, 47872, 47808, 47872, 47808]

# # p1 = statistics.mean(list1)
# print("aca")
# print("\n")
# print(sum(blanco1B)/len(blanco1B))
# print(sum(blanco2B)/len(blanco2B))
# print(sum(blanco1A)/len(blanco1A))
# print(sum(blanco2A)/len(blanco2A))
# print("\n")
# print(sum(negro1B)/len(negro1B))
# print(sum(negro2B)/len(negro2B))
# print(sum(negro1A)/len(negro1A))
# print(sum(negro2A)/len(negro2A))
# print("\n")
# print(sum(gris1B)/len(gris1B))
# print(sum(gris2B)/len(gris2B))
# print(sum(gris1A)/len(gris1A))
# print(sum(gris2A)/len(gris2A))