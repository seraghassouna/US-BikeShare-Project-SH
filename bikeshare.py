"""
This program was written
using Anaconda release 2021.05 with python version 3.8
and the IDE is Spyder 4.2.5
______
The main program structure was maintained, but slightly modified
to fit the flow of data and achieve better readability.
______
Modification no. 1 as per requested
"""

import time
import pandas as pd
import math
from utilities import get_lower, get_weekday_apply, get_month, get_hour\
    , seconds_described

# CONSTANTS
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

valid_city_set = {'Chicago',
                  'New York City',
                  'New York',
                  'Washington'}

valid_yes_no_set = {'Yes',
                    'Y',
                    'No',
                    'N'}

valid_month_set = {'January',
                   'Jan',
                   'February',
                   'Feb',
                   'March',
                   'Mar',
                   'April',
                   'Apr',
                   'May',
                   'June',
                   'Jun',
                   'All'}

month_alias = {'jan':'january',
               'feb':'february',
               'mar':'march',
               'apr':'april',
               'jun':'june'}

valid_day_set = {'Saturday',
                 'Sat',
                 'Sunday',
                 'Sun',
                 'Monday',
                 'Mon',
                 'Tuesday',
                 'Tue',
                 'Wednesday',
                 'Wed',
                 'Thursday',
                 'Thu',
                 'Friday',
                 'Fri',
                 'All'}

day_alias = {'sat':'saturday',
             'sun':'sunday',
             'mon':'monday',
             'tue':'tuesday',
             'wed':'wednesday',
             'thu':'thursday',
             'fri':'friday'}

#_____________________________________________________
#  PROGRAM FUNCTIONS
def get_filters_n_load():
    """
    Asks user to specify a city, month, and day to analyze.
    Loads the data and asks user to display the 1st 5 rows.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
        (dataframe) df - the original raw data [to be passed to "filter_data" function]
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington).
    city_msg = 'Please Choose The City of interset .. Chicago, New York City or Washington.\n'
    city = get_lower(valid_city_set,city_msg)
    if city == 'new york':
        city = 'new york city'
    
    #load the raw data
    df = pd.read_csv(CITY_DATA[city])
    
    #prompt the user to display 5 raw values in loop untill refusal (Rubric requierment)
    df_shape = df.shape
    with pd.option_context("display.max_columns",df_shape[1]):
        pental_packs = math.ceil(df_shape[0]/5)
        answer = 'yes' #initialize the while loop conditional value
        i = 0
        while answer in ['yes', 'y']:
            if i == 0:
                yes_no_msg = 'Would you like to see the first 5 rows of the raw data? .. Enter yes or no.\n'
            else:
                yes_no_msg = 'Would you like to see the next 5 rows of the raw data? .. Enter yes or no.\n'
            answer = get_lower(valid_yes_no_set,yes_no_msg)
            if answer in ['yes', 'y']:
                print('Pental Pack no. = {} from total of {} pack(s).\n...\n'\
                      .format(i+1, pental_packs))
                print(df.iloc[i:i+5])
                i += 1
                print('-'*40)
        #___________

    # get user input for month (all, january, february, ... , june)
    month_msg = 'Choose the month to filter by, or \'all\' to apply no month filter\n'
    month_msg += 'Valid Options: [all, january, february, march, april, may, june]\n'
    month_msg += 'or their aliases.\n'
    month = get_lower(valid_month_set,month_msg)
    if month in month_alias.keys():
        month = month_alias[month]

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day_msg = 'Choose the day to filter by .. or \'all\' to apply no day filter\n'
    day_msg += 'Valid Options: [all, saturday, sunday, monday, tuesday, wednesday, thursday, friday]\n'
    day_msg += 'or their aliases.\n'
    day = get_lower(valid_day_set,day_msg)
    if day in day_alias.keys():
        day = day_alias[day]

    print('-'*40)
    return city, month, day, df


def filter_data(df, city, month, day):
    """
    Filters by month and day if applicable.

    Args:
        (dataframe) df - the original raw data
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    no_filter_list=[]
    #filter by month (of the start time)
    if month != 'all':
        df = df[df['Start Time'].apply(get_month) == month]
    else:
        no_filter_list.append('month')
    #filter by week day (of the start time)
    if day != 'all':
        df = df[df['Start Time'].apply(get_weekday_apply) == day]
    else:
        no_filter_list.append('week day')
    #insert a column for months
    df['Month'] = df['Start Time'].apply(get_month)
    #insert a column for week days
    df['Week Day'] = df['Start Time'].apply(get_weekday_apply)
    #insert a column for start hours
    df['Start Hour'] = df['Start Time'].apply(get_hour)

    return df, no_filter_list


def time_stats(df,no_filter_list):
    """
    Displays statistics on the most frequent times of travel.
    INPUTS:
        df: the dataframe to apply statistics on.
        state: whether the data are original or filtered.
        no_filter_list: a list that states if data were not filtered
        by week day and/or month.
    """

    print('\n[1] Calculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    if 'month' in no_filter_list:
        df_month = df['Month'].describe()
        print('The most common month is {} with frequency {}.\n'.format(df_month['top'],\
                                                                 df_month['freq']))

    # display the most common day of week
    if 'week day' in no_filter_list:
        df_weekday = df['Week Day'].describe()
        print('The most common day of week is {} with frequency {}.\n'\
          .format(df_weekday['top'], df_weekday['freq']))

    # display the most common start hour
    df_hour = df['Start Hour'].describe()
    print('The most common start hour is \'{}\' with frequency {}.\n'\
          .format(df_hour['top'], df_hour['freq']))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\n[2] Calculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    

    # display most commonly used start station
    df_start = df['Start Station'].describe()
    print('The most commonly used start station is {} with frequency {}.\n'\
          .format(df_start['top'], df_start['freq']))

    # display most commonly used end station
    df_end = df['End Station'].describe()
    print('The most commonly used end station is {} with frequency {}.\n'\
          .format(df_end['top'], df_end['freq']))

    # display most frequent combination of start station and end station trip
    df_comb = df['Start Station'] + ' to ' + df['End Station']
    #   note: this way is prefered from using "groupby" only for the purpose of displaying
    #   as "describe" method is fairly clear (for this task) with descriptive data.
    df_comb_desc = df_comb.describe()
    print('The most frequent combination of start station and end station trip is:\n{}\nwith frequency {}.'\
                  .format(df_comb_desc['top'], df_comb_desc['freq']))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\n[3] Calculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_duration = df['Trip Duration'].sum()
    total_duration = seconds_described(total_duration)
    print('Total travel time = {}\n'.format(total_duration))

    # display mean travel time
    avg_duration = df['Trip Duration'].mean()
    avg_duration = seconds_described(avg_duration)
    print('The average travel time = {}\n'.format(avg_duration))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\n[4] Calculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    try:
        print('User Types\n')
        print(df['User Type'].value_counts())
        print('-'*15)
    except:
        print('Not included in the dataset.')
        print('-'*15)

    # Display counts of gender
    try:
        print('Gender\n')
        print(df['Gender'].value_counts())
        print('-'*15)
    except:
        print('Not included in the dataset.')
        print('-'*15)


    # Display earliest, most recent, and most common year of birth
    try:
        print('Birth Year\n')
        earliest = df['Birth Year'].min()
        recent = df['Birth Year'].max()
        mode = df['Birth Year'].mode()[0]
        print('Earliest birth year is {}.\n'.format(earliest))
        print('Most recent birth year is {}.\n'.format(recent))
        print('Most common year of birth is {}.\n'.format(mode))
    except:
        print('Not included in the dataset.')
        print('-'*15)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day, df = get_filters_n_load()
        df, no_filter_list = filter_data(df, city, month, day)

        time_stats(df,no_filter_list)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        yes_no_msg = '\nWould you like to restart? Enter yes or no.\n'
        restart = get_lower(valid_yes_no_set,yes_no_msg)
        if restart == 'y':
            restart = 'yes'
        if restart == 'n':
            restart = 'no'
        #___
        if restart != 'yes':
            break


if __name__ == "__main__":
	main()
