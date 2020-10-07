class Decoder:
    def __init__(self, actions, defined_actions):
        self.actions = self.expand_actions(actions)
        self.action_pointer = 0
        self.defined_actions = defined_actions


    def get_next_action(self):
        if(len(self.actions) > self.action_pointer):
            current_action = self.actions[self.action_pointer]
            self.action_pointer += 1

            if current_action not in self.defined_actions:
                raise TypeError("Action {} not defined".format(current_action))

            return current_action
        else: 
            return -1 # No more actions to execute

    def expand_actions(self, actions): 
        return actions


def test_decoder():
    DEFINED_ACTIONS = ['l', 'r', 't']
    decoder = Decoder("flrflr", DEFINED_ACTIONS)
    
    test = 1
    while test != -1:
        test = decoder.get_next_action()
        print(test)


if __name__ == "__main__":
    test_decoder()