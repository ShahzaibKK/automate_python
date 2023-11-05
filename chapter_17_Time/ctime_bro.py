import time, datetime

current_time = time.time()

human_time = time.ctime(current_time)
print(human_time)


print(datetime.datetime.now().year)
print(datetime.datetime.fromtimestamp(current_time))

mr_birth_date = datetime.timedelta(days=256)
print(mr_birth_date.total_seconds())
print(str(mr_birth_date))
