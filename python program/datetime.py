import datetime as dt
#to print current date
current_date=dt.date.today()
print(current_date)
#we can also create the date
new=dt.date(2012,1,23)
print(new)
print("year is",new.year)
print("month is",new.month)
print("date is",new.day)
#we can also create the time and call
times=dt.time(1,23,45,66666)
print(times)
print("hour is",times.hour)
print("minutes is",times.minute)
print("second is ",times.second)
print("microsecond",times.microsecond)
#to print current date and time
current_datetime=dt.datetime.now()
print(current_datetime)
#we can also create it by own
news=dt.datetime(2011,2,27,1,23,45)
print(news.date())
print(news.time())
#to find difference between two year
curret=dt.datetime.now()
later=dt.datetime(2025,1,23)
diff=later-curret
print(diff)
#diiferent format
gayu=dt.datetime.now()
print(gayu)
a=gayu.strftime("%A %b %d %y")
print(a)
                

