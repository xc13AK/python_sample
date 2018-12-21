#!/usr/bin/python3.4
#-*- coding:UTF-8 -*-
import datetime

now = datetime.date.today()
print("now is %s/%s/%s"%(now.year,now.month,now.day))

#print("new is %s"%sys.argv[1])

new = datetime.date(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
print("the new day is %s/%s/%s"%(new.year,new.month,new.day))

delta=new-now
days=int(delta.days)
print("the days is %d"%days)

week=days%7

if week==1:
    print("SUNDAY")
elif week==2:
    print("MONDAY")
else:
    print("UNKNOWN")

