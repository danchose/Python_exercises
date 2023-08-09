def invest(amount, rate, time):
    amount = int(amount)
    rate = float(rate)
    time = int(time)
    print("principal amount: $", amount)
    print("annual rate of return:",rate)
    for time in range(1, time+1):
        amount = amount*(1+rate)
        print("Year {}: $ {}".format(time, amount))

invest(100, .05, 8)
invest(2000, .025, 5)