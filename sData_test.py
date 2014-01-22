# sData testing playground

from sData import *

robots = RobotList()
newRobot = Robot(2228)

robots.add(newRobot)

events = GameEventList()

newEvent_1 = Auto_HighGoalEvent(hot=True)
newEvent_2 = Auto_HighGoalEvent(hot=False)
newEvent_3 = HighGoalEvent()
newEvent_4 = LowGoalEvent()

events.add(newEvent_1)
events.add(newEvent_2)
events.add(newEvent_3)
print(events.getMainList())
events.undo()
events.undo()
events.redo()
events.add(newEvent_4)

print(events.getMainList())

coolBot = robots.current_robot
coolBot.addMatch(events)
coolBot.calculateStats()
print(coolBot.getAvgPoints())

input()

