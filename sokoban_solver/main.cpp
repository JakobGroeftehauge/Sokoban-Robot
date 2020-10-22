#include <iostream>
#include <functional>
#include <string>
#include <unordered_set>
#include <queue>
#include <vector>
#include <algorithm>
#include "node.h"
#include "sokoban_map.h"
#include "Timer.h"

using namespace std;

//std::vector<std::vector<char>> map = {
//    {'X','X','X','X','X','X','X','X','X','X','X','X'},
//    {'X','X','.','.','.','X','.','.','.','.','.','X'},
//    {'X','X','.','.','.','X','.','.','.','.','.','X'},
//    {'X','X','.','.','.','.','X','.','.','X','X','X'},
//    {'X','.','.','.','.','.','.','.','X','X','X','X'},
//    {'X','.','.','.','X','.','.','.','X','X','X','X'},
//    {'X','X','X','X','X','X','X','X','X','X','X','X'}};


///*the reference frame for the coordinates is placed in the top left corner with the positive x-axis
// point downwards and the positive y-axis pointing towards right. The upper left corner is coordinate (0,0)*/
//std::vector<coordinate> storage_zones = {coordinate(2, 7), coordinate(2, 8), coordinate(3, 7), coordinate(3, 8) };

//std::vector<string> actions = {"left", "left", "left", "left", "up", "down", "right", "right", "up", "left", "down", "left", "down", "left", "left", "up", "right", "right", "right", "right", "right", "down", "right", "up", "up", "right", "up", "up", "left", "left", "down", "right", "right", "down", "left", "down", "left", "left", "up", "left", "up", "up", "left", "left", "down", "right", "up", "right", "down", "down",
//                               "right", "down", "left", "left", "down", "left", "left", "up", "right", "right", "right", "right", "right", "down", "right", "up", "up", "right", "up", "up", "left", "left", "down", "right", "up", "right", "down", "up", "right", "right", "down", "left", "up", "left", "left", "down", "down", "down", "left", "left", "up", "left", "up", "left", "down", "right", "down", "left", "down", "left",
//                               "left", "up", "right", "right", "right", "right", "right", "down", "right", "up", "up", "down", "left", "left", "up", "left", "up", "left", "left", "down", "right", "down", "down", "left", "left", "up", "right", "right", "right", "right", "right", "down", "right", "up"};

bool crate_position_not_changed(sokoban_state state1, sokoban_state state2)
{
    for(unsigned int i = 0; i < state1.box_positions.size(); i++)
    {
        bool match_found = false;
        for(unsigned int j = 0; j < state2.box_positions.size(); j++)
        {
            if(state1.box_positions[i] == state2.box_positions[j])
            {
                match_found = true;
                break;
            }
        }
        if(match_found == false)
        {
            return false;
        }
    }
    return true;
}

int main()
{
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


    sokoban_map env(map, storage_zones);

    std::vector<coordinate> box_positions = {coordinate(3, 3), coordinate(3, 4), coordinate(3, 2), coordinate(4, 2)};
    coordinate start_pos(4, 7);

    sokoban_state current_state(start_pos, box_positions);

    std::unordered_set<std::string> prev_expanded_states;
    std::queue<Node*> queue_unexpanded_nodes;

    //Node* root_node;
    Node root_node = Node(&current_state);
    queue_unexpanded_nodes.push(&root_node);

    bool solution_found = false;
    int it = 0;

    Node *completed_node;
    Node* new_node;
    Node *current_node;
    sokoban_state next_state;

    std::vector<string> movements = {"left", "right", "up", "down"};

    Timer timer_breath_first("breath_first");

    do
    {
        current_node = queue_unexpanded_nodes.front();
        //it = it + 1;
        //std::cout<<"unique key: "<< current_node.state.unique_key << std::endl;
        //std::cout << current_node.state << std::endl;

        for(unsigned int i = 0; i < movements.size(); i++)
        {
            //sokoban_state next_state;
            std::string current_move = movements[i];
            bool valid_move = env.next_state(current_node->state, current_move, next_state);

            if(valid_move == true)
            {
                next_state.generate_unique_key();
                if(prev_expanded_states.find(next_state.unique_key) == prev_expanded_states.end())
                {
                    prev_expanded_states.insert(next_state.unique_key);
                    new_node = new Node(&next_state, current_node);
                    it++;
                    //new_node->state.generate_unique_key();
                    current_node->subsequent_states.push_back(new_node);
                    queue_unexpanded_nodes.push(new_node);
                    if(env.map_completed(&next_state))
                    {
                        solution_found = true;
                        completed_node = new_node;
                        break;
                    }
                }
//                else
//                {
//                    //std::cout << "found in dict" << std::endl;
//                }

            }
        }
        queue_unexpanded_nodes.pop();
        //std::cout << !queue_unexpanded_nodes.empty() << " " << !solution_found;
    } while(!solution_found && !queue_unexpanded_nodes.empty());

    //timer_breath_first.~Timer();

    std::cout << "Length of queue: "<< queue_unexpanded_nodes.size() << std::endl;
    std::cout << "Final number of expanded nodes: " << it << std::endl;


    std::vector<char> solution;

    Node* temp_node = completed_node;
    while(temp_node->parent_state != NULL)
    {
        solution.push_back(temp_node->action_to_current_state());
        if(!crate_position_not_changed(temp_node->state, temp_node->parent_state->state))
        {
            solution.push_back('.');
        }
        //std::cout << temp_node->action_to_current_state() << std::endl;
        temp_node = temp_node->parent_state;
    }

    // revert solutions list;
    std::cout << "Number of steps in solution:" << solution.size() << std::endl;

    std::reverse(solution.begin(), solution.end());

    for(unsigned int i = 0; i < solution.size(); i++)
    {
        std::cout << solution[i];
    }
    std::cout << std::endl;

    return 0;
}
