import datetime

from re import M

from tkinter import N

print("введите две даты в формате <день>.<месяц>.<год>\nмесяц и день всегда указываеться двумя числами")

date1 = input("введите первую дату: ")

date2 = input("введите вторую дату: ")

try:
    date1 = datetime.date(int(date1[6:]), int(date1[3:5]), int(date1[0:2])).toordinal()
    date2 = datetime.date(int(date2[6:]), int(date2[3:5]), int(date2[0:2])).toordinal()
    delta = 0

    if(date1 > date2):
        delta=date1-date2-1

    else:
        delta=date2-date1-1

    if(delta<0):
        delta=0

    print(f"прошло {delta} полных дней")

except(Exception):
    
    print("invalid date")