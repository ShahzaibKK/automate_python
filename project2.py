import random

number_streaks = 0
th = []
newlist = []
for i in range(10):
    while len(th) != 100:
        th.append(random.choice("HT"))
    for j in range(6):
        if th[j] == th[j - 1]:
            newlist.append(th[j])
            # number_streaks += 1

print(len(th), end="")
print("check")
