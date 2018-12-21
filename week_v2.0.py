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

if weekday==0:
    print("it is MONDAY!")
elif weekday==1:
    print("it is TUSDAY!")
elif weekday==2:
    print("it is WENDAY!")
elif weekday==3:
    print("it is THSDAY!")
elif weekday==4:
    print("it is FRIDAY!")
elif weekday==5:
    print("it is SARTDAY!")
elif weekday==6:
    print("it is SUNDAY!")
else:
    print("UNKNOWN")

