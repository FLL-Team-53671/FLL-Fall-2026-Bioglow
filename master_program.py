from pybricks.tools import hub_menu
import sample_mission1
import xbox_remote_control
from current_robot import current_robot

while True:
    program = hub_menu("x", "s")
    r = current_robot()
    if program == "x":
        xbox_remote_control.run(r)
    elif program == "s":
        sample_mission1.run(r)
