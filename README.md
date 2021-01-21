# TimePY

A simple python library to measure timings in your code

## example usage 
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

**outputs:**
```
[0]: 0.0s - "start"
(0.15s) 
[1]: 0.15s - "loaded file"
(0.24s) 
[2]: 0.39s - "processed file"
(0.1s) 
[3]: 0.49s - "saved file"
```

```
[0]: 0.0ms
[1]: 150.558ms
[2]: 390.892ms
[3]: 490.896ms
```

```
[1] loaded file (0.15s)     █████████████████████████
[2] processed file (0.24s)  ████████████████████████████████████████
[3] saved file (0.1s)       ████████████████▋
```



