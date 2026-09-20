from pybricks.tools import hub_menu
import xbox_remote_control
from current_robot import current_robot

while True:
    program = hub_menu("x")
    r = current_robot()
    if program == "x":
        xbox_remote_control.run(r)
