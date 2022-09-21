import datetime
user_time_start=input("Enter a starting hour and minute time like the following : 05:22")
user_time_end=input("Enter a ending hour and minute time like the following : 06:19")
datetime_user_time_start=datetime.datetime.strptime(user_time_start,"HH:MM")
datetime_user_time_end=datetime.datetime.strptime(user_time_end,"HH:MM")
while datetime_user_time_start>datetime_user_time_end:
    print("Error: Starting time must be inferior to ending time")
    user_time_start=input("Enter a starting hour and minute time like the following : 05:22")
    user_time_end=input("Enter a ending hour and minute time like the following : 06:19")
    datetime_user_time_start=datetime.datetime.strptime(user_time_start,"HH:MM")
    datetime_user_time_end=datetime.datetime.strptime(user_time_end,"HH:MM")

