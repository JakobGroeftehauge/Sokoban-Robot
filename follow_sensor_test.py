import ev3dev.ev3 as ev3
import signal

colorSensorLeft = ev3.ColorSensor('in2')
assert colorSensorLeft.connected, "LightSensorLeft(ColorSensor) is not conected"

f = open("followsensortest.csv", "a")


# setup gracefully shutdown
def signal_handler(sig, frame):
    print('Shutting down gracefully')
    f.close()
    exit(0)




while True:
    f.write(str(colorSensorLeft.value()) + ", ")
    print(colorSensorLeft.value())
