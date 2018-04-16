def recurringTask(firstDate, k, daysOfTheWeek, n):

    # month_lengths = {"01": 31, "02": 28, "03": 31, "04": 30,
    #                  "05": 31, "06": 30, "07": 31, "08": 31,
    #                  "09": 30, "10": 31, "11": 30, "12": 31}
    # first we need to know the day of the week that is the start date
    # we get that by calculating the days from the origin date, then mod by 7

    ######################################################################

    def is_leap(year):
        return ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))

    def calculate_full_years(year):

        # should return -365 for any date in 2014
        # should return 0 for any date in 2015
        # should return 366 for any date in 2016
        # should return 731 for the year 2017

        origin = 2015
        date_year = year
        if year - origin == 0:
            return 0

        count_leap_years = 0
        while year != origin:

            if year > origin:
                if is_leap(year):
                    count_leap_years += 1
                year -= 1
            elif year < origin:
                if is_leap(year):
                    count_leap_years += -1
                year += 1

        return (365 * (date_year - origin)) + count_leap_years

    def calc_partial_year(firstDate, month_lengths_arr):
        """Returns the number of days that have passed in the current year.

        For a firstDate of Jan 1 it should return 0.
        For a firstDate of Jan 21 it should return 20.
        For a firstDate of Dec 31 it should return 364 (if not a leap year)
        For a firstDate of Dec 31 in a leap year, it should return 365.
        For a firstDate of Feb 29, it should return 28.
        """
        date, month, year = map(int, firstDate.split("/"))

        days_into_year = date - 1
            # accounts for the fact that today is not completed

        for i in xrange(0, month - 1):
            # excludes the current month; -1 accounts for zero indexing
            days_into_year += month_lengths_arr[i]

        if month > 2:
            # we do not need to check for the 29th here, because date takes care of it
            if is_leap(year):
                days_into_year += 1

        return days_into_year


    ################## MAIN FUNCTION #####################

    month_lengths_arr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day_codes = {0: "Thursday", 1: "Friday", 2: "Saturday", 3: "Sunday",
                 4: "Monday", 5: "Tuesday", 6: "Wednesday"}
    rev_day_codes = {"Thursday": 0, "Friday": 1, "Saturday": 2, "Sunday": 3,
                     "Monday": 4, "Tuesday": 5, "Wednesday": 6}

    date, month, year = map(int, firstDate.split("/"))

    days_into_year = calc_partial_year(firstDate, month_lengths_arr)
        # always positive, because going "forward" in time

    completed_years = calculate_full_years(year)
        # negative if going backward in time

    days_from_jan1_2015 = days_into_year + completed_years

    firstDate_code = days_from_jan1_2015 % 7
        # gives the day of the week code

    origin_dotw = day_codes.get(firstDate_code)
        # A string, like "Tuesday"

    begin_index = daysOfTheWeek.index(origin_dotw)
        # gets the index of that value in the days of the week list (guaranteed to be there)

    dotw_str_arr = daysOfTheWeek[begin_index:]
    second_slice = daysOfTheWeek[:begin_index]
    dotw_str_arr.extend(second_slice)
        # rearranges slices of daysOfTheWeek into the chron order

    dotw_codes_arr = []
        # will have the codes for the days of the week in the right order, no repeats

    for day_string in dotw_str_arr:
        day_code = rev_day_codes.get(day_string)
        dotw_codes_arr.append(day_code)

    date_pieces = []
    days_in_month = month_lengths_arr[(month - 1)]
    print date, month, year
    print days_in_month

    deltas = []
    results = [firstDate]

    # make a list of all the differences between the days, which will be used to make the dates
    # making it will be complicated by the skipping of weeks, k

    # while len(deltas) < (n - 1):  # is this the right limiter???

    #     if len(dotw_codes_arr) == 1:  # at least weekly
    #         delta = k * 7
    #         deltas.append(delta)

    #     else:
    #         for i in xrange(1, len(dotw_codes_arr)):
    #             if dotw_codes_arr[i] < dotw_codes_arr[i - 1]:
    #                 dotw_codes_arr[i] += 7
    #             delta = dotw_codes_arr[i] - dotw_codes_arr[i - 1]

    #             if len(deltas) % len(dotw_codes_arr)



    #             deltas.append(delta)



if __name__ == "__main__":
    recurringTask("01/01/2015", 2, ["Monday", "Thursday"], 4)  #Thurs
    print "***"
    recurringTask("31/12/2014", 2, ["Wednesday", "Thursday"], 4)  #Wed
    print "***"
    recurringTask("30/08/2000", 2, ["Monday", "Wednesday"], 4)  #Wed
    print "***"
    recurringTask("30/08/2500", 2, ["Monday", "Friday"], 4)  #Mon
    print "***"
