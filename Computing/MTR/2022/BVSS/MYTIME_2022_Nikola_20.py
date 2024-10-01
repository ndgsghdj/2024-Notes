def correct_range(num, limit):
    return 0 <= num <= limit #4

print("Time in 24-hour format should be entered as 4 digits")
valid = False
while valid == False:
    time = input("Enter a time in 24-hour format: ")
    if len(time) != 4: #1
        print("Length of input must be 4")
    elif time.isnumeric() == False: #2
        print("Input must be digits only")
    else:
        hour_int = int(time[:2])
        minute_str = time[2:]
        if not correct_range(hour_int, 23): #3
            print("Hour must be in the range 0 to 23 inclusive")
        elif not correct_range(int(minute_str), 59):
            print("Minute must be in the range 0 to 59 inclusive")
        else:
            valid = True

if 0 <= hour_int <= 11: #5
    indicator = "AM"
else:
    indicator = "PM"
new_hour = hour_int
if hour_int == 0:
    new_hour = hour_int + 12
elif hour_int >= 13:
    new_hour = hour_int - 12
converted_time = str(new_hour) + ":" + minute_str + indicator
print(converted_time)


