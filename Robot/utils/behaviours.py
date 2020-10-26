from ev3dev2.motor import * #OUTPUT_A, OUTPUT_B, MoveDifferential, SpeedRPM
from time import sleep
from ev3dev2.sound import Sound

spkr = Sound()

THRESHOLD_LINE = 35
DRIVE_SPEED = 40
STOP_SPEED = 0
TURN_SPEED = 50
TURN_ANGLE = 153
BRAKE_DISTANCE = 30
BRAKE_SPEED = 900
GEARING = 1.566667
STOP_LINE = 40

def bin_val(val, threshold):
    if val < threshold:
        return 1
    else:
        return 0

def sign(val):
    if val >= 0:
        return 1
    else:
        return -1

def turn_left(mDiff):
    speed = SpeedPercent(DRIVE_SPEED)
    speed = speed_to_speedvalue(speed)
    rotations = 0.7 #0.6
    mDiff.on_for_rotations(speed, speed, rotations, brake=False, block=True)

    mDiff.turn_left(SpeedRPM(TURN_SPEED), 90) #96


def turn_right(mDiff):
    speed = SpeedPercent(DRIVE_SPEED)
    speed = speed_to_speedvalue(speed)
    rotations = 0.7 #0.6
    mDiff.on_for_rotations(speed, speed, rotations, brake=False, block=True)

    mDiff.turn_right(SpeedRPM(TURN_SPEED), 90) #96


def turn_one_eighty(mDiff):
    speed = SpeedPercent(DRIVE_SPEED)
    speed = speed_to_speedvalue(speed)
    rotations = 0.7
    mDiff.on_for_rotations(speed, speed, rotations, brake=False, block=True)

    mDiff.turn_left(SpeedRPM(TURN_SPEED), 180) #183

def move_forward(mDiff, colorSensorStop, colorSensorLeft, colorSensorRight):

    off_line_count_max = 2000000000
    sleep_time = 0.001
    kp=1.2
    ki=0
    kd=0.1
    white = 80
    integral = 0.0
    last_error = 0.0
    derivative = 0.0
    off_line_count = 0
    target_light_intensity = 37
    speed = SpeedPercent(DRIVE_SPEED)
    speed = speed_to_speedvalue(speed)
    speed_native_units = speed.to_native_units(mDiff.left_motor)

    rotations = 0.1
    mDiff.on_for_rotations(speed, speed, rotations, brake=False, block=True)

    while True:
        error = colorSensorLeft.value() - colorSensorRight.value() #target_light_intensity - reflected_light_intensity
        integral = integral + error
        derivative = error - last_error
        last_error = error
        turn_native_units = (kp * error) + (ki * integral) + (kd * derivative)

        left_speed = SpeedNativeUnits(speed_native_units + turn_native_units)
        right_speed = SpeedNativeUnits(speed_native_units - turn_native_units)

#        if turn_native_units > 0:
#            left_speed = SpeedNativeUnits(speed_native_units)
#            right_speed = SpeedNativeUnits(speed_native_units - turn_native_units)
#        else:
#            left_speed = SpeedNativeUnits(speed_native_units + turn_native_units)
#            right_speed = SpeedNativeUnits(speed_native_units)

        # Have we lost the line?
#        if reflected_light_intensity >= white:
#            off_line_count += 1

#            if off_line_count >= off_line_count_max:
#                mDiff.stop()
#                raise LineFollowErrorLostLine("we lost the line")
#        else:
#            off_line_count = 0


        if colorSensorStop.reflected_light_intensity < STOP_LINE:
            break

        #time.sleep(sleep_time)

        try:
            mDiff.on(left_speed, right_speed)
        except SpeedInvalid as e:
            mDiff.stop()
            raise LineFollowErrorTooFast("The robot is moving too fast to follow the line")

    mDiff.stop()
#    spkr.beep()



def move_backward(mDiff, colorSensorStop):

    speed = SpeedPercent(-DRIVE_SPEED)
    speed = speed_to_speedvalue(speed)

    rotations = 0.7
    mDiff.on_for_rotations(speed, speed, rotations, brake=False, block=True)

    mDiff.on(speed, speed)

    while True:
        if colorSensorStop.reflected_light_intensity < STOP_LINE:
            mDiff.stop()
            break

#    speed = SpeedPercent(DRIVE_SPEED)
#    speed = speed_to_speedvalue(speed)

#    rotations = 0.3
#    mDiff.on_for_rotations(speed, speed, rotations, brake=True, block=True)




def move_forward_dual(mDiff, colorSensorStop, colorSensorLeft, colorSensorRight):
    status = True
    f = open("stopsensortest_high_can.csv", "a")

    speed = SpeedPercent(DRIVE_SPEED)
    speed = speed_to_speedvalue(speed)

    rotations = 0.2
    mDiff.on_for_rotations(speed, speed, rotations, brake=False, block=True)


    while status:
        status = colorSensorStop.reflected_light_intensity > STOP_LINE
        f.write(str(colorSensorStop.reflected_light_intensity) + ", ")
        if colorSensorLeft.value() < THRESHOLD_LINE:
            mDiff.on(DRIVE_SPEED*0.6, DRIVE_SPEED)
        elif colorSensorRight.value() < THRESHOLD_LINE:
            mDiff.on(DRIVE_SPEED, DRIVE_SPEED*0.6)
        else:
            mDiff.on(DRIVE_SPEED, DRIVE_SPEED)
    f.close()
    mDiff.stop()
#    spkr.beep()
