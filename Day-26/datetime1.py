

from datetime import date,time,datetime,timedelta
'''
today = date.today()

print(today)
print(today.day)
print(today.month)
print(today.year)
print(today.weekday())

'''

'''
dt,month,year = list(map(int,input("[YYYY-MM-DD]").split('-')))
print(date(year,month,dt))

'''


'''
t=time(23,50,12)
print(t)
print(t.hour)
print(t.minute)
print(t.second)

'''


'''
dt=datetime.now()
print(dt)
print(dt.strftime('%D-%m-%Y %H:%M:%S'))
print(dt.strftime('%D-%m-%Y %H:%M:%S %p'))
print(dt.strftime('%d %b %Y %H:%M:%S %p'))
print(dt.strftime('%d %B %Y %H:%M:%S %p'))
print(dt.strftime('%a %d %Y %H:%M:%S %p'))
print(dt.strftime('%A %d %Y %H:%M:%S %p'))

'''

'''
dt=datetime.now()
print(dt)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)
print(dt.month)
print(dt.year)
print(dt.weekday())

print(dt.strftime('%D-%m-%Y %H:%M:%S'))
print(dt.strftime('%D-%m-%Y %H:%M:%S %p'))
print(dt.strftime('%d %b %Y %H:%M:%S %p'))
print(dt.strftime('%d %B %Y %H:%M:%S %p'))
print(dt.strftime('%a %d %Y %H:%M:%S %p'))
print(dt.strftime('%A %d %Y %H:%M:%S %p'))

'''

'''
t=date.today()
n=datetime.now()
t7=t+timedelta(days=7)
t5=t-timedelta(days=7)

n15=n+timedelta(minutes=15)
print(t,t7,t5)
print(n,n15)
'''