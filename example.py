from TimePy.TimePy import *
import time

# initialize Controller
timeCtrl = TimeController()

# save times throughout the program
timeCtrl.add_time("start")
time.sleep(0.15)
timeCtrl.add_time("loaded file")
time.sleep(0.24)
timeCtrl.add_time("processed file")
time.sleep(0.10)
timeCtrl.add_time("saved file")

# print results
timeCtrl.print()  # print times with default settings
timeCtrl.print(unit='ms', decimals=3, show_deltas=False, show_notes=False)  # custom settings
timeCtrl.bar_chart()  # print as bar chart
