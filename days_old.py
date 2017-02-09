# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days.
# Account for leap days.
#
# Assume that the birthday and current date are correct dates (and no
# time travel).
#


def days_of_month(month, year):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    if month != 2:
        return 30
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return 29
    return 28


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    day = day1
    month = month1
    year = year1
    days = 0
    daysOfMonth=days_of_month(month, year)
    while True:
        if day == day2 and month == month2 and year == year2:
            break
        days = days + 1
        day = day + 1
        if day > daysOfMonth:
            day = 1
            month = month + 1
            daysOfMonth=days_of_month(month, year)
        if month > 12:
            year = year + 1
            month = 1
            daysOfMonth=days_of_month(month, year)
    return days


# Test routine
def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed", result
        else:
            print "Test case passed!"

test()
