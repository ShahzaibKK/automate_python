import subprocess, webbrowser

# the_notepade = subprocess.Popen("notepad.exe")
# the_notepade.wait()
# print("program is closed")

kk = subprocess.Popen(["notepad.exe", r"C:\Users\shahz\mylog.log"], shell=True)
kk.wait()
