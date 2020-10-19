#ifndef TIMER_H
#define TIMER_H

#include <chrono>
#include <string>

struct Timer
{
    //std::chrono::time_point<std::chrono::steady_clock> start;
    //std::chrono::time_point<std::chrono::steady_clock> end;
    std::chrono::high_resolution_clock::time_point end;
    std::chrono::high_resolution_clock::time_point start;
    std::chrono::duration<float> duration;
    std::string timer_name;

    Timer()
    {
        start = std::chrono::high_resolution_clock::now();
    }

    Timer(std::string name)
    {
        timer_name = name;
        start = std::chrono::high_resolution_clock::now();
    }

    ~Timer()
    {
        end = std::chrono::high_resolution_clock::now();
        duration = end - start;
        float ms = duration.count() * 1000.0f;
        std::cout << "Timer \"" + timer_name + "\" took: " << ms << "ms" << std::endl;
    }
};

#endif // TIMER_H
