from time import sleep

THRESHOLD_LINE = 50
DRIVE_SPEED = 90
STOP_SPEED = 0
TURN_SPEED = 900
TURN_ANGLE = 153
BRAKE_DISTANCE = 40
BRAKE_SPEED = 900

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

def turn_left(mL, mR):
    # Distance from brake to line
    mL.run_to_rel_pos(position_sp = BRAKE_DISTANCE, speed_sp = BRAKE_SPEED, stop_action = "hold")
    mR.run_to_rel_pos(position_sp = BRAKE_DISTANCE, speed_sp = BRAKE_SPEED, stop_action = "hold")
    mR.wait_until('holding')
    mL.wait_until('holding')
    # Rotate 90 degrees
    mL.run_to_rel_pos(position_sp = -TURN_ANGLE, speed_sp = TURN_SPEED, stop_action = "hold")
    mR.run_to_rel_pos(position_sp = TURN_ANGLE, speed_sp = TURN_SPEED, stop_action = "hold")
    mR.wait_until('holding')
    mL.wait_until('holding')

def turn_right(mL, mR):
    ## Distance from brake to line
    mL.run_to_rel_pos(position_sp = BRAKE_DISTANCE, speed_sp = BRAKE_SPEED, stop_action = "hold")
    mR.run_to_rel_pos(position_sp = BRAKE_DISTANCE, speed_sp = BRAKE_SPEED, stop_action = "hold")
    mR.wait_until('holding')
    mL.wait_until('holding')
    # Rotate 90 degrees
    mR.run_to_rel_pos(position_sp = -TURN_ANGLE, speed_sp = TURN_SPEED, stop_action = "hold")
    mL.run_to_rel_pos(position_sp = TURN_ANGLE, speed_sp = TURN_SPEED, stop_action = "hold")
    mR.wait_until('holding')
    mL.wait_until('holding')

def move_forward(mL, mR, colorSensorLeft, colorSensorRight):
    mR.duty_cycle_sp = DRIVE_SPEED
    mL.duty_cycle_sp = DRIVE_SPEED

    mR.run_direct()
    mL.run_direct()

    sensorLeft = 0
    sensorRight = 0

    while(sensorLeft == 0 and sensorRight == 0):
        if(bin_val(colorSensorLeft.value(), THRESHOLD_LINE)):
            sensorLeft = 1

        if(bin_val(colorSensorRight.value(), THRESHOLD_LINE)):
            sensorRight = 1

    orientation = sign(sensorLeft - sensorRight)
    temp_motor_tick = mR.position;

    while(sensorLeft == 0 or sensorRight == 0):
        if(bin_val(colorSensorLeft.value(), THRESHOLD_LINE)):
            sensorLeft = 1

        if(bin_val(colorSensorRight.value(), THRESHOLD_LINE)):
            sensorRight = 1

    orientation_init = orientation * (mR.position - temp_motor_tick)

    print(orientation_init)

    # Correct orientiation
    if(orientation_init > 0):
        # Correct
        mL.duty_cycle_sp = STOP_SPEED
        travel_count_init = mR.position
        while(mR.position <= travel_count_init + orientation_init):
            pass # Wait for correction
        #mL.duty_cycle_sp = DRIVE_SPEED
    elif(orientation_init < 0):
        # Correct
        mR.duty_cycle_sp = STOP_SPEED
        travel_count_init = mL.position
        while(mL.position <= travel_count_init - orientation_init):
            pass # Wait for correction
        #mR.duty_cycle_sp = DRIVE_SPEED
