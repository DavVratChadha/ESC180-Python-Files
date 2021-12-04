#for loops in python

for i in range(5):
    print(i) #print from 0 to 4 (both included)
print("******************8")

for i in range(5):
    print(i)
    print(2*i)
    print("==================")

for i in range(5):
    print("I like PHY180 tests!")#prints 5 time

for i in range(5):
    print("I am telling you for the " + str(i) + "th time that I like PHY180 tests!")

#compute a^b
# = a*a*a*a*a....
#a is multiplied by itself (b-1) times
# or
# = 1*a*a*a*a...
#1 is multiplied by a, b times
result = 1
for i in range(b):
    result *= a

def my_pow(a,b)
"""Returns a^b
    a: a positive number
    b: a non-negative number"""
    res = a
    for i in range(b-1):
        res *= a
    return res

def my_pow2(a,b)
"""Returns a^b
    a: a positive number
    b: a non-negative number"""
    res = 1
    for i in range(b):
        res *= a
    return res

#for i in range(start,limit,step)
for i in range(1,10,2):
    print(i)

for i in range(1,10): #Note: if the step is not specified, the step is +1
    print(i)


def is_prime(n):
    """returns True iff n is prime
    n -- a non-negative integer"""

    if n <= 1:
        return False

    if n == 2:
        return True

    for i in range (n-2):
        #i = 0,1,2,3....(n-3)
        #(i+2) = 2,3,4,5....(n-1)
        if n%(i+2) == 0
            return False

    return True

def is_prime2(n):
    """returns True iff n is prime
    n -- a non-negative integer"""

    if n <= 1:
        return False

    if n == 2:
        return True

    for i in range (2,n):
        # if n%i == 0:
        #   return False
        #else:
        #   return True
        #This code in comment above is equivalent to the code below (line 88 to 93)
        if n%i != 0:
            pass
        else:
            return False

    return True
