#1,1,2,3,4,8,13

def fib(n):
    """returs the nth element in the fibonacci series"""
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)


#  1
#   ...                                 1
#     ...                            ...                   ...  }n levels, all full
#      (n-4) (n-3)         (n-3)  (n-2)                     4
#         (n-2)              (n-1)                          2
#              n                                            1


# 1 + a + a^2 + ... + a^q = (a^(q+1)-1)/(a-1)
# We have fewer than 1 + 2 + 4 + 8 + ... 2^n = (2^(n+1)-1)/(2-1) = 2^(n+1)-1
# We have O(2^(n+1)) calls  (same as O(2^n))

#2^(n/2+1) + 2*2^(n/2+1) = 2*sqrt(2)^n

# We have more than 1 + 2 + 4 + ... + 2^(n/2) = (2^(n/2+1)-1)/(2-1) = 2*sqrt(2)^n is O(sqrt(2)^n)


# Define T(n) as the runtime of fib(n)
# T(n) = const + T(n-1) + T(n-2)
# T(n) ~ a*fib(n)
# We can say that the worst-case runtime complexity of fib(n) is O(fib(n))

#sqrt(2) = 1.41
#phi = 1.61
#2 = 2


# Caching
# Storing values that the recursive function computes

# cache: {1:1, 2:1, 3:2, 4:3, 5: 5....}

def fib_cache(n, cache):
    if n in cache:
        return cache[n]

    cache[n] = fib_cache(n-1, cache) + fib_cache(n-2, cache)
    return cache[n]

cache = {1:1, 2:1}
fib_cache(20, cache)

def fib_iter(n):
    fib_prev = 1
    fib_cur = 1

    if n <= 2:
        return 1

    for i in range(3, n + 1):
        fib_prev, fib_cur  = fib_cur, fib_prev + fib_cur
        #fib_prev = fib(i-1)_
        #fib_cur = fib(i)
