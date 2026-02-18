def onauton_autonomous_0():
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, reconcile_velocity, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    # Auto
    init_setup()
    turn_mod = 1
    Intake.set_max_torque(100, PERCENT)
    Intake.set_velocity(100, PERCENT)
    while not (not Auto_color == "bl" and not auto_side == "bl"):
        print(console_format(Auto_color))
        print("VEXcode", end="")
        print(console_format(auto_side))
        wait(5, MSEC)
    inertial_for_auton.set_heading(0, DEGREES)
    inertial_for_auton.set_rotation(0, DEGREES)
    if auto_side == "r":
        pass
    elif auto_side == "l":
        Set_Drivetrain_Velocity_to__25(60)
        drive_forwards_dist_milimeters(905)
        wait(0.3, SECONDS)
        PID_turn_for_head_degrees(-90)
        Front_Down = 1
        Intake.spin(FORWARD)
        Set_Drivetrain_Velocity_to__25(30)
        drive_forwards_dist_milimeters(297)
        wait(0.5, SECONDS)
        Set_Drivetrain_Velocity_to__25(20)
        drive_forwards_dist_milimeters(15)
        wait(0.3, SECONDS)
        drive_forwards_dist_milimeters(10)
        wait(0.5, SECONDS)
        Set_Drivetrain_Velocity_to__25(50)
        drive_forwards_dist_milimeters(-300)
        Front_Down = 0
        Turn_To_Heading_heading_input_from_0_359_9(270)
        drive_forwards_dist_milimeters(-370)
        Intake.spin(FORWARD)
        TopMotor.spin(REVERSE)
        wait(3, SECONDS)
        drive_forwards_dist_milimeters(300)
        Turn_To_Heading_heading_input_from_0_359_9(180)
        drive_forwards_dist_milimeters(300)
    elif auto_side == "n":
        PID_turn_for_head_degrees(180)
    else:
        if IntakeData == 0:
            pass
        else:
            Read_Auto_String__auto_code("60:837.5999!40:1772.4!50:-2119.2!48.88086:-2193.6!47.23186:-980.4!0.9401041:-73.2!1:129.6!0:0!/57.40688:800.4!38.91221:1723.2!47.39997:-2010.0!50:-2242.8!50:-1036.8!1:-76.8!0.9984568:128.4!0:0!/0!1!0!0!0!1!1!0!/0!0!0!0!0!0!0!0!/0!{26.70579}1!0!{-109.1027}0!{-97.49892}0!1!1!0!#")
