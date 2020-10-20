from ev3dev2.motor import OUTPUT_A, OUTPUT_B, MoveTank, SpeedPercent, follow_for_ms
from ev3dev2.sensor.lego import ColorSensor
import ev3dev.ev3 as ev3
import signal

tank = MoveTank(OUTPUT_A, OUTPUT_B)

colorSensorFollow = ev3.ColorSensor('in4')
colorSensorStop = ev3.ColorSensor('in3')
assert colorSensorFollow.connected, "LightSensorFollow(ColorSensor) is not connected"
assert colorSensorStop.connected, "LightSensorFollow(ColorSensor) is not connected"

tank.cs = colorSensorFollow

# setup gracefully shutdown
def signal_handler(sig, frame):
    tank.stop()
    print('Shutting down gracefully')
    exit(0)


signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C to exit')

# Follow the line for 4500ms
while (colorSensorStop.value() > 40):
    tank.follow_line(
        kp=1, ki=0, kd=0,
        speed=SpeedPercent(10),
        target_light_intensity=37,
        follow_left_edge = False,
        white=80,
        off_line_count_max=20000000000,
        sleep_time=0.001,
        follow_for=follow_for_ms,
        ms = 10
    )

print("stop")
