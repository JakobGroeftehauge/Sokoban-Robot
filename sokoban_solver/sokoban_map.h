#ifndef SOKOBAN_MAP_H
#define SOKOBAN_MAP_H

#include <vector>
#include <string>
#include "sokoban_state.h"

static int _dummy_var;

class sokoban_map
{
public:
    sokoban_map(std::vector<std::vector<char>> map, std::vector<coordinate> storage_zones);
    bool map_completed(sokoban_state state);
    bool next_state(sokoban_state current_state, std::string action, sokoban_state &next_state);
    void print_map(sokoban_state state);
    // Attributes
    std::vector<std::vector<char>> map;
    std::vector<coordinate> storage_zones;


private:
    bool valid_map();
    bool valid_position(coordinate position);
    bool on_top_box(coordinate position, std::vector<coordinate> box_positions, int &out_box_index = _dummy_var);
};

#endif // SOKOBAN_MAP_H
