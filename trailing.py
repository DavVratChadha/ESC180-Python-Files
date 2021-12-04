#compute the number of trailing zeros in n! (factorial

def fact (n):
    """Function to calculate factorial"""
    res = 1
    for i in range(n+1):
        res *= i
    return res

def zero_counter(n):
    """trailing zero counter"""
    fact_n = str(fact(n))
    num = 0
    length = len(fact_n)
    flag = True
    i = 0
    while i < length:
        if fact_n[-1] == "0":
            num += 1
            fact_n = fact_n[length-1]
            i += 1
        else:
            flag = False
    return num

def zero_counter2(n):
    fact_n = fact(n)

    counter = 0

    while fact_n%10 == 0:
        fact_n //= 10
        counter += 1
    return counter

print("This is outside the if __name__ == __main__ block!")

if __name__ == "__main__":
    print(zero_counter(5))
    print(zero_counter2(5))