import time
import datetime

my_birth_date = datetime.datetime(1996, 9, 20, 0, 0, 0)
current_date = datetime.datetime.now()
difference = current_date - my_birth_date

# Calculate the number of days, seconds, and weeks
days = difference.days
seconds = difference.total_seconds()
weeks = days / 7  # Assuming there are 7 days in a week

# Calculate the number of years (approximate)
years = days / 365.25  # Accounting for leap years

print("Days:", days)
print("Seconds:", seconds)
print("Weeks:", weeks)
print("Years (approximate):", years)
