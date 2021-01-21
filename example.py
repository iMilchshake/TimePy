from TimePy.TimePy import *
import time

# initialize Controller
timeCtrl = TimeController()

# save times throughout the program
timeCtrl.addTime("start")
time.sleep(0.15)
timeCtrl.addTime("loaded file")
time.sleep(0.24)
timeCtrl.addTime("processed file")
time.sleep(0.10)
timeCtrl.addTime("saved file")

# print results
print(timeCtrl)  # default print
timeCtrl.print(unit='ms', decimals=3, show_deltas=False, show_notes=False)  # custom settings
timeCtrl.barChart()  # bar chart
