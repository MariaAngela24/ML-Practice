stock_prices_yesterday = [12, 10, 9, 8, 12, 17, 4]
def get_max_profit(stock_prices_yesterday):

    min_price = stock_prices_yesterday[0]
    max_profit = 0

    for current_price in stock_prices_yesterday:

        # ensure min_price is the lowest price we've seen so far
        min_price = min(min_price, current_price)
        print "min_price = ", min_price

        # see what our profit would be if we bought at the
        # min price and sold at the current price
        potential_profit = current_price - min_price
        print "potential_profit =", potential_profit

        # update max_profit if we can do better
        max_profit = max(max_profit, potential_profit)
        print "max_profit =", max_profit

    print max_profit

get_max_profit(stock_prices_yesterday)


