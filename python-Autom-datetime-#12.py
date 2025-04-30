
#datetime module is used to manipulate timezone 

import datetime 
current_time =  datetime.datetime.now()
print(current_time)


#now to see the diff information   
current_time = datetime.datetime.now()
print(current_time.year)
print(current_time.month)
print(current_time.day)
print(current_time.weekday())
print(current_time.date())
print(current_time.time())
print(current_time.hour)
print(current_time.minute)
print(current_time.second)
print(current_time.microsecond)
print(current_time.ctime())
print(current_time.now())
print(current_time.today())
print(current_time.timetuple())


#manual date  ----
import datetime
testdate = datetime.date(2025,12,30)
print(testdate)
print(type(testdate))
print(testdate.year)
print(testdate.month)
print(testdate.day)

#module type difference  ----
from datetime import datetime
#dt =  datetime.datetime.now() #will cause error
dt =  datetime.now() #correct


import datetime as DT
#dt =  datetime.datetime.now() #will cause error
dt= DT.datetime.now() #correct way


#comparing time  ------
import datetime
mytime= datetime.datetime.now()
print(mytime)
print(type(mytime))

myfuturetime= datetime.datetime.now()
print(myfuturetime)
print(type(myfuturetime))

print("time difference is  "  , myfuturetime-mytime)

#days difference
print((myfuturetime - mytime).days)


#another example
from datetime import datetime

start_time=datetime.strptime("2:13:57","%H:%M:%S")
end_time=datetime.strptime("11:47:52","%H:%M:%S")

print(start_time)
print(end_time)

get_diff =end_time - start_time
print(get_diff)

#in seconds
sec=  get_diff.total_seconds()
print("difference in seconds: ", sec)

#in minutes
min =  sec/60
print("differnce in minutes : ",min)

#in hours
hours =  sec / (60*60)
print("difference in hours : ",hours)



#how to check specified time zone in python -------------
import pytz
from datetime import  datetime
print(datetime.now())
ist=pytz.timezone('Asia/Kolkata')
print(datetime.now(ist))
print(type(datetime.now(ist)))
print(ist)

