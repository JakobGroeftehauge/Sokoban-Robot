from ev3dev2.motor import OUTPUT_A, OUTPUT_B, MoveDifferential, SpeedRPM
from ev3dev2.wheel import EV3Tire

STUD_MM = 8

# test with a robot that:
# - uses the standard wheels known as EV3Tire
# - wheels are 16 studs apart
mdiff = MoveDifferential(OUTPUT_A, OUTPUT_B, EV3Tire, 17 * STUD_MM)

# Rotate 90 degrees clockwise
mdiff.turn_right(SpeedRPM(40), 90 / 1.666667)
