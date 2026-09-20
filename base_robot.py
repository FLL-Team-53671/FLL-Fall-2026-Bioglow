"""
BaseRobot functionality shared by all of the robot designs in robots.py.
"""

# from typing import cast
from pybricks.pupdevices import Motor, ColorSensor

from pybricks.parameters import (
    Port,
    Direction,
    Axis,
    Side,
    Stop,
    Color,
    Button,
    Icon,
)
from pybricks.robotics import DriveBase
from pybricks.hubs import PrimeHub
from pybricks.tools import wait
from pybricks import version
from pybricks.pupdevices import UltrasonicSensor
from pybricks.parameters import Port
from pybricks.pupdevices import Motor

class BaseRobot:
    """
    Base robot with functionality that works across a variety of robot designs.

    Don't use BaseRobot directly. Instead, use robot classes that extend it.
    """

    hub: PrimeHub | None = None
    leftDriveMotor: Motor | None = None
    rightDriveMotor: Motor | None = None
    robot: DriveBase | None = None
    leftAttachmentMotor: Motor | None = None
    rightAttachmentMotor: Motor | None = None
    colorSensor: ColorSensor | None = None

    # Write all of the "things" that your robot will need to do.
    # These methods will then be available for team members to program the robot
    # their mission
    #
    # Here, we have two examples to get you started.
    def moveLeftAttachmentMotorForMillis(
        self,
        millis,
        speed,
    ):
        """
        Moves the left attachment motor for a set amount of time

        Example:

        >>> moveLeftAttachmentMotorForMillis(millis=500, speedPct=50)

        Args:

        millis (REQUIRED integer, > 0): how many miliseconds the left \
        attachment motor will turn for. A millisecond is 0.001 of a second, \
        so 5000 is 5 seconds.

        speed (REQUIRED integer): Controls how fast \
        the motor/motors will move. Positive numbers move the motor right, \
        negative numbers turn it to the left.
        """
        self.leftAttachmentMotor.run_time(speed, millis)

    def moveArmUpIfDown(self):
        self.moveLeftAttachmentMotorForMillis(1300, 90)

    def moveArmDownIfUp(self):
        self.moveLeftAttachmentMotorForMillis(1300, -90)

    def driveForDistance(
        self,
        distance,
        speed,
        then=Stop.BRAKE,
        gyro=True,
    ):
        """
        driveForDistance moves \
        the robot forward a certain amount \

        Parameters:
        -------------
        distance: REQUIRED how far forward the robot will move \
        positive numbers move it forward \
        and negative numbers move the robot backward \
        -------------
        speed: REQUIRED this controls how fast the robot will move \
        positive numbers move the robot forward \
        negative numbers move the robot backward \
        -------------
        then: OPTIONAL this function tells the robot what to do \
        after the current line of code is done running \
        our default for then is stop.BRAKE \
        stop.BRAKE tells the robot that when it stops \
        to stop and then dont do anything \
        untill the next line of code \
        -------------
        gyro: OPTIONAL gyro is used most of the time during our code \
        this function gives us the option to turn off gyro \
        if we need to for some reason \
        gyro is a tool that looks at whats in front of it \
        and as the robot is moving gyro will make sure that \
        the robot is more acurate than before \
        -------------
        """
        self.robot.use_gyro(gyro)
        self.robot.settings(straight_speed=speed)
        self.robot.straight(distance, then, wait)


# This BaseRobot class file is not meant to be run like the mission files.
# But if someone does try (accidentally probably) to run it, show this
# error message.
if __name__ == "__main__":
    print("Don't run the BaseRobot class file. Nothing to do here.")
    print("You probably meant to run one of the mission files.")
