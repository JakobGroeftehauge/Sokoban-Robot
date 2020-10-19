from ev3dev2.motor import OUTPUT_A, OUTPUT_B, MoveTank, SpeedPercent, follow_for_ms
from ev3dev2.sensor.lego import ColorSensor
import ev3dev.ev3 as ev3
import signal

DRIVE_SPEED = 100
THRESHOLD_LINE = 37
STOP_SPEED = 65

tank = MoveTank(OUTPUT_A, OUTPUT_B)

colorSensorFollow = ev3.ColorSensor('in4')
assert colorSensorFollow.connected, "LightSensorFollow(ColorSensor) is not connected"


tank.cs = colorSensorFollow

# setup gracefully shutdown
def signal_handler(sig, frame):
    tank.stop()
    print('Shutting down gracefully')
    exit(0)


signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C to exit')

tank.on(DRIVE_SPEED, DRIVE_SPEED)

while True:
#    print(colorSensorFollow.value())

    if(colorSensorFollow.value() > THRESHOLD_LINE):
        tank.on( DRIVE_SPEED * ((50 - (colorSensorFollow.value() - 37)) * 1/50), DRIVE_SPEED)
    elif(colorSensorFollow.value() < THRESHOLD_LINE):
        tank.on(DRIVE_SPEED, DRIVE_SPEED - DRIVE_SPEED * (30 - (colorSensorFollow.value()-7)) * 1/30)
    else:
        tank.on(DRIVE_SPEED, DRIVE_SPEED)



#7-87
