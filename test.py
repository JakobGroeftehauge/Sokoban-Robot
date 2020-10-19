#!/usr/bin/python3.4
import ev3dev.ev3 as ev3
from time import sleep

import signal

def bin_val(val, threshold):
    if val > threshold:
        return 1
    else:
        return 0


mL = ev3.LargeMotor('outA')
mR = ev3.LargeMotor('outD')

THRESHOLD_BLACK = 50

BASE_SPEED = 30
TURN_SPEED = 100
STOP_SPEED = 0

lightSensorLeft = ev3.ColorSensor('in1')
lightSensorRight = ev3.ColorSensor('in4')

assert lightSensorLeft.connected, "LightSensorLeft(ColorSensor) is not connected"
assert lightSensorRight.connected, "LightSensorRight(LightSensor) is not conected"


mL.run_direct()
mR.run_direct()


mL.polarity = "normal"
mR.polarity = "normal"

def signal_handler(sig, frame):
	print('Shutting down gracefully')
	mL.duty_cycle_sp = 0
	mR.duty_cycle_sp = 0

	exit(0)

signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C to exit')

lightSensorLeft.raw
lightSensorRight.raw
state = True
mR.duty_cycle_sp = TURN_SPEED
mL.duty_cycle_sp = TURN_SPEED

while state:



    sensorLeft = bin_val(lightSensorLeft.value(), THRESHOLD_BLACK)
    sensorRight = bin_val(lightSensorRight.value(), THRESHOLD_BLACK)
    mR.run_direct
    mL.run_direct

    if sensorRight == 1 and sensorLeft == 1:
        print("sort")
        mR.duty_cycle_sp = STOP_SPEED
        mL.duty_cycle_sp = STOP_SPEED


        ## Distance from brake to line
        #mL.run_to_rel_pos(position_sp = 80, speed_sp=900, stop_action="hold")
        #mR.run_to_rel_pos(position_sp = 80, speed_sp=900, stop_action="hold")

        #mR.wait_until('holding')
        #mL.wait_until('holding')
        #sleep(1)
        ## Rotate 90 degrees
        #mL.run_to_rel_pos(position_sp = -160, speed_sp=900, stop_action="hold")
        #mR.run_to_rel_pos(position_sp = 160, speed_sp=900, stop_action="hold")
        #mR.wait_until('holding')
        #mL.wait_until('holding')


        state = False





#    elif sensorRight == 1 and sensorLeft == 1:
#        mR.duty_cycle_sp = TURN_SPEED
#        mL.duty_cycle_sp = TURN_SPEED
#    elif sensorRight == 1 and sensorLeft == 0:
#        mL.duty_cycle_sp = BASE_SPEED
#        mR.duty_cycle_sp = TURN_SPEED
#    else:
#        mL.duty_cycle_sp = TURN_SPEED
#        mR.duty_cycle_sp = BASE_SPEED
