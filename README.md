# TimePY

A simple python library to measure and display timings of your code.

## Example usage 
```python
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
```

### Outputs
#### Default
```
[0]: 0.0s - "start"
(0.15s) 
[1]: 0.15s - "loaded file"
(0.24s) 
[2]: 0.39s - "processed file"
(0.1s) 
[3]: 0.49s - "saved file"
```
#### Custom settings
```
[0]: 0.0ms
[1]: 150.558ms
[2]: 390.892ms
[3]: 490.896ms
```
#### Bar chart
```
[1] loaded file (0.15s)     █████████████████████████
[2] processed file (0.24s)  ████████████████████████████████████████
[3] saved file (0.1s)       ████████████████▋
```

## Efficiency

Each added time adds an overhead of about 0.6 nanoseconds. So TimePy should have no impact on performance for normal use cases. (see [time_measure.py](time_measure.py))