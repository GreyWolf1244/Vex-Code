def Record_Auto():
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, reconcile_velocity, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    controller_1.rumble("....")
    leftData = 0
    RightData = 0
    MatchLoadData = 0
    TopMotorDATA = 0
    IntakeDriveData = ""
    MatchLoadDriveDATA = ""
    TopMotorDriveDATA = ""
    LeftDriveData = ""
    RightDriveData = ""
    AuBP_MaxVP = 60
    controller_1.screen.print("press A")
    while not controller_1.buttonA.pressing():
        wait(5, MSEC)
    while not not controller_1.buttonA.pressing():
        wait(5, MSEC)
    controller_1.screen.clear_row(3)
    controller_1.screen.set_cursor(controller_1.screen.row(), 1)
    while True:
        textReadout = "///Paused\\\\\\"
        while not controller_1.buttonA.pressing():
            wait(5, MSEC)
        while not not controller_1.buttonA.pressing():
            wait(5, MSEC)
        while not controller_1.buttonA.pressing():
            textReadout = str(str("Max Velocity: ") + str(str(AuBP_MaxVP))) + str(str(" & ") + str(str("Speed: ") + str(str(str(((68.95 * 3.14) * (450 * (AuBP_MaxVP / 100))) / 60)) + str(" MM/S"))))
            if controller_1.buttonUp.pressing():
                AuBP_MaxVP = AuBP_MaxVP + 5
                if AuBP_MaxVP > 100:
                    AuBP_MaxVP = 100
                if AuBP_MaxVP < 10:
                    AuBP_MaxVP = 5
                while not not controller_1.buttonUp.pressing():
                    wait(5, MSEC)
            if controller_1.buttonRight.pressing():
                AuBP_MaxVP = AuBP_MaxVP + -5
                if AuBP_MaxVP < 1:
                    AuBP_MaxVP = 1
                while not not controller_1.buttonRight.pressing():
                    wait(5, MSEC)
            wait(5, MSEC)
        if controller_1.buttonLeft.pressing():
            break
        while not not controller_1.buttonA.pressing():
            wait(5, MSEC)
        textReadout = "Recording..."
        IntakeData = 0
        MatchLoadData = 0
        TopMotorDATA = 0
        Right1.set_position(0, DEGREES)
        left1.set_position(0, DEGREES)
        inertial_for_auton.set_rotation(0, DEGREES)
        print("\033[31m")
        print("RECORDING...")
        TopMotor.set_position(0, DEGREES)
        Intake.set_position(0, DEGREES)
        while not controller_1.buttonA.pressing():
            wait(5, MSEC)
        if math.fabs(Intake.position(DEGREES)) > 0:
            IntakeData = 1
        MatchLoadData = Front_Down
        if math.fabs(TopMotor.position(DEGREES)) > 0:
            TopMotorDATA = 1
        print("intake data")
        print(console_format(IntakeData))
        print(console_format(left1.position(DEGREES)))
        print(console_format(Right1.position(DEGREES)))
        if left1.position(DEGREES) > 0 and Right1.position(DEGREES) < 0 or left1.position(DEGREES) < 0 and Right1.position(DEGREES) > 0:
            IntakeDriveData = str(IntakeDriveData) + str(str("{") + str(str(inertial_for_auton.rotation(DEGREES)) + str("}")))
        else:
            if IntakeData == 1:
                IntakeDriveData = str(IntakeDriveData) + str("1!")
            else:
                IntakeDriveData = str(IntakeDriveData) + str("0!")
            if MatchLoadData == 1:
                MatchLoadDriveDATA = str(MatchLoadDriveDATA) + str("1!")
            else:
                MatchLoadDriveDATA = str(MatchLoadDriveDATA) + str("0!")
            if TopMotorDATA == 1:
                TopMotorDriveDATA = str(TopMotorDriveDATA) + str("1!")
            else:
                TopMotorDriveDATA = str(TopMotorDriveDATA) + str("0!")
            textReadout = "drive compensate"
            if math.fabs(left1.position(DEGREES)) < 1 and math.fabs(Right1.position(DEGREES)) < 1:
                leftData = 1
                RightData = 1
            else:
                if math.fabs(left1.position(DEGREES)) > math.fabs(Right1.position(DEGREES)):
                    leftData = AuBP_MaxVP
                    RightData = AuBP_MaxVP / (left1.position(DEGREES) / (Right1.position(DEGREES) + 1))
                else:
                    RightData = AuBP_MaxVP
                    leftData = AuBP_MaxVP / (Right1.position(DEGREES) / (left1.position(DEGREES) + 1))
            LeftDriveData = str(str(LeftDriveData) + str(str(str(leftData)) + str(":"))) + str(str(str(left1.position(DEGREES))) + str("!"))
            RightDriveData = str(str(RightDriveData) + str(str(str(RightData)) + str(":"))) + str(str(str(Right1.position(DEGREES))) + str("!"))
        wait(5, MSEC)
    print("\033[2J")
    LeftDriveData = str(str(LeftDriveData) + str("0:0!")) + str("/")
    RightDriveData = str(str(RightDriveData) + str("0:0!")) + str("/")
    TopMotorDriveDATA = str(str(TopMotorDriveDATA) + str("0!")) + str("/")
    MatchLoadDriveDATA = str(str(MatchLoadDriveDATA) + str("0!")) + str("/")
    IntakeDriveData = str(str(IntakeDriveData) + str("0!")) + str("#")
    controller_1.rumble("-.-.")
    controller_1.screen.print("Press A to retrieve data")
    while not not controller_1.buttonA.pressing():
        wait(5, MSEC)
    while not controller_1.buttonA.pressing():
        wait(5, MSEC)
    controller_1.screen.clear_row(3)
    controller_1.screen.set_cursor(controller_1.screen.row(), 1)
    textReadout = "Check the console for data"
    print("\033[30m")
    # fix
    print(str(LeftDriveData) + str(str(RightDriveData) + str(str(TopMotorDriveDATA) + str(str(MatchLoadDriveDATA) + str(IntakeDriveData)))))
    print("Copy this value and paste it into the read auto block")

def get_next_value_for_drive():
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, reconcile_velocity, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    IntakeDriveData = ""
    LeftDriveData = ""
    RightDriveData = ""
    TopMotorDriveDATA = ""
    MatchLoadDriveDATA = ""
    LeftVP = ""
    RightVP = ""
    use_turningInertial = 0
    while not (IntakeData[Intake_Iter - 1]) == "!":
        textReadout = str("finding intake data...") + str(Intake_Iter)
        print("\033[91m")
        print(str("finding intake data...") + str(Intake_Iter))
        if (IntakeData[Intake_Iter - 1]) == "#":
            print("limit reached! Commencing breaking...")
            Intake_Iter = Intake_Iter + -1
            BreakParsing = 1
            break
        if (IntakeData[Intake_Iter - 1]) == "{":
            Intake_Iter = Intake_Iter + 1
            while not (IntakeData[Intake_Iter - 1]) == "}":
                IntakeDriveData = str(IntakeDriveData) + str(IntakeData[Intake_Iter - 1])
                Intake_Iter = Intake_Iter + 1
                wait(5, MSEC)
            Intake_Iter = Intake_Iter + 1
            use_turningInertial = 1
            break
        IntakeDriveData = str(IntakeDriveData) + str(IntakeData[Intake_Iter - 1])
        Intake_Iter = Intake_Iter + 1
        wait(5, MSEC)
    if use_turningInertial == 0:
        Intake_Iter = Intake_Iter + 1
        while not (leftData[Left_Iter - 1]) == ":":
            textReadout = str("finding left vp...") + str(Left_Iter)
            print("\033[32m")
            print(str("finding left vp...") + str(Left_Iter))
            if BreakParsing == 1:
                print("Breaking left...")
                break
            LeftVP = str(LeftVP) + str(leftData[Left_Iter - 1])
            Left_Iter = Left_Iter + 1
            wait(5, MSEC)
        Left_Iter = Left_Iter + 1
        while not (leftData[Left_Iter - 1]) == "!":
            textReadout = str("finding left dist...") + str(Left_Iter)
            print("\033[31m")
            print(str("finding left dist...") + str(Left_Iter))
            if BreakParsing == 1:
                print("Breaking left...")
                break
            LeftDriveData = str(LeftDriveData) + str(leftData[Left_Iter - 1])
            Left_Iter = Left_Iter + 1
            wait(5, MSEC)
        Left_Iter = Left_Iter + 1
        while not (RightData[Right_Iter - 1]) == ":":
            textReadout = str("finding right vp...") + str(Right_Iter)
            print("\033[34m")
            print(str("finding right vp...") + str(Right_Iter))
            if BreakParsing == 1:
                print("Breaking right...")
                break
            RightVP = str(RightVP) + str(RightData[Right_Iter - 1])
            Right_Iter = Right_Iter + 1
            wait(5, MSEC)
        Right_Iter = Right_Iter + 1
        while not (RightData[Right_Iter - 1]) == "!":
            textReadout = str("finding right dist...") + str(Right_Iter)
            print("\033[36m")
            print(str("finding right dist...") + str(Right_Iter))
            if BreakParsing == 1:
                print("Breaking right...")
                break
            RightDriveData = str(RightDriveData) + str(RightData[Right_Iter - 1])
            Right_Iter = Right_Iter + 1
            wait(5, MSEC)
        Right_Iter = Right_Iter + 1
        print(str("finding scoring data...") + str(top_iter))
        while not (TopMotorDATA[top_iter - 1]) == "!":
            textReadout = str("finding scoring data...") + str(top_iter)
            print("\033[91m")
            print(str("finding scoring data...") + str(top_iter))
            if BreakParsing == 1:
                print("Breaking scoring...")
                break
            TopMotorDriveDATA = str(TopMotorDriveDATA) + str(TopMotorDATA[top_iter - 1])
            top_iter = top_iter + 1
            wait(5, MSEC)
        top_iter = top_iter + 1
        while not (MatchLoadData[matchload_iter - 1]) == "!":
            textReadout = str("finding matchload data...") + str(matchload_iter)
            print("\033[91m")
            print(str("finding matchload data...") + str(matchload_iter))
            if BreakParsing == 1:
                print("Breaking matchload...")
                break
            MatchLoadDriveDATA = str(MatchLoadDriveDATA) + str(MatchLoadData[matchload_iter - 1])
            matchload_iter = matchload_iter + 1
            wait(5, MSEC)
        matchload_iter = matchload_iter + 1

def Read_Auto_String__auto_code(Read_Auto_String__auto_code__auto_code):
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, reconcile_velocity, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    BreakParsing = 0
    leftData = ""
    RightData = ""
    IntakeData = ""
    Right_Iter = 1
    Left_Iter = 1
    iteration = 1
    while not (Read_Auto_String__auto_code__auto_code[iteration - 1]) == "/":
        leftData = str(leftData) + str(Read_Auto_String__auto_code__auto_code[iteration - 1])
        iteration = iteration + 1
        wait(5, MSEC)
    iteration = iteration + 1
    while not (Read_Auto_String__auto_code__auto_code[iteration - 1]) == "/":
        RightData = str(RightData) + str(Read_Auto_String__auto_code__auto_code[iteration - 1])
        iteration = iteration + 1
        wait(5, MSEC)
    iteration = iteration + 1
    while not (Read_Auto_String__auto_code__auto_code[iteration - 1]) == "/":
        TopMotorDATA = str(TopMotorDATA) + str(Read_Auto_String__auto_code__auto_code[iteration - 1])
        iteration = iteration + 1
        wait(5, MSEC)
    iteration = iteration + 1
    while not (Read_Auto_String__auto_code__auto_code[iteration - 1]) == "/":
        MatchLoadData = str(MatchLoadData) + str(Read_Auto_String__auto_code__auto_code[iteration - 1])
        iteration = iteration + 1
        wait(5, MSEC)
    iteration = iteration + 1
    while not (Read_Auto_String__auto_code__auto_code[iteration - 1]) == "#":
        IntakeData = str(IntakeData) + str(Read_Auto_String__auto_code__auto_code[iteration - 1])
        iteration = iteration + 1
        wait(5, MSEC)
    IntakeData = str(IntakeData) + str(Read_Auto_String__auto_code__auto_code[iteration - 1])
    iteration = iteration + 1
    controller_1.rumble("....")
    controller_1.screen.print("Press a to view data")
    print("\033[30m")
    print(str("Left Data: ") + str(leftData))
    print(str("Right Data: ") + str(RightData))
    print(str("intake Data: ") + str(IntakeData))
    print(str("Match Load data: ") + str(MatchLoadData))
    print(str("scoring Data: ") + str(TopMotorDATA))
    if not ("!" in IntakeData):
        print("\033[31m")
        print("ERROR ON INTAKE; NO DELINEATOR:STOPPING")
        while not ("!" in IntakeData):
            wait(5, MSEC)
    controller_1.rumble("....")
    controller_1.screen.clear_row(3)
    controller_1.screen.set_cursor(controller_1.screen.row(), 1)
    controller_1.screen.print("X to confirm")
    controller_1.screen.clear_row(3)
    controller_1.screen.set_cursor(controller_1.screen.row(), 1)
    Intake_Iter = 1
    Right_Iter = 1
    Left_Iter = 1
    top_iter = 1
    matchload_iter = 1
    while True:
        get_next_value_for_drive()
        print("\033[30m")
        if use_turningInertial == 1:
            print(console_format(IntakeDriveData))
            Turn_target_Degrees_With_Inertial_Helping(float(IntakeDriveData))
            use_turningInertial = 0
        else:
            print(console_format(IntakeDriveData))
            if (float(IntakeDriveData)) == 1:
                Intake.spin(FORWARD)
            else:
                Intake.stop()
            print(console_format(TopMotorDriveDATA))
            if (float(TopMotorDriveDATA)) == 1:
                TopMotor.spin(REVERSE)
            else:
                TopMotor.stop()
            print(console_format(MatchLoadDriveDATA))
            if (float(MatchLoadDriveDATA)) == 1:
                Front_Down = 1
            else:
                Front_Down = 0
            print(console_format(LeftVP))
            set_Left_drive_velocity_to_velocity(float(LeftVP))
            print(console_format(RightVP))
            Set_Right_Drive_Velocity_To_v(float(RightVP))
            print(console_format(LeftDriveData))
            raw__spin_left_degrees_degrees_f_r_f_r(float(LeftDriveData), "f")
            print(console_format(RightDriveData))
            raw__spin_right_for_d_degrees_f_r_f_b(float(RightDriveData), "f")
        while not (not left1.is_spinning() and not Right1.is_spinning()):
            wait(5, MSEC)
        while not (inertial_for_auton.orientation(PITCH, DEGREES) > -5 and inertial_for_auton.orientation(PITCH, DEGREES) < 5 and inertial_for_auton.orientation(ROLL, DEGREES) > -5 and inertial_for_auton.orientation(ROLL, DEGREES) < 5):
            wait(5, MSEC)
        if (IntakeData[Intake_Iter - 1]) == "b" or (IntakeData[Intake_Iter - 1]) == "#":
            break
        if BreakParsing == 1:
            break
        wait(5, MSEC)
    textReadout = "done!"
    print("Done!")
    print("Done!")
