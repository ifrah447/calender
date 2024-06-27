#!/usr/bin/python
import time;

localtime = time.localtime(time.time())
print("Local current time : ",localtime)


#!/usr/bin/python
import calendar

cal = calendar.month(2000, 1)
print("Here is the calendar:")
print(cal)
