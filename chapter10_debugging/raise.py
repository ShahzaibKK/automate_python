import traceback

try:
    raise Exception("Fuck Bro")
except:
    with open("traceback.txt", "w") as error_file:
        error_file.write(traceback.format_exc())
        print(f"The Error Message in traceback.txt")
