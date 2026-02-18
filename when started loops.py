#handles starting to record an auto
def when_started1():
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, reconcile_velocity, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    # DO NOT INTERMIX PID TURN & [TURN FOR__] OR [TURN TO HEADING__]
    controller_1.rumble("----")
    controller_1.screen.print("Don't forget to setup!")
    while not (not Auto_color == "bl" and not auto_side == "bl"):
        wait(5, MSEC)
    controller_1.screen.clear_row(3)
    controller_1.screen.set_cursor(controller_1.screen.row(), 1)
    if auto_side == "m":
        if IntakeData == 0:
            recording = 1
            Record_Auto()
        else:
            pass
    else:
        pass
#handles readout and initial inertial calibration
def when_started2():
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, reconcile_velocity, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    # readout
    recording = 0
    skillsRun = 0
    Auto_color = "bl"
    auto_side = "bl"
    brain.screen.set_pen_color(Color.RED)
    brain.screen.print("CALIBRATING... ")
    brain.screen.next_row()
    brain.screen.print("DO NOT PLUG IN TO FIELD CONTROL")
    inertial_for_auton.calibrate()
    while inertial_for_auton.is_calibrating():
        sleep(50)
    inertial_for_auton.set_heading(0, DEGREES)
    inertial_for_auton.set_rotation(0, DEGREES)
    brain.screen.clear_screen()
    brain.screen.set_pen_color(Color.GREEN)
    brain.screen.set_cursor(1, 1)
    brain.screen.print("DONE")
    wait(0.3, SECONDS)
    brain.screen.clear_screen()
    while True:
        if Auto_color == "r":
            brain.screen.set_fill_color(Color.RED)
        else:
            brain.screen.set_fill_color(Color.WHITE)
        brain.screen.draw_rectangle(50, 25, 100, 50)
        brain.screen.set_pen_color(Color.BLACK)
        brain.screen.set_cursor(3, 9)
        brain.screen.print("RED")
        if Auto_color == "b":
            brain.screen.set_fill_color(Color.BLUE)
        else:
            brain.screen.set_fill_color(Color.WHITE)
        brain.screen.draw_rectangle(150, 25, 100, 50)
        brain.screen.set_pen_color(Color.BLACK)
        brain.screen.set_cursor(3, 20)
        brain.screen.print("BLUE")
        if Auto_color == "n":
            brain.screen.set_fill_color(Color.ORANGE)
        else:
            brain.screen.set_fill_color(Color.WHITE)
        brain.screen.draw_rectangle(250, 25, 100, 50)
        brain.screen.set_pen_color(Color.BLACK)
        brain.screen.set_cursor(3, 25)
        brain.screen.print("No C-Sort")
        if skillsRun == 1:
            brain.screen.set_fill_color(Color.YELLOW)
        else:
            brain.screen.set_fill_color(Color.WHITE)
        brain.screen.draw_rectangle(350, 25, 100, 50)
        brain.screen.set_pen_color(Color.BLACK)
        brain.screen.set_cursor(3, 37)
        brain.screen.print("Skills?")
        if brain.screen.pressing():
            if brain.screen.y_position() > 25 and brain.screen.y_position() < 70:
                if brain.screen.x_position() > 50 and brain.screen.x_position() < 150:
                    Auto_color = "r"
                if brain.screen.x_position() > 155 and brain.screen.x_position() < 250:
                    Auto_color = "b"
                if brain.screen.x_position() > 255 and brain.screen.x_position() < 350:
                    Auto_color = "n"
                if brain.screen.x_position() > 355 and brain.screen.x_position() < 455:
                    if skillsRun == 1:
                        skillsRun = 0
                    else:
                        skillsRun = 1
                    while not not brain.screen.pressing():
                        wait(5, MSEC)
            if brain.screen.y_position() > 95 and brain.screen.y_position() < 140:
                if brain.screen.x_position() > 50 and brain.screen.x_position() < 150:
                    auto_side = "r"
                if brain.screen.x_position() > 155 and brain.screen.x_position() < 250:
                    auto_side = "l"
                if brain.screen.x_position() > 255 and brain.screen.x_position() < 350:
                    auto_side = "n"
                if brain.screen.x_position() > 355 and brain.screen.x_position() < 450:
                    auto_side = "m"
                    IntakeData = 0
        if brain.screen.y_position() > 135 and brain.screen.y_position() < 210:
            if brain.screen.x_position() > 355 and brain.screen.x_position() < 450:
                auto_side = "m"
                IntakeData = 1
        print(console_format(brain.screen.x_position()), end="")
        print(" , ", end="")
        print(console_format(brain.screen.y_position()))
        print("///", end="")
        print(console_format(IntakeData), end="")
        print("///", end="")
        if auto_side == "r":
            brain.screen.set_fill_color(Color.GREEN)
        else:
            brain.screen.set_fill_color(Color.WHITE)
        brain.screen.draw_rectangle(50, 100, 100, 50)
        brain.screen.set_pen_color(Color.BLACK)
        brain.screen.set_cursor(7, 9)
        brain.screen.print("RIGHT")
        if auto_side == "l":
            brain.screen.set_fill_color(Color.GREEN)
        else:
            brain.screen.set_fill_color(Color.WHITE)
        brain.screen.draw_rectangle(150, 100, 100, 50)
        brain.screen.set_pen_color(Color.BLACK)
        brain.screen.set_cursor(7, 20)
        brain.screen.print("LEFT")
        if auto_side == "n":
            brain.screen.set_fill_color(Color.CYAN)
        else:
            brain.screen.set_fill_color(Color.WHITE)
        brain.screen.draw_rectangle(250, 100, 100, 50)
        brain.screen.set_pen_color(Color.BLACK)
        brain.screen.set_cursor(7, 28)
        brain.screen.print("NoSolo")
        if auto_side == "m" and IntakeData == 0:
            brain.screen.set_fill_color(Color.RED)
        else:
            brain.screen.set_fill_color(Color.WHITE)
        brain.screen.draw_rectangle(350, 100, 100, 50)
        brain.screen.set_pen_color(Color.BLACK)
        brain.screen.set_cursor(6, 36)
        brain.screen.print("AuBP")
        brain.screen.set_cursor(7, 36)
        brain.screen.print("RECORD")
        if auto_side == "m" and IntakeData == 1:
            brain.screen.set_fill_color(Color.PURPLE)
        else:
            brain.screen.set_fill_color(Color.WHITE)
        brain.screen.draw_rectangle(350, 150, 100, 50)
        brain.screen.set_pen_color(Color.BLACK)
        brain.screen.set_cursor(9, 36)
        brain.screen.print("AuBP")
        brain.screen.set_cursor(10, 36)
        brain.screen.print("RUN")
        if not Auto_color == "bl" and not auto_side == "bl":
            break
        wait(5, MSEC)
    brain.screen.clear_screen()
    if Auto_color == "r":
        brain.screen.set_fill_color(Color.RED)
    else:
        brain.screen.set_fill_color(Color.WHITE)
    brain.screen.draw_rectangle(50, 25, 100, 50)
    brain.screen.set_pen_color(Color.BLACK)
    brain.screen.set_cursor(3, 9)
    brain.screen.print("RED")
    if Auto_color == "b":
        brain.screen.set_fill_color(Color.BLUE)
    else:
        brain.screen.set_fill_color(Color.WHITE)
    brain.screen.draw_rectangle(150, 25, 100, 50)
    brain.screen.set_pen_color(Color.BLACK)
    brain.screen.set_cursor(3, 20)
    brain.screen.print("BLUE")
    if Auto_color == "n":
        brain.screen.set_fill_color(Color.ORANGE)
    else:
        brain.screen.set_fill_color(Color.WHITE)
    brain.screen.draw_rectangle(250, 25, 100, 50)
    brain.screen.set_pen_color(Color.BLACK)
    brain.screen.set_cursor(3, 25)
    brain.screen.print("No C-Sort")
    if auto_side == "r":
        brain.screen.set_fill_color(Color.GREEN)
    else:
        brain.screen.set_fill_color(Color.WHITE)
    brain.screen.draw_rectangle(50, 100, 100, 50)
    brain.screen.set_pen_color(Color.BLACK)
    brain.screen.set_cursor(7, 9)
    brain.screen.print("RIGHT")
    if auto_side == "l":
        brain.screen.set_fill_color(Color.GREEN)
    else:
        brain.screen.set_fill_color(Color.WHITE)
    brain.screen.draw_rectangle(150, 100, 100, 50)
    brain.screen.set_pen_color(Color.BLACK)
    brain.screen.set_cursor(7, 20)
    brain.screen.print("LEFT")
    if auto_side == "n":
        brain.screen.set_fill_color(Color.CYAN)
    else:
        brain.screen.set_fill_color(Color.WHITE)
    brain.screen.draw_rectangle(250, 100, 100, 50)
    brain.screen.set_pen_color(Color.BLACK)
    brain.screen.set_cursor(7, 26)
    brain.screen.print("NoSolo")
    if auto_side == "m":
        brain.screen.set_fill_color(Color.PURPLE)
    else:
        brain.screen.set_fill_color(Color.WHITE)
    brain.screen.draw_rectangle(350, 100, 100, 50)
    brain.screen.set_pen_color(Color.BLACK)
    brain.screen.set_cursor(6, 36)
    brain.screen.print("AuBP")
    brain.screen.set_cursor(7, 36)
    if IntakeData == 0:
        brain.screen.print("RECORD")
    else:
        brain.screen.print("RUN")
    wait(1.2, SECONDS)
    print("\033[2J")
    brain.screen.clear_screen()
    brain.screen.set_fill_color(Color.TRANSPARENT)
    brain.screen.set_font(FontType.MONO15)
    brain.screen.set_pen_color(Color.GREEN)
    screen_precision = 2
    while True:
        brain.screen.clear_screen()
        brain.screen.set_cursor(1, 1)
        brain.screen.print("Program: ")
        brain.screen.next_row()
        brain.screen.set_cursor(1, 28)
        brain.screen.set_pen_color(Color.YELLOW)
        if brain.battery.capacity() < 40:
            brain.screen.set_fill_color(Color.RED)
        brain.screen.print(str("Battery status: Level: ") + str(str(str(brain.battery.capacity())) + str(" percent")))
        brain.screen.next_row()
        brain.screen.set_pen_color(Color.GREEN)
        brain.screen.set_fill_color(Color.TRANSPARENT)
        if auto_side == "l":
            brain.screen.print("Left ")
        elif auto_side == "r":
            brain.screen.print("Right ")
        elif auto_side == "m":
            brain.screen.set_pen_color(Color.RED)
            brain.screen.print("AuBP ")
        else:
            brain.screen.set_pen_color(Color.CYAN)
            brain.screen.print("One Inch ")
        brain.screen.set_cursor(2, 28)
        brain.screen.set_pen_color(Color.YELLOW)
        brain.screen.print(str("current: ") + str(str(str(brain.battery.current(CurrentUnits.AMP))) + str(str(" amps & voltage: ") + str(str(brain.battery.voltage(VoltageUnits.VOLT)) + str(" volts")))))
        brain.screen.next_row()
        if Auto_color == "r":
            brain.screen.set_pen_color(Color.RED)
            brain.screen.print("Red ")
            brain.screen.next_row()
        elif Auto_color == "b":
            brain.screen.set_pen_color(Color.BLUE)
            brain.screen.print("Blue ")
            brain.screen.next_row()
        else:
            brain.screen.set_pen_color(Color.ORANGE)
            brain.screen.print("No Color Sorting")
            brain.screen.next_row()
        brain.screen.next_row()
        brain.screen.set_pen_color(Color.GREEN)
        brain.screen.print("port    Name    temp power torque effeciency")
        brain.screen.next_row()
        if Right1.temperature(PERCENT) > 2:
            if Right1.temperature(PERCENT) > 70:
                brain.screen.set_fill_color(Color.RED)
            brain.screen.print(str("P11     Right1: ") + str(str(Right1.temperature(PERCENT))))
            brain.screen.print(" ")
            brain.screen.print(Right1.power(PowerUnits.WATT), precision=screen_precision)
            brain.screen.print(" ")
            brain.screen.print(Right1.torque(TorqueUnits.NM), precision=screen_precision)
            brain.screen.print(" ")
            brain.screen.print(Right1.efficiency(PERCENT), precision=screen_precision)
            brain.screen.next_row()
            brain.screen.set_fill_color(Color.TRANSPARENT)
        if Right2.temperature(PERCENT) > 2:
            if Right2.temperature(PERCENT) > 70:
                brain.screen.set_fill_color(Color.RED)
            brain.screen.print(str("P13     Right2: ") + str(str(Right2.temperature(PERCENT))))
            brain.screen.print(" ")
            brain.screen.print(Right2.power(PowerUnits.WATT), precision=screen_precision)
            brain.screen.print(" ")
            brain.screen.print(Right2.torque(TorqueUnits.NM), precision=screen_precision)
            brain.screen.print(" ")
            brain.screen.print(Right2.efficiency(PERCENT), precision=screen_precision)
            brain.screen.next_row()
            brain.screen.set_fill_color(Color.TRANSPARENT)
        if Right3.temperature(PERCENT) > 2:
            if Right3.temperature(PERCENT) > 70:
                brain.screen.set_fill_color(Color.RED)
            brain.screen.print(str("P12     Right3: ") + str(str(Right3.temperature(PERCENT))))
            brain.screen.print(" ")
            brain.screen.print(Right3.power(PowerUnits.WATT), precision=screen_precision)
            brain.screen.print(" ")
            brain.screen.print(Right3.torque(TorqueUnits.NM), precision=screen_precision)
            brain.screen.print(" ")
            brain.screen.print(Right3.efficiency(PERCENT), precision=screen_precision)
            brain.screen.next_row()
            brain.screen.set_fill_color(Color.TRANSPARENT)
        if left1.temperature(PERCENT) > 2:
            if left1.temperature(PERCENT) > 70:
                brain.screen.set_fill_color(Color.RED)
            brain.screen.print(str("P20      Left1: ") + str(str(left1.temperature(PERCENT))))
            brain.screen.print(" ")
            brain.screen.print(left1.power(PowerUnits.WATT), precision=screen_precision)
            brain.screen.print(" ")
            brain.screen.print(left1.torque(TorqueUnits.NM), precision=screen_precision)
            brain.screen.print(" ")
            brain.screen.print(left1.efficiency(PERCENT), precision=screen_precision)
            brain.screen.next_row()
            brain.screen.set_fill_color(Color.TRANSPARENT)
        if left2.temperature(PERCENT) > 2:
            if left2.temperature(PERCENT) > 70:
                brain.screen.set_fill_color(Color.RED)
            brain.screen.print(str("P19      Left2: ") + str(str(left2.temperature(PERCENT))))
            brain.screen.print(" ")
            brain.screen.print(left2.power(PowerUnits.WATT), precision=screen_precision)
            brain.screen.print(" ")
            brain.screen.print(left2.torque(TorqueUnits.NM), precision=screen_precision)
            brain.screen.print(" ")
            brain.screen.print(left2.efficiency(PERCENT), precision=screen_precision)
            brain.screen.next_row()
            brain.screen.set_fill_color(Color.TRANSPARENT)
        if left3.temperature(PERCENT) > 2:
            if left3.temperature(PERCENT) > 70:
                brain.screen.set_fill_color(Color.RED)
            brain.screen.print(str("P18      Left3: ") + str(str(left3.temperature(PERCENT))))
            brain.screen.print(" ")
            brain.screen.print(left3.power(PowerUnits.WATT), precision=screen_precision)
            brain.screen.print(" ")
            brain.screen.print(left3.torque(TorqueUnits.NM), precision=screen_precision)
            brain.screen.print(" ")
            brain.screen.print(left3.efficiency(PERCENT), precision=screen_precision)
            brain.screen.next_row()
            brain.screen.set_fill_color(Color.TRANSPARENT)
        if colorsorting.temperature(PERCENT) > 0:
            if colorsorting.temperature(PERCENT) > 70:
                brain.screen.set_fill_color(Color.RED)
            brain.screen.print(str("P15 colorsorting:") + str(str(colorsorting.temperature(PERCENT))))
            brain.screen.print(" ")
            brain.screen.print(colorsorting.power(PowerUnits.WATT), precision=screen_precision)
            brain.screen.print(" ")
            brain.screen.print(colorsorting.torque(TorqueUnits.NM), precision=screen_precision)
            brain.screen.print(" ")
            brain.screen.print(colorsorting.efficiency(PERCENT), precision=screen_precision)
            brain.screen.next_row()
            brain.screen.set_fill_color(Color.TRANSPARENT)
        brain.screen.print(str("P15 colorsorting:") + str(str(colorsorting.temperature(PERCENT))))
        brain.screen.print(" ")
        brain.screen.print(colorsorting.power(PowerUnits.WATT), precision=screen_precision)
        brain.screen.print(" ")
        brain.screen.print(colorsorting.torque(TorqueUnits.NM), precision=screen_precision)
        brain.screen.print(" ")
        brain.screen.print(colorsorting.efficiency(PERCENT), precision=screen_precision)
        brain.screen.next_row()
        brain.screen.set_fill_color(Color.TRANSPARENT)
        if TopMotor.temperature(PERCENT) > 2:
            if TopMotor.temperature(PERCENT) > 70:
                brain.screen.set_fill_color(Color.RED)
            brain.screen.print(str("P1    TopMotor: ") + str(str(TopMotor.temperature(PERCENT))))
            brain.screen.print(" ")
            brain.screen.print(TopMotor.power(PowerUnits.WATT), precision=screen_precision)
            brain.screen.print(" ")
            brain.screen.print(TopMotor.torque(TorqueUnits.NM), precision=screen_precision)
            brain.screen.print(" ")
            brain.screen.print(TopMotor.efficiency(PERCENT), precision=screen_precision)
            brain.screen.next_row()
            brain.screen.set_fill_color(Color.TRANSPARENT)
        if Intake.temperature(PERCENT) > 2:
            if Intake.temperature(PERCENT) > 70:
                brain.screen.set_fill_color(Color.RED)
            brain.screen.print(str("P14     Intake: ") + str(str(Intake.temperature(PERCENT))))
            brain.screen.print(" ")
            brain.screen.print(Intake.power(PowerUnits.WATT), precision=screen_precision)
            brain.screen.print(" ")
            brain.screen.print(Intake.torque(TorqueUnits.NM), precision=screen_precision)
            brain.screen.print(" ")
            brain.screen.print(Intake.efficiency(PERCENT), precision=screen_precision)
            brain.screen.next_row()
            brain.screen.set_fill_color(Color.TRANSPARENT)
        if inertial_for_auton.acceleration(XAXIS) > 0:
            brain.screen.print(str("P6 Inertial:") + str(str("Acceleration in Gs(x,y,z): ") + str(str(str(round(inertial_for_auton.acceleration(XAXIS), 1))) + str(str(" , ") + str(str(str(round(inertial_for_auton.acceleration(YAXIS), 1))) + str(str(" , ") + str(str(round(inertial_for_auton.acceleration(ZAXIS), 1)))))))))
            brain.screen.next_row()
            brain.screen.print(str("Orientation (R,P,Y): ") + str(str(str(round(inertial_for_auton.orientation(ROLL, DEGREES), 1))) + str(str(" , ") + str(str(str(round(inertial_for_auton.orientation(PITCH, DEGREES), 1))) + str(str(" , ") + str(str(round(inertial_for_auton.orientation(YAW, DEGREES), 1))))))))
            brain.screen.next_row()
            brain.screen.print(str(str("Rotation: ") + str(str(round(inertial_for_auton.rotation(DEGREES), 1)))) + str(str("Heading: ") + str(str(round(inertial_for_auton.heading(DEGREES), 1)))))
            brain.screen.next_row()
        if auto_side == "m" and auto_side == "m":
            break
        brain.screen.render()
        wait(5, MSEC)
    while True:
        brain.screen.clear_screen()
        brain.screen.set_cursor(1, 1)
        brain.screen.set_font(FontType.MONO20)
        brain.screen.set_pen_color(Color.PURPLE)
        brain.screen.print(textReadout, precision=screen_precision)
        brain.screen.render()
        if textReadout == "done!":
            break
        wait(5, MSEC)
    wait(1.2, SECONDS)
    brain.screen.clear_screen()
    brain.screen.set_fill_color(Color.TRANSPARENT)
    brain.screen.set_font(FontType.MONO15)
    brain.screen.set_pen_color(Color.GREEN)
    screen_precision = 2
    while True:
        brain.screen.clear_screen()
        brain.screen.set_cursor(1, 1)
        brain.screen.print("Program: ")
        if auto_side == "l":
            brain.screen.print("Left ")
        elif auto_side == "r":
            brain.screen.print("Right ")
        elif auto_side == "m":
            brain.screen.set_pen_color(Color.RED)
            brain.screen.print("AuBP ")
        else:
            brain.screen.set_pen_color(Color.CYAN)
            brain.screen.print("One Inch ")
        if Auto_color == "r":
            brain.screen.set_pen_color(Color.RED)
            brain.screen.print("Red ")
            brain.screen.next_row()
        elif Auto_color == "b":
            brain.screen.set_pen_color(Color.BLUE)
            brain.screen.print("Blue ")
            brain.screen.next_row()
        else:
            brain.screen.set_pen_color(Color.ORANGE)
            brain.screen.print("No Color Sorting")
            brain.screen.next_row()
        brain.screen.set_pen_color(Color.GREEN)
        brain.screen.print("port  Name      temp  power   effeciency torque(Nm)")
        brain.screen.next_row()
        if Right1.temperature(PERCENT) > 2:
            if Right1.temperature(PERCENT) > 70:
                brain.screen.set_fill_color(Color.RED)
            brain.screen.print(str("P11 Right1: ") + str(str(Right1.temperature(PERCENT))))
            brain.screen.print("    ")
            brain.screen.print(Right1.power(PowerUnits.WATT), precision=screen_precision)
            brain.screen.print("    ")
            brain.screen.print(Right1.efficiency(PERCENT), precision=screen_precision)
            brain.screen.print("    ")
            brain.screen.print(Right1.torque(TorqueUnits.NM), precision=screen_precision)
            brain.screen.next_row()
            brain.screen.set_fill_color(Color.TRANSPARENT)
        if Right2.temperature(PERCENT) > 2:
            if Right2.temperature(PERCENT) > 70:
                brain.screen.set_fill_color(Color.RED)
            brain.screen.print(str("P13 Right2: ") + str(str(Right2.temperature(PERCENT))))
            brain.screen.print("    ")
            brain.screen.print(Right2.power(PowerUnits.WATT), precision=screen_precision)
            brain.screen.print("    ")
            brain.screen.print(Right2.efficiency(PERCENT), precision=screen_precision)
            brain.screen.print("    ")
            brain.screen.print(Right2.torque(TorqueUnits.NM), precision=screen_precision)
            brain.screen.next_row()
            brain.screen.set_fill_color(Color.TRANSPARENT)
        if Right3.temperature(PERCENT) > 2:
            if Right3.temperature(PERCENT) > 70:
                brain.screen.set_fill_color(Color.RED)
            brain.screen.print(str("P12 Right3: ") + str(str(Right3.temperature(PERCENT))))
            brain.screen.print(Right3.power(PowerUnits.WATT), precision=screen_precision)
            brain.screen.print("    ")
            brain.screen.print(Right3.efficiency(PERCENT), precision=screen_precision)
            brain.screen.print("    ")
            brain.screen.print(Right3.torque(TorqueUnits.NM), precision=screen_precision)
            brain.screen.next_row()
            brain.screen.set_fill_color(Color.TRANSPARENT)
        if left1.temperature(PERCENT) > 2:
            if left1.temperature(PERCENT) > 70:
                brain.screen.set_fill_color(Color.RED)
            brain.screen.print(str("P20 Left1: ") + str(str(left1.temperature(PERCENT))))
            brain.screen.print("    ")
            brain.screen.print(left1.power(PowerUnits.WATT), precision=screen_precision)
            brain.screen.print("    ")
            brain.screen.print(left1.efficiency(PERCENT), precision=screen_precision)
            brain.screen.print("    ")
            brain.screen.print(left1.torque(TorqueUnits.NM), precision=screen_precision)
            brain.screen.next_row()
            brain.screen.set_fill_color(Color.TRANSPARENT)
        if left2.temperature(PERCENT) > 2:
            if left2.temperature(PERCENT) > 70:
                brain.screen.set_fill_color(Color.RED)
            brain.screen.print(str("P19 Left2: ") + str(str(left2.temperature(PERCENT))))
            brain.screen.print("    ")
            brain.screen.print(left2.power(PowerUnits.WATT), precision=screen_precision)
            brain.screen.print("    ")
            brain.screen.print(left2.efficiency(PERCENT), precision=screen_precision)
            brain.screen.print("    ")
            brain.screen.print(left2.torque(TorqueUnits.NM), precision=screen_precision)
            brain.screen.next_row()
            brain.screen.set_fill_color(Color.TRANSPARENT)
        if left3.temperature(PERCENT) > 2:
            if left3.temperature(PERCENT) > 70:
                brain.screen.set_fill_color(Color.RED)
            brain.screen.print(str("P18 Left3: ") + str(str(left3.temperature(PERCENT))))
            brain.screen.print("    ")
            brain.screen.print(left3.power(PowerUnits.WATT), precision=screen_precision)
            brain.screen.print("    ")
            brain.screen.print(left3.efficiency(PERCENT), precision=screen_precision)
            brain.screen.print("    ")
            brain.screen.print(left3.torque(TorqueUnits.NM), precision=screen_precision)
            brain.screen.next_row()
            brain.screen.set_fill_color(Color.TRANSPARENT)
        if colorsorting.temperature(PERCENT) > 2:
            if colorsorting.temperature(PERCENT) > 70:
                brain.screen.set_fill_color(Color.RED)
            brain.screen.print(str("P15 colorsorting:") + str(str(colorsorting.temperature(PERCENT))))
            brain.screen.print("    ")
            brain.screen.print(colorsorting.power(PowerUnits.WATT), precision=screen_precision)
            brain.screen.print("    ")
            brain.screen.print(colorsorting.efficiency(PERCENT), precision=screen_precision)
            brain.screen.print("    ")
            brain.screen.print(colorsorting.torque(TorqueUnits.NM), precision=screen_precision)
            brain.screen.next_row()
            brain.screen.set_fill_color(Color.TRANSPARENT)
        if TopMotor.temperature(PERCENT) > 2:
            if TopMotor.temperature(PERCENT) > 70:
                brain.screen.set_fill_color(Color.RED)
            brain.screen.print(str("P1 TopMotor: ") + str(str(TopMotor.temperature(PERCENT))))
            brain.screen.print("    ")
            brain.screen.print(TopMotor.power(PowerUnits.WATT), precision=screen_precision)
            brain.screen.print("    ")
            brain.screen.print(TopMotor.efficiency(PERCENT), precision=screen_precision)
            brain.screen.print("    ")
            brain.screen.print(TopMotor.torque(TorqueUnits.NM), precision=screen_precision)
            brain.screen.next_row()
            brain.screen.set_fill_color(Color.TRANSPARENT)
        if Intake.temperature(PERCENT) > 2:
            if Intake.temperature(PERCENT) > 70:
                brain.screen.set_fill_color(Color.RED)
            brain.screen.print(str("P14 Intake: ") + str(str(Intake.temperature(PERCENT))))
            brain.screen.print("    ")
            brain.screen.print(Intake.power(PowerUnits.WATT), precision=screen_precision)
            brain.screen.print("    ")
            brain.screen.print(Intake.efficiency(PERCENT), precision=screen_precision)
            brain.screen.print("    ")
            brain.screen.print(Intake.torque(TorqueUnits.NM), precision=screen_precision)
            brain.screen.next_row()
            brain.screen.set_fill_color(Color.TRANSPARENT)
        if inertial_for_auton.acceleration(XAXIS) > 0:
            brain.screen.print(str("P6 Inertial:") + str(str("Acceleration in Gs(x,y,z): ") + str(str(str(round(inertial_for_auton.acceleration(XAXIS), 1))) + str(str(" , ") + str(str(str(round(inertial_for_auton.acceleration(YAXIS), 1))) + str(str(" , ") + str(str(round(inertial_for_auton.acceleration(ZAXIS), 1)))))))))
            brain.screen.next_row()
            brain.screen.print(str("Orientation (R,P,Y): ") + str(str(str(round(inertial_for_auton.orientation(ROLL, DEGREES), 1))) + str(str(" , ") + str(str(str(round(inertial_for_auton.orientation(PITCH, DEGREES), 1))) + str(str(" , ") + str(str(round(inertial_for_auton.orientation(YAW, DEGREES), 1))))))))
            brain.screen.next_row()
            brain.screen.print(str("Heading: ") + str(str(round(inertial_for_auton.heading(DEGREES), 1))))
            brain.screen.next_row()
            brain.screen.print(str("Rotation: ") + str(str(round(inertial_for_auton.rotation(DEGREES), 1))))
            brain.screen.next_row()
            brain.screen.render()
        wait(5, MSEC)

#handles variable controlled functions
def when_started3():
    global my_event, fake_auto, sd_is_in, Accuracy, Front_Down, right_temp, left_temp, Descoring, turn_mod, DegreesToTurn, TurnData, driveMod, auto_side, Auto_color, leftData, RightData, IntakeData, iteration, LeftDriveData, RightDriveData, IntakeDriveData, Left_Iter, Right_Iter, Intake_Iter, textReadout, LeftVP, RightVP, BreakParsing, AuBP_MaxVP, colortoggle, skillsRun, recording, MatchLoadData, TopMotorDATA, TopMotorDriveDATA, MatchLoadDriveDATA, matchload_iter, top_iter, use_turningInertial, LastFront_down, turn_to_h_dif, Kp, Ki, Kd, error, loop_delay, last_error, integral, position, integral_limit, error_threshhold, derivative, POWER, intake_speed, reconcile_velocity, screen_precision, console_precision, ai_vision_2_index, ai_vision_2_objects, controller_1_precision
    sd_is_in = False
    if brain.sdcard.is_inserted():

        print("sd card inserted!")
        sd_is_in = True
    init_setup()
    # right button - accuracy toggle
    while True:
        if controller_1.buttonUp.pressing():
            colorsorting.stop()
        if Front_Down == 1:
            frontPiston.set(True)
        else:
            frontPiston.set(False)
        if Descoring == 1:
            DeScorer.set(True)
        else:
            DeScorer.set(False)
        wait(5, MSEC)
