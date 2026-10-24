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
    br.robot.turn(68)
    br.robot.arc(2000, 12)
    br.robot.turn(10)
    br.driveForDistance(180, 40, Stop.BRAKE, False)
    br.driveForDistance(-60, 200)
    br.robot.turn(90)
    br.driveForDistance(300, 200)
    br.robot.turn(-20)
    br.driveForDistance(100, 200)
    br.robot.turn(50)
    br.driveForDistance(500, 200)


if __name__ == "__main__":
    r = current_robot()
    run(r)
