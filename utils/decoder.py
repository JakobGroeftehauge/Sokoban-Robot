class Decoder:
    def __init__(self, actions):
        self.actions = self.expand_actions(actions)
        self.action_pointer = 0
        self.conversion_table = {'f': 0, 'l':1, 'r':2} 


    def get_next_action(self):
        if(len(self.actions) > self.action_pointer):
            current_action = self.actions[self.action_pointer]
            if current_action in self.conversion_table:
                current_action = self.conversion_table[current_action]
            else: 
                raise TypeError("Action not defined")
            self.action_pointer += 1
            return current_action
        else: 
            return -1 # No more actions to execute

    def expand_actions(self, actions): 
        return actions


def test_decoder():
    decoder = Decoder("flrflr")
    
    test = 1 
   
    print(test)
    while test != -1:
        test = decoder.get_next_action()
        print(test)


if __name__ == "__main__":
    test_decoder()