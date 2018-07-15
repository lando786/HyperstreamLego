#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep #needed for waits

r = LargeMotor('outA') #Assign outA to Right Motor
l = LargeMotor('outB') # Designate outB to be Left Motor

l.run_to_rel_pos(position_sp=2160, speed_sp=900, stop_action="hold")
r.run_to_rel_pos(position_sp=2160, speed_sp=900, stop_action="hold")
#Move left and right at the same time make them rotate 2160 degrees, at a speed of 900, 
#and afterwards make an action of 'hold' to apply brakes

sleep(5)   # Give the motor time to move