import datetime

def input_manager():
    """Manage the input of the user and return the datetime object of the user input"""
    user_time_start=input("Enter a starting hour and minute time like the following : 05:22\n")
    user_time_end=input("Enter a ending hour and minute time like the following : 06:19\n")
    datetime_user_time_start=datetime.datetime.strptime(user_time_start,"%H:%M")
    datetime_user_time_end=datetime.datetime.strptime(user_time_end,"%H:%M")
    is_next_day=input("Is the ending time the next day ? (y/n)\n")
    compute_next_day(is_next_day,datetime_user_time_end)
    return datetime_user_time_start,datetime_user_time_end,is_next_day

"""Loop to get a correct time input"""
def main():
    datetime_user_time_start,datetime_user_time_end,is_next_day=input_manager()
    while datetime_user_time_start>datetime_user_time_end and is_next_day==False:
        print("Error: Starting time must be inferior to ending time")
        datetime_user_time_start,datetime_user_time_end=input_manager()
    time_difference=compute_time(datetime_user_time_start,datetime_user_time_end)
    print("The time difference is : ",time_difference)
def compute_next_day(is_next_day:str,datetime_user_time_end:datetime)->bool:
    """Compute the time between two datetime objects when the ending time is the next day"""
    is_next_day=is_next_day.lower()
    if is_next_day=="y":
        datetime_user_time_end=datetime_user_time_end+datetime.timedelta(days=1)
        return True
    else:
        return False

    
def compute_time(datetime_user_time_start:datetime,datetime_user_time_end:datetime):
    """Compute the time between two datetime objects"""
    time_difference=datetime_user_time_end-datetime_user_time_start
    return time_difference


if __name__ == '__main__':
    main()

