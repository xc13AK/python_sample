#!/usr/bin/python3.4
#-*- coding:UTF-8 -*-

print("the day of 2018-1-1 is MONDAY")

#get the feature day from input
year=2018 #int(input("enter the year:"))
month=int(input("enter the month:"))
day=int(input("enter the day:"))

print("new day is %s-%s-%s"%(year,month,day))

months=[31,28,31,30,31,30,31,31,30,31,30,31]
days=0
i=0
while i<month-1:
    days += months[i]
    i += 1
days += day - 1

print("delta is %s days"%days)

week=int(days)%7


if week==0:
    print("MONDAY")
elif week==1:
    print("TUSDAY")
elif week==2:
    print("WENDAY")
elif week==3:
    print("THURSDAY")
elif week==4:
    print("FRIDAY")
elif week==5:
    print("SATRDAY")
elif week==6:
    print("SUNDAY")
else:
    print("UNKNOWN")

