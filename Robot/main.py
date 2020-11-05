import ev3dev.ev3 as ev3
import signal

from  utils.decoder import Decoder
from  utils.behaviours import *
from ev3dev2.motor import OUTPUT_A, OUTPUT_D, MoveDifferential, SpeedRPM
from ev3dev2.wheel import EV3Tire

STUD_MM = 8

# Definition of actions/behvaiours
FORWARD = "f"
FORWARD_GYRO = "f"
BACKWARD = "b"
LEFT = "l"
RIGHT = "r"
ONE_EIGHTY = "t"
NOT_DEFINED = -1

DEFINED_ACTIONS = [FORWARD, LEFT, RIGHT, BACKWARD, ONE_EIGHTY]



def main():
    # Setup input ports
    colorSensorStop = ev3.LightSensor('in1')
    colorSensorLeft = ev3.ColorSensor('in2')
    colorSensorRight = ev3.ColorSensor('in3')


    assert colorSensorStop.connected, "LightSensorStop(ColorSensor) is not connected"
    assert colorSensorLeft.connected, "LightSensorLeft(ColorSensor) is not conected"
    assert colorSensorRight.connected, "LightSensorRight(ColorSensor) is not conected"
    #colorSensorStop.MODE_REFLECT
    #colorSensorLeft.raw
    #colorSensorRight.raw

    # Setup output ports
    mDiff = MoveDifferential(OUTPUT_A, OUTPUT_D, EV3Tire, 15 * STUD_MM)
    mDiff.left_motor.polarity = "normal"
    mDiff.right_motor.polarity = "normal"

    # setup gracefully shutdown
    def signal_handler(sig, frame):
        print('Shutting down gracefully')
        mDiff.stop()
        exit(0)


    signal.signal(signal.SIGINT, signal_handler)
    print('Press Ctrl+C to exit')


    # setup decoder and define chain of actions
    #string_of_actions = "urrruulldddl"
    #string_of_actions = "fffblfrffrfrffb" #"ffffrfrfrfblfflffrflfb"
    string_of_actions = "llll.uddllu.r.r.r.r.rdr.u.uruulld.r.rlddllu.luulld.rur.d.dull.d.rd.r.r.rdr.u.uruurrd.lul.dulld.rddlllluur.dld.r.r.rdr.u.udlllldllu.r.r.r.r.rdr.u"
    #string_of_actions = "lffffrffbtffrffrfrffffffbrflflfffbrflfflfflflfffbtflffrffrflffbrfflfflflffblfrffffbtflfflffblffbrflffffbrflflfffbrflfflfflflffblfrfrffbtfrffrfrffbrflfflfffrffffrffrfrffbrflflffffbrflflfffbtfrfffflfrffrfrffffffbrflflff"
    #string_of_actions = "lfffrfflf"
    #string_of_actions = "l"

    decoder = Decoder(string_of_actions, DEFINED_ACTIONS)


    current_action = decoder.get_next_action()


    while current_action != NOT_DEFINED: # current action == -1 -> no more actions to execute

        if(current_action == FORWARD):
            move_forward(mDiff, colorSensorStop, colorSensorLeft, colorSensorRight)
            current_action = decoder.get_next_action()
        #if(current_action == FORWARD_GYRO):
        #    move_forward_gyro(mDiff, colorSensorStop, colorSensorFollow, gyro)
        #    current_action = decoder.get_next_action()

#        if(current_action == FORWARD):
#            move_forward_dual(mDiff, colorSensorStop, colorSensorLeft, colorSensorRight)
#            current_action = decoder.get_next_action()

        elif(current_action == BACKWARD):
            move_backward(mDiff, colorSensorStop)
            current_action = decoder.get_next_action()

        elif(current_action == ONE_EIGHTY):
            turn_one_eighty(mDiff)
            current_action = decoder.get_next_action()


        elif(current_action == LEFT):
            turn_left(mDiff)
            current_action = decoder.get_next_action()


        elif(current_action == RIGHT):
            turn_right(mDiff)
            current_action = decoder.get_next_action()


        else:
            raise TypeError("No switch case implemented for action/behaviour: {}".format(current_action))


if __name__ == "__main__":
    main()
    mDiff.stop()
