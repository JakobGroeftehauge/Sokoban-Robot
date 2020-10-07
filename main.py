from  utils.decoder import Decoder
from  utils.behaviours import *

# Definition of actions/behvaiours
FORWARD = "f"
LEFT = "l"
RIGHT = "r"
NOT_DEFINED = -1

DEFINED_ACTIONS = [FORWARD, LEFT, RIGHT]



def main():
    string_of_actions = "flfrl"
    decoder = Decoder(string_of_actions, DEFINED_ACTIONS)

    current_action = decoder.get_next_action()

    while current_action != NOT_DEFINED: # current action == -1 -> no more actions to execute
        
        if(current_action == FORWARD):
            move_forward()
            print(current_action)
            current_action = decoder.get_next_action()
            

        elif(current_action == LEFT): 
            turn_left()
            print(current_action)
            current_action = decoder.get_next_action()
            

        elif(current_action == RIGHT): 
            turn_right() 
            print(current_action)
            current_action = decoder.get_next_action()
            
            
        else: 
            raise TypeError("No switch case implemented for action/behaviour: {}".format(current_action))
       



if __name__ == "__main__":
    main()
