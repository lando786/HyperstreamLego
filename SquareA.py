#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep

r = LargeMotor('outA') #Assign outA to Right Motor
l = LargeMotor('outB') # Designate outB to be Left Motor

l.run_to_rel_pos(position_sp=2160, speed_sp=900, stop_action="hold")
r.run_to_rel_pos(position_sp=2160, speed_sp=900, stop_action="hold")
#Move left and right at the same time

l.wait_while('running')
r.wait_while('running')

l.run_to_rel_pos(position_sp=360, speed_sp=900, stop_action="hold")
r.run_to_rel_pos(position_sp=-180, speed_sp=900, stop_action="hold")
#Rotate left motor 180 degrees, and right motor 180 degrees in the oposite direction
#noticed the -180 on the right motor

l.wait_while('running')
r.wait_while('running')
l.run_to_rel_pos(position_sp=2160, speed_sp=900, stop_action="hold")
r.run_to_rel_pos(position_sp=2160, speed_sp=900, stop_action="hold")

l.wait_while('running')
r.wait_while('running')

l.run_to_rel_pos(position_sp=360, speed_sp=900, stop_action="hold")
r.run_to_rel_pos(position_sp=-180, speed_sp=900, stop_action="hold")

l.wait_while('running')
r.wait_while('running')
l.run_to_rel_pos(position_sp=2160, speed_sp=900, stop_action="hold")
r.run_to_rel_pos(position_sp=2160, speed_sp=900, stop_action="hold")

l.wait_while('running')
r.wait_while('running')

l.run_to_rel_pos(position_sp=360, speed_sp=900, stop_action="hold")
r.run_to_rel_pos(position_sp=-180, speed_sp=900, stop_action="hold")

l.wait_while('running')
r.wait_while('running')
l.run_to_rel_pos(position_sp=2160, speed_sp=900, stop_action="hold")
r.run_to_rel_pos(position_sp=2160, speed_sp=900, stop_action="hold")

l.wait_while('running')
r.wait_while('running')

l.run_to_rel_pos(position_sp=360, speed_sp=900, stop_action="hold")
r.run_to_rel_pos(position_sp=-180, speed_sp=900, stop_action="hold")

l.wait_while('running')
r.wait_while('running')
