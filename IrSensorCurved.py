#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep #needed for waits

r = LargeMotor('outB') #Assign outA to Right Motor
l = LargeMotor('outA') # Designate outB to be Left Motor
ir = InfraredSensor()
ir.mode = 'IR-PROX'
assert ir.connected, "missing ir sensor"

ts = TouchSensor()
assert ts.connected, "missing touch sensor"

d = 0
while not ts.value():
    d = ir.value()
    if d <= 39 && d >=11
        l.run_forever(speed_sp=900)
        r.run_forever(speed_sp=900)
    if d > 40 :
        l.run_forever(speed_sp=900)
        r.run_forever(speed_sp=600)
    if d < 10:
        l.run_forever(speed_sp=600)
        r.run_forever(speed_sp=900)
    else:
        l.stop()
        r.stop()

Sound.beep()

#Move left and right at the same time make them rotate 2160 degrees, at a speed of 900, 
#and afterwards make an action of 'hold' to apply brakes

sleep(5)   # Give the motor time to move