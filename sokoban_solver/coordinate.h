#ifndef COORDINATE_H
#define COORDINATE_H


class coordinate
{
public:
    coordinate();
    coordinate(int x, int y);
    coordinate operator + (coordinate const &obj);
    void operator * (int number);
    bool operator == (coordinate const &obj);
    int x;
    int y;
};

#endif // COORDINATE_H
