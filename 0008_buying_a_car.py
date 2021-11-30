def nbMonths(price_old, price_new, saving_permonth, percentloss_bymonth):
    savings, months = 0, 0
    while savings + price_old < price_new:
        savings += saving_permonth
        price_old *= (100 - percentloss_bymonth)/100
        price_new *= (100 - percentloss_bymonth)/100
        if months%2 == 0:
            percentloss_bymonth += 0.5
        months += 1  
    return [months, round(savings + price_old - price_new)]


#Solution for https://www.codewars.com/kata/554a44516729e4d80b000012/