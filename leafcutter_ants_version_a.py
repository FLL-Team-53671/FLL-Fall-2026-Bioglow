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


# 1 square away from the first bold line with wheels touching the wall and the back right wheel is basically on top of the third bold line
def run(br: BaseRobot):
    br.robot.arc(-80, 50)
    br.driveForDistance(610, 200)  # Stop.BRAKE, False)
    br.robot.turn(68)
    br.robot.arc(2000, 12)
    br.robot.turn(15)
    br.driveForDistance(160, 40)  # Stop.BRAKE, False)
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
