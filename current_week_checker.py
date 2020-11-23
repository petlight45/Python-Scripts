from datetime import date
import math

def suffix_derive(week):
    dic_suffix = {
        "1": "st",
        "2": "nd",
        "3": "rd",
    }
    try:
        if str(week)[-2] == "1":
            return "th"
    except:
        pass
    if int(str(week)[-1]) > 3:
        return "th"
    else:
        return dic_suffix[str(week)[-1]]

def checker(start, stop):
    days_offset = (stop-start).days
    weeks = math.trunc(days_offset/7)
    days = days_offset - (weeks*7)
    current_week = "{}{} Week".format(weeks+1, suffix_derive(weeks+1))
    return weeks,days,current_week

start_date = date(2020, 1,1)
stop_date = date.today()
response = checker(start_date,stop_date)
print(response[-1], "{} Week(s)".format(response[0]), "{} Day(s)".format(response[1]), sep="\n")

