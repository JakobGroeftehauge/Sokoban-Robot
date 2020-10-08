#ifndef SOKOBAN_STATE_H
#define SOKOBAN_STATE_H

#include <vector>
#include <iostream>
#include "coordinate.h"

class sokoban_state
{
public:
    sokoban_state();
    sokoban_state(coordinate player_postion, std::vector<coordinate> box_positions);
    std::vector<coordinate> box_positions;
    coordinate player_postion;
    friend std::ostream& operator <<(std::ostream& os, const sokoban_state& state);
};

#endif // SOKOBAN_STATE_H
