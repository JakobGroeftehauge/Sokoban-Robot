#ifndef NODE_H
#define NODE_H

#include <vector>
#include "sokoban_state.h"


class Node
{
public:
    Node();
    Node(sokoban_state* state);
    Node(sokoban_state* state, Node* parent_state);
    char action_to_current_state();

    // Attributes
    Node* parent_state = NULL;
    sokoban_state state;
    std::vector<Node*> subsequent_states;
};

#endif // NODE_H
