import time, threading

print("start the Program")


def take_nap():
    time.sleep(5)
    print("wake up to realiality")


thread_obj = threading.Thread(target=take_nap)
thread_obj.start()
print("Program has been ended!")
