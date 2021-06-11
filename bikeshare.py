import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington).
    
    cities =['chicago', 'new york city', 'washington']
    city = ''
    while city not in cities:
        city = input("Which city do you want to have a closer look at? Choose one of Chicago, New York City or Washington: ").lower()
        if city not in cities:  
            print('Try again!')
        else:
            break
    print("\nYou chose, {}!".format(city))
        
    # get user input for month
    months =['all','january','february','march','april','may','june','july','august','september','october','november','december']
    month = ''
    while month not in months:
        month = input("Which month do you want to have a closer look at? Choose one of All, January, February, March, April, May, June, July, August, September, October, November, December: ").lower()
        if month not in months:  
            print('try again!')
        else:
            break
    print("\nYou chose, {}!".format(month))


    # get user input for day of week (all, monday, tuesday, ... sunday)
    days =['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    day = ''
    while day not in days:
        day = input("Which day do you want to have a closer look at? Choose one: All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday: ").lower()
        if day not in days:  
            print('Try again!')
        else:
            break
    print("\nYou chose, {}!".format(day))
    
    print("\nYour filters are: {},{},{}!".format(city, month, day))      
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months =['january','february','march','april','may','june','july','august','september','october','november','december']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
     
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
     
    # display the most common month
    months =['january','february','march','april','may','june','july','august','september','october','november','december']
    most_common_month = months[df['month'].mode()[0]-1].title()
    print("Most common month is: {}".format(most_common_month))

    # display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print("Most common day is: {}".format(most_common_day))

     # display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print("Most common start hour is: {}".format(most_common_hour))        
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    
    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("Most common start station is: {}".format(most_common_start_station))

    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("Most common end station is: {}".format(most_common_end_station))

    # display most frequent combination of start station and end station trip
    most_frequent_combination = df.groupby(['Start Station','End Station']).size().idxmax()
    print("Most frequent combination: Start Station: {} and End Station: {}".format(most_frequent_combination[0],most_frequent_combination[1]))  

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    total_travel_time_days = int(total_travel_time//(24*60*60))
    total_travel_time_hours = int((total_travel_time%(24*60*60))//(60*60))
    total_travel_time_min = int(((total_travel_time%(24*60*60))%(60*60))//60)
    total_travel_time_sec = int(((total_travel_time%(24*60*60))%(60*60))%60)
    print("Total Travel Time is: {} days {} hours {} mins {} sec".format(total_travel_time_days,total_travel_time_hours,total_travel_time_min,total_travel_time_sec))

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    mean_travel_time_days = int(mean_travel_time//(24*60*60))
    mean_travel_time_hours = int((mean_travel_time%(24*60*60))//(60*60))
    mean_travel_time_min = int(((mean_travel_time%(24*60*60))%(60*60))//60)
    mean_travel_time_sec = int(((mean_travel_time%(24*60*60))%(60*60))%60)
    print("Mean Travel Time is: {} days {} hours {} mins {} sec".format(mean_travel_time_days,mean_travel_time_hours,mean_travel_time_min,mean_travel_time_sec))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Types:\n' + user_types.to_string())
    
    # Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print('\nGender:\n' + gender.to_string())
        # Display earliest, most recent, and most common year of birth
        earliest_year_of_birth = int(df['Birth Year'].min())
        print('\nEarliest Date of Birth: {}'.format(earliest_year_of_birth))
        most_recent_year_of_birth = int(df['Birth Year'].max())
        print('Most recent Date of Birth: {}'.format(most_recent_year_of_birth))
        most_common_year_of_birth = int(df['Birth Year'].mode()[0])
        print('Most common Date of Birth: {}'.format(most_common_year_of_birth))
    except KeyError:
        print('\nSorry. Information about Gender and Birth Year is not available for the city of Washington.')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    x = input('\nDo you want to see a preview of the Raw Data? Yes or No?\n ').lower()
    a = 0
    b = 5
    while True:
        if x == 'yes':
            print(df.iloc[a:b])
            a += 5
            b += 5
        elif x == 'no':
            break
        else:
            print('Wrong Input. Try again.')
        x = input('\nDo you want to see more lines of the data? Yes or No?\n ').lower()
        

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        try:    
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            raw_data(df)
        except KeyError:
            print("Sorry there is no data for the filters you selected.\nSelect one of these month: All, January, February, March, April, May, June ")
        except IndexError:
            print("Sorry there is no data for the filters you selected.\nSelect one of these month: All, January, February, March, April, May, June")
        except ValueError:
            print("Sorry there is no data for the filters you selected.")
        
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()