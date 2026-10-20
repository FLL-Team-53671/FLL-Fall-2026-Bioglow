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
    br.robot.arc(2000, 10)
    br.driveForDistance(220, 40, Stop.BRAKE, False)
    br.driveForDistance(-220, 40, Stop.BRAKE, False)
    br.robot.arc(2000, -10)
    br.robot.turn(-80)
    br.driveForDistance(-700, 200, Stop.BRAKE, False)
if __name__ == "__main__":
    r = current_robot()
    run(r)
