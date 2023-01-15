# Day 16: 30 Days of python programming
from datetime import date 
from datetime import datetime
# Exercises: Level 1

# Question 1
now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
print(f"{day}/{month}/{year} {hour}:{minute}")
timestamp = now.timestamp()
print('timestamp', timestamp)

# Question 2
t = now.strftime("%m/%d/%Y, %H:%M:%S")
print("Time",t)

# Question 3
today = "5 December, 2019"
string_to_time = datetime.strptime(today, "%d %B, %Y")
print("5 December, 2019 =",string_to_time)

# Question 4
current_date = date(year=2022, month=12, day=19)
new_year = date(year=2023, month=1, day=1)
timeleft_for_newyear = new_year -current_date
print("difference bewteen now and new year is",timeleft_for_newyear)

# Question 5
current_date = date(year=2022, month=12, day=19)
old_time = date(year=1970, month=1, day=1)
time_difference = current_date - old_time
print("Difference is ",time_difference)
