def main():

    daily_balances = [107.92, 108.67, 109.86, 110.15]

    """
    Should equal:
      "slice starting 3 days ago: [108.67, 109.86]"
      "slice starting 2 days ago: [109.86, 110.15]"
    """
    show_balances(daily_balances)

def show_balances(daily_balances):

    day = len(daily_balances)
    end = len(daily_balances)
    start_day = 3
    slice_end = 2

        # do not include -1 because that slice will only have 1 balance, yesterday
    for slice_start, bal in enumerate(daily_balances):
        balance_slice = daily_balances[slice_start: slice_end]

        if day <= start_day and slice_end <= end:
            print("slice starting %d days ago: %s" % (day, balance_slice))
        day -= 1
        slice_end += 1


if __name__ == '__main__':
    main()
