from pybricks.tools import hub_menu
import sample_mission1
import xbox_remote_control
from current_robot import current_robot
import Across_the_board
import leafcutter_ants
import drone_mission

while True:
    program = hub_menu("x", "s")
    r = current_robot()
    if program == "x":
        xbox_remote_control.run(r)
    elif program == "A":
        Across_the_board.run(r)
    elif program == "L":
        leafcutter_ants.run(r)
    elif program == "D":
        drone_mission.run(r)
