# python project
# okay so i'm doing a project called Date validation \ date detection

import re, pyperclip


date_regex = re.compile(r"\d{2}[/-]\d{2}[/-]\d{4}")
text = str(pyperclip.paste())
mo = date_regex.findall(text)
catch_correct_date = []
for v_date in mo:
    if (
        int(v_date[:2]) > 31
        or int(v_date[3:5]) > 12
        or int(v_date[6:]) < 1999
        or int(v_date[6:]) > 2999
    ):
        print(f"invalid date {v_date}")
    elif v_date[3:5] in ["04", "06", "09", "11"] and int(v_date[:2]) == 31:
        print(f"this month {v_date} have 30 days")
    elif (
        int(v_date[3:5]) == 2
        and int(v_date[6:]) % 4 == 0
        and (int(v_date[6:]) % 100 != 0 or int(v_date[6:]) % 400 == 0)
    ):
        leap_date = int(v_date[:2]) + 1
        print(f"Today is leap year February date should be {leap_date}")
    elif v_date[3:5] in "02" and int(v_date[:2]) > 29:
        print(f"this month {v_date} have 29 days")
    else:
        the_perfect_dates = v_date
        print(f"\n** {the_perfect_dates} **")
        catch_correct_date.append(the_perfect_dates)

if len(catch_correct_date) > 0:
    pyperclip.copy("\n".join(catch_correct_date))
    print("copied")
else:
    print("Fisrt Copy some dates bro")
