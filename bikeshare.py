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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    while True:
        cities=['chicago','new york city','washington']
        city = input("Please enter one of these city where you want to analyze your data [chicago, new york city, washington] and please feel free to copy the city name from the question to avoid any spelling mistakes \n your city is: ")
        city=city.lower()
        try:
            if city in cities:
                print("your choice is: {}".format(city))
                break
            else:
                print("wrong city")
        except ValueError:
            print("that is not a valid option")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        months=['january','february','march','april','may','june','all']
        month = input("Please enter one of these months from when you want to analyze your data [january,february,march,april,may,june,all(if you want to see all of the months)] and please feel free to copy the month name from the question to avoid any spelling mistakes \n your month is: ")
        month=month.lower()
        try:
            if month in months:
                print("your choice is: {}".format(month))
                break
            else:
                print("that is not one of the options")
        except ValueError:
            print("that is not a valid option")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        week_days=['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all']
        day = input("Please enter one of these week days from when you want to analyze your data ['sunday','monday','tuesday','wednesday','thursday','friday','saturday',all(if you want to see all of the week days)] and please feel free to copy the day name from the question to avoid any spelling mistakes \n your week day is: ")
        day=day.lower()
        try:
            if day in week_days:
                print("your choice is: {}".format(day))
                break
            else:
                print("that is not one of the options")
        except ValueError:
            print("that is not a valid option")
     
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
    df=pd.read_csv(CITY_DATA[city])
    
    # to make the right date and time format then extract the month, day and time each alone
    df['Start Time']=pd.to_datetime(df['Start Time'])
    #changed and replaced the Start time with the right format
    #adding the new coloumns
    df['month']=df['Start Time'].dt.month 
    #monthes here are numbered eg: january = 1
    df['week_day']=df['Start Time'].dt.weekday_name  
    #starts with a capital eg: Saturday not saturdau
    df['hour']=df['Start Time'].dt.hour
                      
    #applying filters
    if month != 'all':
        months=['january','february','march','april','may','june']
        month=months.index(month)+1
        df=df[df['month']==month]
        
    if day != 'all':
        df=df[df['week_day']==day.title()]
        
    return df

def raw_data(df):
    while True:
        answer=input("Do you wanna see data (5 rows) from the source? please answer with [yes or no] \n Answer: ")
        answer=answer.lower()
        i=6
        if answer == 'yes':
            print(df.iloc[0:5])
            while True:
                more_answer=input("Do you wanna see data (5 rows) more from the source? please answer with [yes or no] \n Answer: ")
                more_answer=more_answer.lower()
                if more_answer == 'yes':
                    print(df.iloc[i:i+5])
                    i=i+5
                if more_answer =='no':
                    print("i hope that you found what you were looking for")
                    break 
                else:
                    print("wrong Entry")
        if answer =='no':
                    print("i hope that you found what you were looking for")
                    break
        
        else:
            print("worng entry")
        
            
    print('-'*40)

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month= (df['month'].mode()[0])
    months_dic={1:'january',2:'february',3:'march',4:'april',5:'may',6:'june'}
    print("The most common month is {}".format(most_common_month))
    print("The most common month is {}".format(months_dic[int(most_common_month)]))
    # TO DO: display the most common day of week
    most_common_day= df['week_day'].mode()[0]
    print("The most common day is {}".format(most_common_day))
    # TO DO: display the most common start hour
    most_common_time= df['hour'].mode()[0]
    print("The most common time is {}".format(most_common_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # TO DO: display most commonly used start station
    commonly_used_start_station=df['Start Station'].mode()[0]
    print("The most common start station: {}".format(commonly_used_start_station))
    # TO DO: display most commonly used end station
    commonly_used_end_station=df['End Station'].mode()[0]
    print("The most common end station: {}".format(commonly_used_end_station))
    # TO DO: display most frequent combination of start station and end station trip
    df['Combination']=df['Start Station']+df['End Station']
    most_frequent_combination=df['Combination'].mode()[0]
    print("the most common combination is: {}".format(most_frequent_combination))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print("the total travel time is: {}".format(total_travel_time))
    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print("the average travel time is: {}".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(city, df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_count=df['User Type'].value_counts()
    print("the count of users classified to subscriber and customer is: {}".format(user_types_count))
    # TO DO: Display counts of gender
    if city != 'washington':
        gender_count=df['Gender'].value_counts()
        print("the count of Gender is: {}".format(gender_count))
        # TO DO: Display earliest, most recent, and most common year of birth
        common_year=df['Birth Year'].mode()[0]
        max_year=df['Birth Year'].max()
        min_year=df['Birth Year'].min()
        print("the most common Bith year is: {}".format(common_year))
        print("the latest Bith year is: {}".format(max_year))
        print("the earliest Bith year is: {}".format(min_year))
    else:
        print("Sorry we have limited data in washington")
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(city, df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
