import math
import time
import termgraph as tg
import termplotlib as tpl
import numpy as np

def calculateTimeDifference(t1, t2):
    """ calculates the time difference between two given times """
    return abs(t1 - t2)


def timeToString(t, unit='s', decimals=2):
    """ returns a string representation for a given time """
    if unit == 's':
        unitFactor = 1
    elif unit == 'ms':
        unitFactor = 1000
    elif unit == 'ns':
        unitFactor = 1000000
    else:
        raise ValueError("incorrect unit")

    # apply unitFactor
    t *= unitFactor

    # truncate
    truncFactor = 10.0 ** decimals
    return str(math.trunc(t * truncFactor) / truncFactor) + unit


class TimeController:

    def __init__(self):
        self.__timer = list()
        self.__notes = list()
        self.start_time = -1
        self.timerCount = 0

    def __repr__(self):
        return self.print(do_print=False)

    def print(self, unit='s', decimals=2, show_deltas=True, show_notes=True, do_print=True):
        """ returns all times and time differences """
        output = ""
        for i in range(self.timerCount):
            # add delta
            if i != 0 and show_deltas:
                output += "(%s) \n" % timeToString(self.getDifference(i - 1, i), unit, decimals)

            # add time
            output += "[%d]: %s" % (i, timeToString(self.getTime(i), unit, decimals))

            # add note
            if show_notes and self.__notes[i] != "":
                output += " - \"%s\"" % self.__notes[i]

            # finish line
            if i < self.timerCount - 1:
                output += "\n"

        if do_print:
            print(output)
        return output

    def barChart(self, unit='s', decimals=2):
        timeDifferences = []
        labels = []
        for t in range(1, self.timerCount):
            timeDifferences.append(self.getDifference(t, t-1))
            labels.append("[%d] " % t + self.__notes[t] + " (%s)" % timeToString(self.getDifference(t, t-1), unit, decimals))

        fig = tpl.figure()
        fig.barh(
            timeDifferences,
            labels,
            force_ascii=False,
            show_vals=False
        )
        fig.show()

    def addTime(self, note=""):
        """ add a new time """
        t = time.time()

        if self.start_time == -1:
            self.start_time = t
            t = 0
        else:
            t -= self.start_time

        self.__timer.append(t)
        self.__notes.append(note)
        self.timerCount += 1

    def getTime(self, i):
        """ get time at given index """
        return self.__timer[i]

    def getDifference(self, i0, i1):
        """ calculates the time difference between two given time indexes """
        return calculateTimeDifference(self.__timer[i0], self.__timer[i1])

    def getOverallTime(self):
        """ returns the overall time (from first time to last time)"""
        if self.timerCount >= 2:
            return self.getDifference(0, self.timerCount - 1)
        raise Exception("At least 2 times are needed")
