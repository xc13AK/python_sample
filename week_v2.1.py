#!/usr/bin/python3.4
#-*- coding:UTF-8 -*-

import datetime

#get the feature day from input
year=int(input("enter the year:"))
month=int(input("enter the month:"))
day=int(input("enter the day:"))

new=datetime.date(year,month,day)
print("the day is %s-%s-%s"%(new.year,new.month,new.day))

weekday=int(new.weekday())
week_string=["MONDAY","TUSDAY","WENDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
print("it is %s"%week_string[weekday])

