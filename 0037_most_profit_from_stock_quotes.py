def get_most_profit_from_stock_quotes(quotes:list) -> int:
    profit = 0
    for i, quote in enumerate(quotes[:-1]):
        profit += max(0, max(quotes[i+1:]) - quote)  
    return profit


# https://www.codewars.com/kata/597ef546ee48603f7a000057