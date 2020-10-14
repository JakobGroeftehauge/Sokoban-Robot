#include <vector>
#include <algorithm>
#include "sokoban_state.h"

sokoban_state::sokoban_state()
{

}


sokoban_state::sokoban_state(coordinate player_postion, std::vector<coordinate> box_positions)
{
    this->player_postion = player_postion;
    this->box_positions = box_positions;
    generate_unique_key();
}

void sokoban_state::generate_unique_key()
{
    std::vector<coordinate> sorted_box_pos = this->box_positions;
    std::sort(sorted_box_pos.begin(), sorted_box_pos.end());

    std::string temp_string = std::to_string(this->player_postion.x) + std::to_string(this->player_postion.y);

    for(int i = 0; i < sorted_box_pos.size();i++)
    {
        temp_string += std::to_string(sorted_box_pos[i].x) + std::to_string(sorted_box_pos[i].y);
    }
    this->unique_key = temp_string;
}


std::ostream& operator << (std::ostream &os, const sokoban_state &state)
{
    os << "Player pos: {" << state.player_postion.x << ", " << state.player_postion.y << "}  Box pos: ";
    for(unsigned int i = 0; i < state.box_positions.size(); i++)
    {
        os << " {" << state.box_positions[i].x << ", " << state.box_positions[i].y << "},";
    }
    os << std::endl;
    return os;
}
