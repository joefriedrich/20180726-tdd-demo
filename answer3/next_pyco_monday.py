import datetime
import sys
import getopt

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def next_leap_year(start_year):
    year = start_year
    while not is_leap_year(year):
        year += 1
    return year

def feb_29_is_monday(year):
    d = datetime.date(year, 2, 29)
    if d.weekday() == 0:
        return True
    else:
        return False

def next_pyco_leapyear_monday(start_year):
    year = next_leap_year(start_year)
    while not feb_29_is_monday(year):
        year = next_leap_year(year + 1)
    return year

def get_start_year_from_arguments():
    #---Start command line options logic---
    try:
        opts, args = getopt.getopt(
            args[1:],
            "hy:o:",
            ["start-year="])
    except getopt.GetoptError:
        print 'python next_pyco_monday.py -y <start_year>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'python next_pyco_monday.py -y <start_year>'
            sys.exit()
        elif opt in ("-y", "--start-year"):
            start_year = int(arg)
    if not start_year:
        print 'python next_pyco_monday.py -y <start_year>'
        sys.exit(2)
    #---End command line options logic---
    return start_year

def main(args):
    year = get_start_year_from_arguments()

    print 'Starting is %d' % year
    print (("Next year with a Central Ohio Python User Group meetup "
        "on a leapyear end of February: %d") %
        next_pyco_leapyear_monday(year))

if __name__ == "__main__":
    main(sys.argv)
