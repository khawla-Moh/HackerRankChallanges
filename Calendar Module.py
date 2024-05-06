import calendar
month,day,year=list(map(int,input().split()))
c1=calendar.weekday(year,month,day)

print((calendar.day_name[c1]).upper())

