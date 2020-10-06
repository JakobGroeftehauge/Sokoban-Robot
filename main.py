from  utils.decoder import Decoder
from  utils.behaviours import *

def main():
    string_of_actions = "flfrl"
    decoder = Decoder(string_of_actions)

    current_action = decoder.get_next_action()

    while current_action != -1:
       current_action = -1 

    print("test")



if __name__ == "__main__":
    main()
