class Decoder:
    def __init__(self, actions, defined_actions):
        self.actions = self.expand_actions(actions)
        self.action_pointer = 0
        self.defined_actions = defined_actions


    def get_next_action(self):
        if(len(self.actions) > self.action_pointer):
            current_action = self.actions[self.action_pointer]
            self.action_pointer += 1
            print(current_action)
            if current_action not in self.defined_actions:
                raise TypeError("Action {} not defined".format(current_action))

            return current_action
        else:
            return -1 # No more actions to execute

    def expand_actions(self, actions, initial_direction='u'):
        expanded_list_actions = ""
        current_direction = initial_direction
        for i in range(len(actions)):  
            # If actions is c. The can is being manipulated. take care of.  

            if not current_direction == actions[i]: 
                expanded_list_actions = expanded_list_actions + self.get_action(current_direction, actions[i])
            expanded_list_actions = expanded_list_actions + 'f'
            current_direction = actions[i]
        
        return expanded_list_actions

    def get_action(self, current_direction, wanted_direction):
        """
        docstring
        """
        if current_direction == "d" and wanted_direction == "u" or current_direction == "u" and wanted_direction == "d":
            return "rr"
        elif current_direction == "r" and wanted_direction == "l" or current_direction == "l" and wanted_direction == "r":
            return "rr" 
        elif current_direction == "r" and wanted_direction == "u":
            return "l"
        elif current_direction == "r" and wanted_direction == "d":
            return "r"
        elif current_direction == "l" and wanted_direction == "u":
            return "r"
        elif current_direction == "l" and wanted_direction == "d":
            return "l"
        elif current_direction == "u" and wanted_direction == "r":
            return "r"
        elif current_direction == "u" and wanted_direction == "l":
            return "l"
        elif current_direction == "d" and wanted_direction == "l":
            return "l"
        elif current_direction == "d" and wanted_direction == "r":
            return "r" 
    
def test_decoder():
    DEFINED_ACTIONS = ['l', 'r', 'u', 'd', 'f']
    decoder = Decoder("llrrurur", DEFINED_ACTIONS)

    print(decoder.actions)
    test = 1
    while test != -1:
        test = decoder.get_next_action()
        print(test)


if __name__ == "__main__":
    test_decoder()
