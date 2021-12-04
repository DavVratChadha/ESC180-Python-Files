def power(x,n):
    """return x^n"""
    res = 1
    for i in range(n):
        res *= x
    return res

def power_rec(x,n):
    #base case
    if n == 0:
        return 1
    return x*power_rec(x,n-1)


def power_rec2(x,n):
    if n == 0:
        return 1
    if n == 1:
        return x

    half_power = power_rec2(x, n//2)

    if n%2 == 0:
        return half_power*half_power
    else:
        return half_power*half_power*x
    return x*power_rec(x,n-1)

#runtime complexity = O(log2(n)) = O(log(n))
#O(nlogn)
#def run(n)
# k = n*log(n)
