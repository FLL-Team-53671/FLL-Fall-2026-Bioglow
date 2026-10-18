from base_robot import BaseRobot
from current_robot import current_robot

from pybricks.tools import wait
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


def run(br: BaseRobot):
    br.driveForDistance(610, 200, Stop.BRAKE, False)
    br.robot.turn(55)
    br.driveForDistance(550, 200)
    br.rightDriveMotor.run(140)
    br.leftDriveMotor.run(140)
    while True:
        if br.colorSensor.color() == White:
            br.leftDriveMotor.run(0)
            br.rightDriveMotor.run(0)
            br.driveForDistance(100, 20)
        print(br.colorSensor.color())


if __name__ == "__main__":
    r = current_robot()
    run(r)
