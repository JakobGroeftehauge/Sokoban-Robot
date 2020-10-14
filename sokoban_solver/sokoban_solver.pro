TEMPLATE = app
CONFIG += console c++11
CONFIG -= app_bundle
CONFIG -= qt

SOURCES += \
        coordinate.cpp \
        main.cpp \
        node.cpp \
        sokoban_map.cpp \
        sokoban_state.cpp

HEADERS += \
    Timer.h \
    coordinate.h \
    node.h \
    sokoban_map.h \
    sokoban_state.h
