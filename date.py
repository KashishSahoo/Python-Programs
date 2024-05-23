import datetime

a=datetime.date.today()
print(a)

y=datetime.date.today().strftime("%Y")
print(y)

b=datetime.date.today().strftime("%B")
print(b)

d=datetime.date.today().strftime("%d")
print(d)

print("Week Number=",datetime.date.today().strftime("%W"))

print("Weekday Of Week=",datetime.date.today().strftime("%w"))

print("day of year=",datetime.date.today().strftime('%j'))

print("day of week=",datetime.date.today().strftime('%A'))

print(datetime.datetime.now())

