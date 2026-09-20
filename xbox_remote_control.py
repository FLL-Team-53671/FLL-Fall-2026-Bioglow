"""
Use an Xbox controller as a remote control for prototyping.

This is based on code written by Julian Huss and shared by Monongahela Cryptid
Cooperative team #23247. See:
https://github.com/MonongahelaCryptidCooperative/FLL-Block-2024-2025
"""

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color
from pybricks.robotics import DriveBase
from pybricks.tools import wait
from pybricks.iodevices import XboxController

from base_robot import BaseRobot
from current_robot import current_robot

CONTROLLER = None


def run(
    robot: BaseRobot,
    remote_speed: int = 200,
    remote_turn: int = 100,
    remote_accel: int = 1000,
    remote_turn_accel: int = 1000,
    attach_speed: int = 500,
):
    """
    Lanch the Xbox Controller RC Mode.
    """

    assert robot.hub is not None
    assert robot.robot is not None

    # Connect to controller if not yet connected)
    robot.hub.light.blink(Color.RED, [200, 200])
    global CONTROLLER
    if CONTROLLER == None:
        CONTROLLER = XboxController()

    # Local variables that are used in this function
    left_stick = 0
    right_stick = 0
    left_trigger = 0
    right_trigger = 0
    hub = robot.hub
    drivebase = robot.robot
    left_attach = robot.leftAttachmentMotor
    right_attach = robot.rightAttachmentMotor

    # Zero out the odometry and attachment motors
    drivebase.reset()
    if left_attach is not None:
        left_attach.reset_angle(0)
    if right_attach is not None:
        right_attach.reset_angle(0)

    # Override the drivebase values to make it easier to control
    drivebase.settings(
        remote_speed, remote_accel, remote_turn, remote_turn_accel
    )
    # Turn on Gyro
    drivebase.use_gyro(True)

    ### Main Controller Loop
    while True:
        hub.light.on(Color.BLUE)
        if Button.A in CONTROLLER.buttons.pressed():
            # If the A button is pressed print off to the console:
            # how far the robot drove,
            # how much it turned,
            # how far the attachment motors were moved
            # then reset all of these measurements
            print(drivebase.distance(), " mm driven")
            print(drivebase.angle(), " degrees turned")
            if left_attach is not None:
                print(left_attach.angle(), " degrees left attachment")
                left_attach.reset_angle(0)
            if right_attach is not None:
                print(right_attach.angle(), " degrees right attachment")
                right_attach.reset_angle(0)
            drivebase.reset()
            CONTROLLER.rumble(50, 400)
            hub.speaker.beep(500, 200)
        elif Button.X in CONTROLLER.buttons.pressed():
            # X exits RC mode and allows a new program to be selected
            drivebase.use_gyro(False)
            CONTROLLER.rumble(50, 400)
            hub.speaker.beep(500, 200)
            break
        # If neither the A/X buttons pressed see if their are stick/trigger inputs
        else:
            left_stick = convert_stick_input(CONTROLLER.joystick_left()[1])
            right_stick = convert_stick_input(CONTROLLER.joystick_right()[0])
            left_trigger = convert_stick_input(CONTROLLER.triggers()[0])
            right_trigger = convert_stick_input(CONTROLLER.triggers()[1])

            # If left/right stick input make the robot move
            if left_stick != 0 or right_stick != 0:
                drivebase.drive(
                    left_stick * remote_speed, right_stick * remote_turn
                )
            # Else stop the robot
            else:
                drivebase.brake()

            # If left trigger input make the attachment move
            if left_attach is not None:
                if left_trigger != 0:
                    if Button.LB in CONTROLLER.buttons.pressed():
                        # Control the Left attachment motor
                        # Left trigger = Left motor forward
                        # Left trigger + Left bumper  = Left motor backwards
                        left_attach.run(left_trigger * attach_speed * -1)
                    else:
                        left_attach.run(left_trigger * attach_speed)
                # Else stop the left attachment.
                else:
                    left_attach.brake()

            # If Right trigger input make the attachment move
            if right_attach is not None:
                if right_trigger != 0:
                    if Button.RB in CONTROLLER.buttons.pressed():
                        # Control the Right attachment motor
                        # Right trigger = right motor forward
                        # Right trigger + right bumper  = right motor backwards
                        right_attach.run(right_trigger * attach_speed * -1)
                    else:
                        right_attach.run(right_trigger * attach_speed)
                # Else stop the right attachment.
                else:
                    right_attach.brake()
        wait(10)


def convert_stick_input(stick):
    "Eliminate Stick Drift"
    # Convert the input from the xbox controller
    # from -100 to 100 to -1 to 1. Also change small
    # values to 0 to eliminate stick drift. Rescales the
    # inputs appropriately
    if -7 <= stick <= 7:
        # Return 0 to eliminate  stick drift
        return 0
    elif 7 > stick:
        # Rescale positive (right turning input) given that 0  to  7 = 0
        return (stick - 7) / 93
    else:
        # Rescale negative (left turning input) given that 0 to -7 = 0
        return (stick + 7) / 93


if __name__ == "__main__":
    r = current_robot()
    run(r)
