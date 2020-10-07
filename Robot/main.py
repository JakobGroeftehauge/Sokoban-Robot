import ev3dev.ev3 as ev3
import signal 

from  utils.decoder import Decoder
from  utils.behaviours import *



# Definition of actions/behvaiours
FORWARD = "f"
LEFT = "l"
RIGHT = "r"
NOT_DEFINED = -1

DEFINED_ACTIONS = [FORWARD, LEFT, RIGHT]



def main():
    # Setup input ports 
    lightSensorLeft = ev3.ColorSensor('in1')
    lightSensorRight = ev3.ColorSensor('in4') 

    assert lightSensorLeft.connected, "LightSensorLeft(ColorSensor) is not connected"
    assert lightSensorRight.connected, "LightSensorRight(LightSensor) is not conected"


    # Setup output ports 
    mL = ev3.LargeMotor('outA')
    mR = ev3.LargeMotor('outB')

    mL.run_direct()
    mR.run_direct()


    mL.polarity = "inversed"
    mR.polarity = "inversed"

    # setup gracefully shutdown
    def signal_handler(sig, frame):
        print('Shutting down gracefully')
        mL.duty_cycle_sp = 0
        mR.duty_cycle_sp = 0
        exit(0)

    
    signal.signal(signal.SIGINT, signal_handler)
    print('Press Ctrl+C to exit')


    # setup decoder and define chain of actions
    string_of_actions = "flfrl"
    decoder = Decoder(string_of_actions, DEFINED_ACTIONS)


    current_action = decoder.get_next_action()

    while current_action != NOT_DEFINED: # current action == -1 -> no more actions to execute
        
        if(current_action == FORWARD):
            move_forward()
            current_action = decoder.get_next_action()
            

        elif(current_action == LEFT): 
            turn_left()
            current_action = decoder.get_next_action()
            

        elif(current_action == RIGHT): 
            turn_right() 
            current_action = decoder.get_next_action()
            
            
        else: 
            raise TypeError("No switch case implemented for action/behaviour: {}".format(current_action))
       

if __name__ == "__main__":
    main()
