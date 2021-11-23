import math
import time
import termgraph as tg
import termplotlib as tpl
import numpy as np


def calculate_time_difference(t1, t2):
    """ calculates the time difference between two given times """
    return abs(t1 - t2)


def time_to_string(t, unit='s', decimals=2):
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

    def __init__(self, init=True):
        """ TimeController constructor

        Args:
            init (bool, optional): If a timer should be added on object initialization. Defaults to True.
        """
        self.__timer = list()
        self.__notes = list()
        self.start_time = -1
        self.timerCount = 0
        if init:
            self.add_time("init")

    def __repr__(self):
        return self.print(do_print=False)

    def print(self, unit='s', decimals=2, show_deltas=True, show_notes=True, do_print=True):
        """returns all times and time differences

        Args:
            unit (str, optional): time-unit (s, ms, ns). Defaults to 's'.
            decimals (int, optional): amount of decimal places to show. Defaults to 2.
            show_deltas (bool, optional): if delta_times should be displayed. Defaults to True.
            show_notes (bool, optional): if each time's note should be displayed. Defaults to True.
            do_print (bool, optional): if print() should be called. Defaults to True.

        Returns:
            str: output
        """
        output = ""
        for i in range(self.timerCount):
            # add delta
            if i != 0 and show_deltas:
                output += "(%s) \n" % time_to_string(
                    self.get_difference(i - 1, i), unit, decimals)

            # add time
            output += "[%d]: %s" % (i,
                                    time_to_string(self.get_time(i), unit, decimals))

            # add note
            if show_notes and self.__notes[i] != "":
                output += " - \"%s\"" % self.__notes[i]

            # finish line
            if i < self.timerCount - 1:
                output += "\n"

        if do_print:
            print(output)
        return output

    def bar_chart(self, unit='s', decimals=2):
        """displays a bar-chart

        Args:
            unit (str, optional): time-unit (s, ms, ns). Defaults to 's'.
            decimals (int, optional): amount of decimal places to show. Defaults to 2.
        """
        timeDifferences = []
        labels = []
        for t in range(1, self.timerCount):
            timeDifferences.append(self.get_difference(t, t-1))
            labels.append("[%d] " % t + self.__notes[t] + " (%s)" %
                          time_to_string(self.get_difference(t, t-1), unit, decimals))

        fig = tpl.figure()
        fig.barh(
            timeDifferences,
            labels,
            force_ascii=False,
            show_vals=False
        )
        fig.show()

    def add_time(self, note=""):
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

    def get_time(self, i):
        """ get time at given index """
        return self.__timer[i]

    def get_times(self):
        """ get all times as a new list """
        return self.__timer.copy()

    def get_difference(self, i0, i1):
        """ calculates the time difference between two given time indexes """
        return calculate_time_difference(self.__timer[i0], self.__timer[i1])

    def get_overall_time(self):
        """ returns the overall time (from first time to last time)"""
        if self.timerCount >= 2:
            return self.get_difference(0, self.timerCount - 1)
        raise Exception("At least 2 times are needed")
