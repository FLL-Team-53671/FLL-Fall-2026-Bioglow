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
    # br.driveForDistance(55, 100)
    # br.robot.turn(48)
    # br.turnRightAttachmentMotor(-250, 100)
    # br.driveForDistance(455, 200)
    # br.turnRightAttachmentMotor(30, 100)
    # br.driveForDistance(-500, 200)

    br.driveForDistance(55, 100)
    br.robot.turn(48)
    br.rightAttachmentMotor.run_until_stalled(
        -100, then=Stop.BRAKE, duty_limit=50
    )
    br.driveForDistance(455, 200)
    br.rightAttachmentMotor.run_until_stalled(
        100, then=Stop.BRAKE, duty_limit=50
    )
    br.driveForDistance(-500, 200)


if __name__ == "__main__":
    r = current_robot()
    run(r)
