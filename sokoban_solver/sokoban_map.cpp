#pragma once
#include "sokoban_map.h"
#include <iostream>
#include <map>
#include <vector>       // std::vector


std::map<std::string, coordinate> action_to_vector {
    {"left",  coordinate(0, -1)},
    {"right", coordinate(0,  1)},
    {"up",    coordinate(-1,  0)},
    {"down",  coordinate(1, 0)}};

std::vector<int> t = {1, 1};

sokoban_map::sokoban_map(std::vector<std::vector<char>> map, std::vector<coordinate> storage_zones)
{
    this->map = map;
    this->storage_zones = storage_zones;

    if(!valid_map())
    {
        throw "Not valid map!";
    }
}

bool sokoban_map::map_completed(sokoban_state* state)
{
    for(unsigned int i = 0; i < state->box_positions.size(); i++)
    {
        bool match_found = false;
        for(int j = 0; j < this->storage_zones.size(); j++)
        {
            if(state->box_positions[i] == this->storage_zones[j])
            {
                match_found = true;
                continue;
            }
        }

        if(match_found == false)
        {
            return false;
        }
    }
    return true;
}

bool sokoban_map::next_state(sokoban_state current_state, std::string action, sokoban_state& next_state)
{

    coordinate move = action_to_vector[action];

    coordinate new_position = move + current_state.player_postion;

    // Check if new position is valid -> new position is a '.'
    if(!valid_position(new_position))
    {
        return false;
    }

    // Check if new position is on top of box
   int colliding_box_index;
   if(on_top_box(new_position, current_state.box_positions, colliding_box_index))
    {
        coordinate new_position_box = new_position + move;
        if(!valid_position(new_position_box))
        {
            return false;
        }
        else if(on_top_box(new_position_box, current_state.box_positions))
        {
            return false;
        }
        else
        {
            //update box positions
            std::vector<coordinate> updated_box_postions = current_state.box_positions;
            updated_box_postions[colliding_box_index] = new_position_box;
            next_state = sokoban_state(new_position, updated_box_postions);
//            next_state.player_postion = new_position; //coordinate(new_position.x, new_position.y);
//            next_state.box_positions = current_state.box_positions;
//            next_state.generate_unique_key();
            return true;
        }
    }
    else
    {
       next_state = sokoban_state(new_position, current_state.box_positions);
//       next_state.player_postion = new_position;  //coordinate(new_position.x, new_position.y);
//       next_state.box_positions = current_state.box_positions;
//       next_state.generate_unique_key();
       return true;
    }
}

void sokoban_map::print_map(sokoban_state state)
{
    std::vector<std::vector<char>> env = this->map;
    env[state.player_postion.x][state.player_postion.y] = 'M';
    for(int i = 0; i < state.box_positions.size(); i++)
    {
        int x = state.box_positions[i].x;
        int y = state.box_positions[i].y;
        env[x][y] = 'J';
    }

    for(int i = 0; i < env.size(); i++)
    {
        for(int j = 0; j < env[i].size(); j++)
        {
            std::cout << env[i][j];
        }
        std::cout << std::endl;
    }
}

bool sokoban_map::valid_map()
{
    // Check if all map lists in the map vector is equal lenght
    for(int i = 0; i < this->map.size() - 1; i++)
    {
        if(this->map[i].size() != this->map[i +1].size())
        {
            return false;
        }
    }

    // Ensure storage zones is not placed in walls
    for(int i = 0; i < this->storage_zones.size(); i++)
    {
        if(!valid_position(this->storage_zones[i]))
        {
            return false;
        }

        bool identical_pos_found = false;
        for(int j = i + 1; j < this->storage_zones.size(); j++)
        {
            if(this->storage_zones[i] == this->storage_zones[j])
            {
                identical_pos_found = true;
            }
        }
        if(identical_pos_found)
        {
            return false;
        }

    }

    return true;
}

bool sokoban_map::valid_position(coordinate position)
{
    if(map[position.x][position.y] == '.')
    {
        return true;
    }
    else
    {
        return false;
    }
}

bool sokoban_map::on_top_box(coordinate position, std::vector<coordinate> box_positions, int &out_box_index)
{
    for(int i = 0; i < box_positions.size() ; i++)
    {
        if(position == box_positions[i])
        {
            out_box_index = i;
            return true;
        }
    }
    return false;
}

