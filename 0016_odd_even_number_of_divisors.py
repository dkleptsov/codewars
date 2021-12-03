def oddity(n: int) -> str:
    divisors = [1]
    for i in range(2,int((n)**(1/2))+1):
        if n%i == 0:
            divisors.extend([i,n/i])
    divisors.extend([n])
    return "odd" if len(set(divisors))%2 else "even"


# https://www.codewars.com/kata/55830eec3e6b6c44ff000040/