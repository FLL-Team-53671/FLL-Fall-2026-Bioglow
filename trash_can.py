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

# This is a mission program. You will have one of these for each "mission"
# Normally a mission is one run from base, but there are ways to do more than
# that if needed.


def run(br: BaseRobot):

    br.driveForDistance(245, 100)

    br.turnRightAttachmentMotor(35, 3)
    br.driveForDistance(-245, 21)


if __name__ == "__main__":
    r = current_robot()
    run(r)
