#include <iostream>
#include "sokoban_map.h"

using namespace std;

std::vector<std::vector<char>> map = {
    {'X','X','X','X','X','X','X','X','X','X','X','X'},
    {'X','X','.','.','.','X','.','.','.','.','.','X'},
    {'X','X','.','.','.','X','.','.','.','.','.','X'},
    {'X','X','.','.','.','.','X','.','.','X','X','X'},
    {'X','.','.','.','.','.','.','.','X','X','X','X'},
    {'X','.','.','.','X','.','.','.','X','X','X','X'},
    {'X','X','X','X','X','X','X','X','X','X','X','X'}};


/*the reference frame for the coordinates is placed in the top left corner with the positive x-axis
 point downwards and the positive y-axis pointing towards right. The upper left corner is coordinate (0,0)*/
std::vector<coordinate> storage_zones = {coordinate(2, 7), coordinate(2, 8), coordinate(3, 7), coordinate(3, 8) };

std::vector<string> actions = {"left", "left", "left", "left", "up", "down", "right", "right", "up", "left", "down", "left", "down", "left", "left", "up", "right", "right", "right", "right", "right", "down", "right", "up", "up", "right", "up", "up", "left", "left", "down", "right", "right", "down", "left", "down", "left", "left", "up", "left", "up", "up", "left", "left", "down", "right", "up", "right", "down", "down",
                               "right", "down", "left", "left", "down", "left", "left", "up", "right", "right", "right", "right", "right", "down", "right", "up", "up", "right", "up", "up", "left", "left", "down", "right", "up", "right", "down", "up", "right", "right", "down", "left", "up", "left", "left", "down", "down", "down", "left", "left", "up", "left", "up", "left", "down", "right", "down", "left", "down", "left",
                               "left", "up", "right", "right", "right", "right", "right", "down", "right", "up", "up", "down", "left", "left", "up", "left", "up", "left", "left", "down", "right", "down", "down", "left", "left", "up", "right", "right", "right", "right", "right", "down", "right", "up"};


int main()
{
    sokoban_map env(map, storage_zones);

    std::vector<coordinate> box_positions = {coordinate(3, 3), coordinate(3, 4), coordinate(3, 2), coordinate(4, 2)};
    coordinate start_pos(4, 7);

    sokoban_state current_state(start_pos, box_positions);

    for(unsigned int i = 0; i < actions.size(); i++)
    {
        sokoban_state next_state;
        bool valid_move = env.next_state(current_state, actions[i], next_state);
        std::cout << "valid: " <<valid_move <<" "<< current_state;
        current_state = next_state;
    }

    std::cout << "Map completed: "<< env.map_completed(current_state) << std::endl;

    env.print_map(current_state);

    return 0;
}
