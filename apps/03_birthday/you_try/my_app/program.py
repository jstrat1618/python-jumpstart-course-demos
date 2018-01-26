import datetime

def print_header():
    print("-------------------------------")
    print("            BIRTHDAY APP")
    print("-------------------------------")


def get_bday_from_user():
    print("When were you born?")
    bday_yr = int(input("Year [YYYY] "))
    bday_mon = int(input("Month [MM] "))
    bday_day = int(input("Day [DD] "))

    bday = datetime.date(bday_yr, bday_mon, bday_day)
    return bday


def compute_days_between_dates(origin_date, target_date):
    this_year = datetime.date(target_date.year, origin_date.month, origin_date.day)
    dt = this_year - target_date
    return dt.days


def print_bday_info(days):
    if days  <0:
        print("You birthday was {} days ago.".format(-days))
    elif days >0:
        print("Your birthday is in {} days.".format(days))
    else:
        print("Your Birthday is today! \n HAPPY BIRTHDAY!!!")



def main():
    print_header()
    bday = get_bday_from_user()
    tdy = datetime.date.today()
    num_days = compute_days_between_dates(bday, tdy)
    print_bday_info(num_days)


if __name__ == '__main__':
    main()