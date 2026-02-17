def stop_l_r_drive_l_r(stop_l_r_drive_l_r__l_r):
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    if stop_l_r_drive_l_r__l_r == "l":
        left1.stop()
        left3.stop()
        left2.stop()
    else:
        if stop_l_r_drive_l_r__l_r == "r":
            Right1.stop()
            Right2.stop()
            Right3.stop()
        else:
            pass

def Drive_reverse_dist_milinmeters(Drive_reverse_dist_milinmeters__dist):
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    driveMod = (Drive_reverse_dist_milinmeters__dist / ((69.85 * 3.14) / 360)) / 0.76
    Raw__Drive_f_r_f_r_for_d_degrees("r", driveMod)
    wait(0.1, SECONDS)

def turn_r_l_r_l_for_seconds_seconds_at_speed(turn_r_l_r_l_for_seconds_seconds_at_speed__r_l, turn_r_l_r_l_for_seconds_seconds_at_speed__seconds, turn_r_l_r_l_for_seconds_seconds_at_speed__speed):
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    if turn_r_l_r_l_for_seconds_seconds_at_speed__r_l == "r":
        drive_forward_true_right__R_L_at_velocity_v(False, turn_r_l_r_l_for_seconds_seconds_at_speed__speed)
        drive_reverse_true_right__R_l_at_velocity_v(True, turn_r_l_r_l_for_seconds_seconds_at_speed__speed)
    else:
        drive_forward_true_right__R_L_at_velocity_v(True, turn_r_l_r_l_for_seconds_seconds_at_speed__speed)
        drive_reverse_true_right__R_l_at_velocity_v(False, turn_r_l_r_l_for_seconds_seconds_at_speed__speed)
    wait(turn_r_l_r_l_for_seconds_seconds_at_speed__seconds, SECONDS)
    stop_l_r_drive_l_r("r")
    stop_l_r_drive_l_r("l")

def Turn_To_Heading_heading_input_from_0_359_9(Turn_To_Heading_heading_input_from_0_359_9__heading):
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    turn_to_h_dif = Turn_To_Heading_heading_input_from_0_359_9__heading - inertial_for_auton.heading(DEGREES)
    if turn_to_h_dif > 180:
        Turn_target_Degrees_With_Inertial_Helping(0 - (360 - turn_to_h_dif))
    else:
        Turn_target_Degrees_With_Inertial_Helping(turn_to_h_dif)

def drive_forwards_dist_milimeters(drive_forwards_dist_milimeters__dist):
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    driveMod = (drive_forwards_dist_milimeters__dist / ((69.85 * 3.14) / 360)) / 0.76
    Raw__Drive_f_r_f_r_for_d_degrees("f", driveMod)
    wait(0.1, SECONDS)

def Turn_target_Degrees_With_Inertial_Helping(Turn_target_Degrees_With_Inertial_Helping__target):
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    inertial_for_auton.set_rotation(0, DEGREES)
    raw__turn_d_degrees(Turn_target_Degrees_With_Inertial_Helping__target)
    for repeat_count in range(3):
        raw__turn_d_degrees((Turn_target_Degrees_With_Inertial_Helping__target - inertial_for_auton.rotation(DEGREES)) * 0.5)
        wait(5, MSEC)
    wait(0.1, SECONDS)

def drive_for_seconds_seconds_at_velocity_f_b_f_b(drive_for_seconds_seconds_at_velocity_f_b_f_b__seconds, drive_for_seconds_seconds_at_velocity_f_b_f_b__velocity, drive_for_seconds_seconds_at_velocity_f_b_f_b__f_b):
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    if drive_for_seconds_seconds_at_velocity_f_b_f_b__f_b == "f":
        drive_forward_true_right__R_L_at_velocity_v(True, drive_for_seconds_seconds_at_velocity_f_b_f_b__velocity)
        drive_forward_true_right__R_L_at_velocity_v(False, drive_for_seconds_seconds_at_velocity_f_b_f_b__velocity)
    else:
        if drive_for_seconds_seconds_at_velocity_f_b_f_b__f_b == "b":
            drive_reverse_true_right__R_l_at_velocity_v(True, drive_for_seconds_seconds_at_velocity_f_b_f_b__velocity)
            drive_reverse_true_right__R_l_at_velocity_v(False, drive_for_seconds_seconds_at_velocity_f_b_f_b__velocity)
        else:
            pass
    wait(drive_for_seconds_seconds_at_velocity_f_b_f_b__seconds, SECONDS)
    stop_l_r_drive_l_r("l")
    stop_l_r_drive_l_r("r")

def raw__turn_d_degrees(raw__turn_d_degrees__d):
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    turn_mod = ((((355.6 * 3.14) / 360) * raw__turn_d_degrees__d) / 0.76) * 2
    Right1.spin_for(REVERSE, turn_mod, DEGREES, wait=False)
    Right2.spin_for(REVERSE, turn_mod, DEGREES, wait=False)
    Right3.spin_for(REVERSE, turn_mod, DEGREES, wait=False)
    left1.spin_for(FORWARD, turn_mod, DEGREES, wait=False)
    left2.spin_for(FORWARD, turn_mod, DEGREES, wait=False)
    left3.spin_for(FORWARD, turn_mod, DEGREES)
