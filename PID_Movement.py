def PID_move_mm_mm(PID_move_mm_mm__mm):
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, reconcile_velocity, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    driveMod = (PID_move_mm_mm__mm / ((69.85 * 3.14) / 360)) / 0.76
    Right1.set_position(0, DEGREES)
    left1.set_position(0, DEGREES)
    Kp = 0.15
    Ki = 0.02
    Kd = 0.15
    error = 0
    last_error = 0
    integral = 0
    loop_delay = 0.015
    error_threshhold = 5
    integral_limit = 300
    while True:
        # AVG motor positions
        position = (Right1.position(DEGREES) + left1.position(DEGREES)) / 2
        # PID math
        error = driveMod - position
        integral = integral + error
        # Anti-windup
        if math.fabs(error) > integral_limit:
            integral = 0
        derivative = error - last_error
        last_error = error
        POWER = Kp * error + (Ki * integral + Kd * derivative)
        # Driving
        Set_Drivetrain_Velocity_to__25(POWER)
        Right1.spin(FORWARD)
        Right2.spin(FORWARD)
        Right3.spin(FORWARD)
        left1.spin(FORWARD)
        left2.spin(FORWARD)
        left3.spin(FORWARD)
        if math.fabs(error) < error_threshhold:
            break
        wait(loop_delay, SECONDS)
        wait(5, MSEC)
    stop_l_r_drive_l_r("l")
    stop_l_r_drive_l_r("r")
    wait(0.3, SECONDS)

def PID_turn_for_head_degrees(PID_turn_for_head_degrees__head):
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, reconcile_velocity, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    reconcile_velocity = Right1.velocity(PERCENT)
    Kp = 0.6
    Ki = 0.001
    Kd = 0.05
    integral_limit = 200
    error_threshhold = 1
    loop_delay = 0.015
    inertial_for_auton.set_rotation(0, DEGREES)
    error = 0
    last_error = 0
    integral = 0
    while True:
        # PID math
        error = PID_turn_for_head_degrees__head - inertial_for_auton.rotation(DEGREES)
        integral = integral + error
        # Anti-windup
        if math.fabs(error) > integral_limit:
            integral = 0
        derivative = error - last_error
        last_error = error
        POWER = Kp * error + (Ki * integral + Kd * derivative)
        # Driving
        Set_Drivetrain_Velocity_to__25(POWER)
        Right1.spin(REVERSE)
        Right2.spin(REVERSE)
        Right3.spin(REVERSE)
        left1.spin(FORWARD)
        left2.spin(FORWARD)
        left3.spin(FORWARD)
        if math.fabs(error) < error_threshhold:
            break
        wait(loop_delay, SECONDS)
        wait(5, MSEC)
    stop_l_r_drive_l_r("l")
    stop_l_r_drive_l_r("r")
    Set_Drivetrain_Velocity_to__25(reconcile_velocity)

def PID_turn_to_heading_heading(PID_turn_to_heading_heading__heading):
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, reconcile_velocity, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    turn_to_h_dif = PID_turn_to_heading_heading__heading - inertial_for_auton.heading(DEGREES)
    if turn_to_h_dif > 180:
        PID_turn_for_head_degrees(0 - (360 - turn_to_h_dif))
    else:
        PID_turn_for_head_degrees(turn_to_h_dif)
