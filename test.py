#!/usr/bin/python3.4

import ev3dev.ev3 as ev3
from time import sleep

import signal

def bin_value(val, threshold):
    if val > threshold: 
        return 1 
    else 
        return 0 


mL = ev3.LargeMotor('outA')
mR = ev3.LargeMotor('outB')

THRESHOLD_BLACK = 20

BASE_SPEED = -30
TURN_SPEED = -80
STOP_SPEED = 0

lightSensorLeft = ev3.ColorSensor('in1')
lightSensorRight = ev3.ColorSensor('in4') 

assert lightSensorLeft.connected, "LightSensorLeft(ColorSensor) is not connected"
assert lightSensorRight.connected, "LightSensorRight(LightSensor) is not conected"


mB.run_direct()
mA.run_direct()


mA.polarity = "inversed"
mB.polarity = "inversed"

def signal_handler(sig, frame):
	print('Shutting down gracefully')
	mA.duty_cycle_sp = 0
	mB.duty_cycle_sp = 0

	exit(0)

signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C to exit')


while True:
	
    sensorLeft = bin_val(lightSensorLeft.value(), THRESHOLD_BLACK)
	sensorRight = bin_val(lightSensorRight.value(), THRESHOLD_BLACK)
	
    if sensorRight == 0 and sensorRight == 0: 
        # Next state
        mR.duty_cycle_sp = STOP_SPEED
		mL.duty_cycle_sp = STOP_SPEED
    elif sensorRight == 1 and sensorRight == 1:
        mR.duty_cycle_sp = TURN_SPEED
		mL.duty_cycle_sp = TURN_SPEED
    elif sensorRight == 1 and sensorRight == 0: 
        mR.duty_cycle_sp = BASE_SPEED
		mL.duty_cycle_sp = TURN_SPEED
    else sensorRight == 0 and sensorRight == 1: 
        mR.duty_cycle_sp = TURN_SPEED
		mL.duty_cycle_sp = BASE_SPEED


	
	
