import datetime
def input_manager():
    user_time_start=input("Enter a starting hour and minute time like the following : 05:22")
    user_time_end=input("Enter a ending hour and minute time like the following : 06:19")
    datetime_user_time_start=datetime.datetime.strptime(user_time_start,"HH:MM")
    datetime_user_time_end=datetime.datetime.strptime(user_time_end,"HH:MM")
    return datetime_user_time_start,datetime_user_time_end
datetime_user_time_start,datetime_user_time_end=input_manager()
while datetime_user_time_start>datetime_user_time_end:
    print("Error: Starting time must be inferior to ending time")
    datetime_user_time_start,datetime_user_time_end=input_manager()



