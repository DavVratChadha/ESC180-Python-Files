def fact_white(n):
    cur_prod = 1 #current product = (i-1)!
    i = 1

    while i != n+1:
        cur_prod *= i
        i += 1
        #invariant: cur_prod = (i-1)!

    #i = n+1
    #cur_prod = (i-1)! = n!
    return cur_prod

def f(a = 2,b = 3):
    return a + b

def fact_iter(n, cur_prod = 1, i = 1):
    """Return n! arguments:
    n -- an integer
    cur_prod = (i-1)!
    """
    #base case
    if i == n+1:
        return cur_prod

    #recursive step
    return fact_iter(n,cur_prod*i, i+1)

def fact_rec(n):
    if n == 0:
        return 1
    return n * fact_rec(n-1)
