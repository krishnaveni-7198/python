#simple adding

class Time:
    def __init__(self, hours, minutes, seconds):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __add__(self, other):
        return self.__hours + other.__hours, self.__minutes + other.__minutes, self.__seconds + other.__seconds


obj1 = Time(1, 32, 50)
obj2 = Time(2, 5, 12)
obj3 = obj1 + obj2
print(obj3)
print()

#net code

import datetime as dt
t1 = dt.datetime.strptime('12:00:59', '%H:%M:%S')
t2 = dt.datetime.strptime('02:00:11', '%H:%M:%S')
time_zero = dt.datetime.strptime('00:00:00', '%H:%M:%S')
print((t1 - time_zero + t2).time())
