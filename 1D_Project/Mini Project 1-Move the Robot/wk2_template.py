#!/usr/bin/python
# -*- coding: utf-8 -*-

from pythymiodw import *

def print_temp(t_celcius):
    """ calculate t_fahrenheit and print both
    """
    t_fahrenheit = t_celcius*9/5 + 32
    print("The temperature reading in Celsius is", round(t_celcius,3), "and Fahrenheit is", round(t_fahrenheit, 3))
def forward(bot, speed, duration):
    """ move both wheels for that duration, and stop
    """
    if speed > 500:
        speed = 500
    elif speed < -500:
        speed = -500

    bot.wheels(speed, speed)
    bot.sleep(duration)

def user_input():
    speed = input("Please input speed (maximum: 500):")
    duration = input("Please input duration:")
    try:
        speed, duration = int(speed), int(duration)
        if duration < 0:
            print("duration cannot be negative, try again")
            return user_input()
        else:
            return speed, duration

    except:
        print("input error, please try again typing an integer")
        return user_input()

robot = ThymioReal() # create an object

############### Start writing your code here ################

# Prompt user to enter speed and duration of movement
v, t = user_input()
# Move according to the specified speed and duration
forward(robot, v, t)
# Read temperature in celcius from the sensor and print it
print_temp(robot.temperature)
########################## end ############################## 

robot.quit() # disconnect the communication