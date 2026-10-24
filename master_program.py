from pybricks.tools import hub_menu
import sample_mission1
import xbox_remote_control
from current_robot import current_robot
import Across_the_board
import leafcutter_ants
import drone_mission
import explodiong_seeds
import leafcutter_ants_version_a
import back_the_board

while True:
    program = hub_menu("x", "1", "2", "3", "4", "5")
    r = current_robot()
    if program == "x":
        xbox_remote_control.run(r)
    elif program == "3":
        Across_the_board.run(r)
    elif program == "4":
        leafcutter_ants_version_a.run(r)
    elif program == "1":
        drone_mission.run(r)
    elif program == "2":
        explodiong_seeds.run(r)
    elif program == "5":
        back_the_board.run(r)
