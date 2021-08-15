"""
filename = utilities.py
Purpose: a custom module that includes utility functions for bikeshare.py
"""
import datetime

#  UTILITY FUNCTIONS
def get_lower(init_set,msg):
    """
    UTILITY FUNCTION
    Asks user based on a specified message (msg) from a set of
    valid values (init_set), This function returns a lower case value from the
    valid input.
    
    Returns:
        (str) val - the lower case valid value
    """
    
    #CREATE THE WHOLE SET OF VALID VALUES
    lower_list = [x.lower() for x in init_set] #get the lower case values
    #add the lower case values to the set
    for w in lower_list:
        init_set.add(w)
    #get the value from user, whether title or lower case,
    #then convert it to lower case anyway
    val = '' #its boolean equivalent value is False
    while not val:
        val = input(msg)
        val = val.lower() #handels upper/lower & mixed case 
        if val in init_set:
            return val
        else:
            val='' #to insure the loop will work for another trial
            print('Invalid Option .. Please try again')

def get_datetime(day):
    """
    UTILITY FUNCTION 
    takes the date as a string and returns the equivalent datetime object.
    """
    return datetime.datetime(int(day[:4]),int(day[5:7]),int(day[8:10]),
                        int(day[11:13]),int(day[14:16]),int(day[17:]))

def get_weekday(day_datetime):
    """
    UTILITY FUNCTION 
    takes the datetime object and returns its week day.
    """
    week_days = {0:'monday',
                 1:'tuesday',
                 2:'wednesday',
                 3:'thursday',
                 4:'friday',
                 5:'saturday',
                 6:'sunday'}
    return week_days[day_datetime.weekday()]

def get_weekday_apply(day):
    """
    UTILITY FUNCTION 
    a compact function that takes the date as a string and returns the
    week day .. used with an ((apply)) method on a single column of the dataframe.
    """
    return get_weekday(get_datetime(day))

def get_month(day_str):
    """
    UTILITY FUNCTION 
    takes the day date (str) and returns its month.
    """
    month_dict = {'01':'january',
                  '02':'february',
                  '03':'march',
                  '04':'april',
                  '05':'may',
                  '06':'june',
                  '07':'july',
                  '08':'august',
                  '09':'september',
                  '10':'october',
                  '11':'november',
                  '12':'december'}
    return month_dict[day_str[5:7]]

def get_hour(day_str):
    """
    UTILITY FUNCTION
    just returns the hour from the date string. USED in ((apply)) method to create a 
    column of hours.
    """
    return day_str[11:13]

def seconds_described(s):
    """
    UTILITY FUNCTION
    returns the equivalent time in days, hours, minutes and seconds
    as a descriptive string.
    INPUT:
        s (int) - time in seconds.
    """
    minutes, seconds = divmod(s,60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    if days !=0:
        day_print = str(days) + ' day(s) '
        hour_print = str(hours) + ' hour(s) '
        minute_print = str(minutes) + ' minute(s) '
        sec_print = str(seconds) + ' second(s)'
    elif days == 0 and hours != 0:
        day_print = ''
        hour_print = str(hours) + ' hour(s) '
        minute_print = str(minutes) + ' minute(s) '
        sec_print = str(seconds) + ' second(s)'
    elif days == 0 and hours == 0 and minutes !=0:
        day_print = ''
        hour_print = ''
        minute_print = str(minutes) + ' minute(s) '
        sec_print = str(seconds) + ' second(s)'
    else:
        day_print = ''
        hour_print = ''
        minute_print = ''
        sec_print = str(seconds) + ' second(s)'
    
    return day_print + hour_print + minute_print + sec_print + '.'