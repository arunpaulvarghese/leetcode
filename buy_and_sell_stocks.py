# Program to demonstrate a simple stock market price analysis
def stockPrice(prices):
    profit = 0
    buy = prices[0]

    for sell in prices[1:]:
        if sell > buy:
            profit = max(profit, sell - buy)
        else:
            buy = sell
    return profit



pri = [3,5,2,6,3,1,10]
print(stockPrice(pri))
