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

        i = 0
        while i < len(actions):
            temp_action = ""

            if(actions[i] == "."):
                if i < len(actions) - 2:
                    if not actions[i + 2] == '.':
                        temp_action = "fb"
                    elif i < len(actions) - 3: 
                        if not actions[i + 1 ] not actions[i + 3]: 
                            temp_action = "FB
                else:
                    temp_action = "f"

                i = i + 1
            if not current_direction == actions[i]:
                expanded_list_actions = expanded_list_actions + self.get_action(current_direction, actions[i])
            expanded_list_actions = expanded_list_actions + 'f' + temp_action
            current_direction = actions[i]
            i = i + 1

        return expanded_list_actions

    def get_action(self, current_direction, wanted_direction):
        """
        docstring
        """
        if current_direction == "d" and wanted_direction == "u" or current_direction == "u" and wanted_direction == "d":
            return "t"
        elif current_direction == "r" and wanted_direction == "l" or current_direction == "l" and wanted_direction == "r":
            return "t"
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
            return "r"
        elif current_direction == "d" and wanted_direction == "r":
            return "l"

def test_decoder():
    DEFINED_ACTIONS = ['l', 'r', 'b', 'f']
    decoder = Decoder('llll.uddllu.r.r.r.r.rdr.u.uruulld.r.rlddllu.luulld.rur.d.dull.d.rd.r.r.rdr.u.uruurrd.lul.dulld.rddlllluur.dld.r.r.rdr.u.udlllldllu.r.r.r.r.rdr.u', DEFINED_ACTIONS)

    print(decoder.actions)
    test = 1
    # while test != -1:
    #     test = decoder.get_next_action()
    #     print(test)


if __name__ == "__main__":
    test_decoder()
