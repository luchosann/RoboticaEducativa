import sys
sys.path.insert(0, '/usr/share/sugar/activities/TurtleBots.activity/plugins/butia')

from pybot import usb4butia

robot = usb4butia.USB4Butia()
robot.set2MotorSpeed(0, 0, 0 , 0)
