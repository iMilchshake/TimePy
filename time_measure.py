# measure TimePy's time overhead using TimePy itself

import TimePy.TimePy as TimePy

# initialize Controller
timeCtrl = TimePy.TimeController()

# sample size
n = 1000000

# add n timers
for i in range(n):
    timeCtrl.add_time()

# calculate and print times
t_overall = timeCtrl.get_overall_time()  # time it took to add all n timers
t_average = t_overall / n  # time it took to add one timer on average
print("overall time: ", TimePy.time_to_string(t_overall, unit='s'))
print("average time: ", TimePy.time_to_string(t_average, unit='ns'))

# output:
# overall time:  5.69s
# average time:  0.56ns
# so ~0.6ns overhead for each timer that was added
