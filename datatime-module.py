                # DATATIME MODULES
                
        #Datetim(date,time,datetime,timezone,timedelta)
"""        
import datetime
print(dir(datetime))

"""
#output

"""
['MAXYEAR', 'MINYEAR', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', 
 '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']
"""

import datetime

#date
"""
mydate=datetime.date(2022,1,1)
print(mydate)
"""
#output
#2022-01-01

# current date

currentDate=datetime.date.today()
print(currentDate)

#output
#2023-06-16

#display current year

currentYear=currentDate.year
print(currentYear)
#output
#2023

currentMonth=currentDate.month
print(currentMonth)
#output
#6

currentDay=currentDate.day
print(currentDay)
#output
#16


# display weekdays

# 0-6 (0-monday,1-tuesday......6-sunday)

print(currentDate.weekday())
#output
#4---> its a thursday

#isoweekday   # 1-monday,2-tuesday.....7-sunday

print(currentDate.isoweekday())
#output
#5 -->its a thursday

          
          
          # like as arithmetic operations
          

# timedelta ---> difference between 2 days
# timedalta + day

todayDate=datetime.date.today()
tdelta=datetime.timedelta(days=5)

print(todayDate)
print(tdelta)
print(todayDate+tdelta)  # addition 16+5=21
print(todayDate-tdelta)  # subtraction 16-5=11

#output

#2023-06-16
#5 days, 0:00:00
#2023-06-21
#2023-06-11


# to find a number of days passed in this year( days and time)

newyear=datetime.date(2022,1,1)
print("number of days passed:",todayDate-newyear)

#output
#number of days passed: 531 days, 0:00:00


# to find a number of days passed in this year(only days)

newyear=datetime.date(2021,1,1)
print("number of days passed:",(todayDate-newyear).days)

#output

#number of days passed: 896





# time --> hrs/mins/microsecs

mytime=datetime.time(4,45,23,234354)
                    #h,m,s,microsecs
print(mytime)


#output
#04:45:23.234354


print(mytime.hour)
print(mytime.minute)
print(mytime.second)
print(mytime.microsecond)

#output

#4
#45
#23
#234354


# date + time

myday=datetime.datetime(2020,1,1,7,56,34,454534)
print(myday)
print(myday.year)
print(myday.month)
print(myday.day)
print(myday.hour)
print(myday.minute)
print(myday.second)
print(myday.microsecond)

#output

#2020-01-01 07:56:34.454534
#2020
#1
#1
#7
#56
#34
#454534



#------------------------------------------------------------------------------------------------------------


# current data and time

tday=datetime.datetime.today()
print(tday)

tday_now=datetime.datetime.now()   #python third party module
print(tday_now)

tday_utc=datetime.datetime.utcnow()
print(tday_utc)

# same output

#2023-06-17 00:00:34.552190
#2023-06-17 00:00:34.552189
#2023-06-17 07:00:34.552189  # 1st jan 1970...(based)  #universal timing 



# using timestamp

mydate=datetime.date.fromtimestamp(15454545454)
print(mydate)

#output
#2459-09-25


# conversion of datetime to string format
# datetime -->string
# strf-->predefined method --(formated string)

tdate=datetime.datetime.now()
print(tdate)


# %H-hours   %M-minutes  %S-seconds  %s-micro seconds

# %d-day , %m-month(1,2,3),%B-January,febuary..), %b(jan,feb....) ,%Y-YYYY ,%y-yy

mytime=tdate.strftime("%H :%M : %S")
print(mytime)

#output
#00 :09 : 29


mydate=tdate.strftime("%d /%m / %y")
print(mydate)

#output
#17 /06 / 23

# sting format

mydatetime=tdate.strftime("%d /%m / %y, %H :%M : %S")
print(mydatetime)


#output
#17 /06 / 23, 00 :12 : 18


#-------------------------------------------------------------------------------------------


# sting to datetime
# function--> strptime

date_str="2 october 2022"
print(date_str)
print(datetime.datetime.strptime(date_str,"%d %B %Y"))

#output

#2 october 2022
#2022-10-02 00:00:00



