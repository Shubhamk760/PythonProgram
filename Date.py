from datetime import datetime, timedelta

# Current Date
today = datetime.now().date()
print(today)

# Current Timestamp (Time only)
current_time = datetime.now().time()
print(current_time)

# Both Date & Time
current_datetime = datetime.now()
print(current_datetime)

print("                                                  ")

# Format Date
formatted_date = current_datetime.strftime("%d-%m-%Y %H:%M:%S")
print("Before formatting:", current_datetime)
print("After formatting:", formatted_date)

print("                                                  ")



# Current Date
today = datetime.now().date()

# Add 10 days to the current date
future_date = today + timedelta(days=365)

# Print the future date
print("Future date (10 days later):", future_date)


#pip install python-dateutil
# Future Date
# tomorrow = today + timedelta(days=5, years=3)
# today_str = today.isoformat()
# tomorrow_str = (today + timedelta(days=1)).isoformat()

# print(tomorrow_str)
# print(tomorrow)
