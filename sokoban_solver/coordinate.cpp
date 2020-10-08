#include "coordinate.h"

coordinate::coordinate()
{

}

coordinate::coordinate(int x, int y)
{
    this->x = x;
    this->y = y;
}

coordinate coordinate::operator +(const coordinate &obj)
{
    int x_sum = this->x + obj.x;
    int y_sum = this->y + obj.y;
    return coordinate(x_sum, y_sum);
}

void coordinate::operator * (int number)
{
    this->x = this->x * number;
    this->y = this->y * number;
}

bool coordinate::operator ==(const coordinate &obj)
{
    if(this->x == obj.x)
    {
        if(this->y == obj.y)
        {
            return true;
        }
    }
    return false;
}
