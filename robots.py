"""A robot class for each different robot design.

Ideas to try:
- https://github.com/MonongahelaCryptidCooperative/RobotDesigns/blob/main/final%20assembly.pdf
- https://primelessons.org/en/RobotDesigns.html
"""

from base_robot import *



class DrivingBaseRobot(BaseRobot):
    """
    Basic driving base from the SPIKE Prime website.

    Building instructions:
    - https://spike.legoeducation.com/prime/models/bltc58e302d70cf6530
    """

    def __init__(self):
        self.hub = PrimeHub(top_side=Axis.Z, front_side=-Axis.Y)  # type: ignore
        self.leftDriveMotor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
        self.rightDriveMotor = Motor(Port.D)

        TIRE_DIAMETER = 56  # mm
        AXLE_TRACK = 103  # distance between the wheels, mm
        self.robot = DriveBase(
            self.leftDriveMotor,
            self.rightDriveMotor,
            TIRE_DIAMETER,
            AXLE_TRACK,
        )

        self.leftAttachmentMotor = Motor(Port.B)
        self.rightAttachmentMotor = Motor(Port.E)

        # self.colorSensor = ColorSensor(Port.F)


class AdvancedDrivingBaseRobot(BaseRobot):
    """The Advanced Drive Base from the SPIKE Prime website.

    Build instructions:
    https://education.lego.com/en-us/lessons/prime-competition-ready/assembling-an-advanced-driving-base/
    """

    def __init__(self):
        self.hub = PrimeHub(top_side=Axis.Z, front_side=-Axis.Y)  # type: ignore
        self.leftDriveMotor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
        self.rightDriveMotor = Motor(Port.D)

        TIRE_DIAMETER = 85  # mm
        AXLE_TRACK = 155  # distance between the wheels, mm
        self.robot = DriveBase(
            self.leftDriveMotor,
            self.rightDriveMotor,
            TIRE_DIAMETER,
            AXLE_TRACK,
        )

        self.leftAttachmentMotor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
        self.rightAttachmentMotor = Motor(Port.E)


class PiRobot(BaseRobot):
    """The Advanced Drive Base from the SPIKE Prime website.

    Build instructions:
    https://education.lego.com/en-us/lessons/prime-competition-ready/assembling-an-advanced-driving-base/
    """

    def __init__(self):
        self.hub = PrimeHub(top_side=Axis.Z, front_side=-Axis.Y)  # type: ignore
        self.leftDriveMotor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
        self.rightDriveMotor = Motor(Port.D)

        TIRE_DIAMETER = 85  # mm
        AXLE_TRACK = 155  # distance between the wheels, mm
        self.robot = DriveBase(
            self.leftDriveMotor,
            self.rightDriveMotor,
            TIRE_DIAMETER,
            AXLE_TRACK,
        )

        self.leftAttachmentMotor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
        self.rightAttachmentMotor = Motor(Port.E)
        UltrasonicSensor(Port.C)
        # left color sensor: A
        # right color sensor : C

        #distance prot is port c
# Dictionary from robot me to robot class. Make sure to add a new entry in
# this dictionary if you configure a new robot.
ROBOT_CONFIG = {
    "Cuddles": AdvancedDrivingBaseRobot,
    "RobBot": PiRobot,
}
