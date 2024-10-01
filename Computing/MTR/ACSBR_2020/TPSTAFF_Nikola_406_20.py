times = []
times_workers = []

for _ in range(5):
    name = input("Enter name of staff: ")

    check_timein = False

    while True:
        try:
            if check_timein:
                time_in = input("Invalid! Time-in HH:MM for {}: ".format(name))
            else:
                time_in = input("Time-in HH:MM for {}: ".format(name))
            time_in = time_in.split(":")
            for str in time_in:
                assert str.isdigit()
            time_in_hour = int(time_in[0])
            time_in_min = int(time_in[1])
            assert (0 <= time_in_hour <= 23 and 0 <= time_in_min <= 59)
            break
        except:
            check_timein = True

    check_timeout = False
    
    while True:
        try:
            if check_timeout:
                time_out = input("Invalid! Time-out HH:MM for {}: ".format(name))
            else:
                time_out = input("Time-out HH:MM for {}: ".format(name))
            time_out = time_out.split(":")
            for str in time_out:
                assert str.isdigit()
            time_out_hour = int(time_out[0])
            time_out_min = int(time_out[1])

            is_later = (time_out_hour == time_in_hour and time_out_min > time_in_min) or (time_out_hour > time_in_hour)

            assert (0 <= time_out_hour <= 23 and 0 <= time_out_min <= 59)
            assert is_later

            break
        except:
            check_timeout = True

    total_min = (time_out_hour - time_in_hour) * 60 + (time_out_min - time_in_min)
    times.append(total_min)
    times_workers.append("{} worked for {} minutes".format(name, total_min))

for string in times_workers:
    print(string)

print("Average number of minutes worked: {}".format(round(sum(times)/len(times), 1)))
