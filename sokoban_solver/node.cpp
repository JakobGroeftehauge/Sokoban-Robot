#include "node.h"
#include "sokoban_state.h"

Node::Node()
{
}

Node::Node(sokoban_state* state)
{
    this->state = sokoban_state(state->player_postion, state->box_positions);
}

Node::Node(sokoban_state* state, Node* parent_state)
{
    this->state = sokoban_state(state->player_postion, state->box_positions);;
    this->parent_state = parent_state;
}

char Node::action_to_current_state()
{
    if(this->parent_state != NULL)
    {
        sokoban_state parent_state = this->parent_state->state;
        int x = this->state.player_postion.x - parent_state.player_postion.x;
        int y = this->state.player_postion.y - parent_state.player_postion.y;

        if(x == 1)
        {
            return 'd';
        }
        else if(x == -1)
        {
            return 'u';
        }
        else if(y == 1)
        {
            return 'r';
        }
        else if(y == -1)
        {
            return 'l';
        }
        else
        {
            return 'e';
        }
    }
    else
    {
        throw("ERROR: parent state is nullptr");
    }
}
