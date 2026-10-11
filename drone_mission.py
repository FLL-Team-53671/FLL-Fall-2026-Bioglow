from base_robot import BaseRobot
from current_robot import current_robot

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
    # br.rightAttachmentMotor.run_target(100, 180)
    br.driveForDistance(630, 200, Stop.BRAKE, False)
    br.driveForDistance(-630, 200, Stop.BRAKE, False)
    #   br.robot.arc(-50, 360)


if __name__ == "__main__":
    r = current_robot()
    run(r)
