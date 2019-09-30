import datetime
import csv

# d1 = "10/24/2017"
# d2 = "11/24/2016"
# d1 = datetime.date(2016, 11, 24)
# d2 = datetime.date(2017, 10, 24)
# max_date = max(d1,d2)
#
# print(d2 - d1)
#
# today = datetime.date.today()
#
# print(today)

# date_and_time_now = datetime.datetime.now()
# time_now = date_and_time_now.time()
# print(time_now)
data_list = []
data_list_hour_float = []

with open('sample_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    date_hour_format_string = '%Y-%m-%d %H:%M:%S'

    # temp_date_time = '2016-01-01 00:00:09'
    # new_data = datetime.datetime.strptime(temp_date_time,date_hour_format_string)

    for line in csv_reader:
        data_list.append(line)

    for index, data in enumerate(data_list):
        data_list[index][0] = datetime.datetime.strptime(str(data_list[index][0]), date_hour_format_string)
        data_list[index][1] = float(data_list[index][1])

    data_list_hour_float = [(data[0].hour, data[1]) for data in data_list]
    #print(f"data hours:{data_list_hour_float}")

    hour_buckets = {}

    for item in data_list_hour_float:
        if item[0] in hour_buckets:
            hour_buckets[item[0]][0] += 1
            hour_buckets[item[0]][1] += item[1]
        else:
            hour_buckets[item[0]] = [1,item[1]]

    print(f"Calculating average of concerns per 24 hours:")
    for key in hour_buckets:
        print(
            f"Hour(s):{key}, Average:{hour_buckets[key][1] / hour_buckets[key][0]}", )
        #print(f"Hour(s):{str(key - 12) + ' PM' if key > 12 else str(key) + ' AM'}, Average:{hour_buckets[key][1]/hour_buckets[key][0]}" , )

