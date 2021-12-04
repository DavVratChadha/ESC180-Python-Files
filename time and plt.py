#"abababaaaazivhzzzzzzzzziuyuvbnzz", "z"
#"oiytcgvjhaaaaayfashgasaaaaaaaaaasdasd", "a"

def longest_run1(s, c):
    run = 0
    max_run = 0
#inserting an end character different from the target character
    if c == "z":
        s += "y"
    else:
        s += "z"
#line 5 to 11 take a contant amount of time on every run

    for ch in s:
        if ch != c:
            max_run = max(run, max_run)
            run = 0   #t1
        else:
            run += 1  #t2

    return max_run

#in terms of n = len(s), what is worst-case runtime complexity?
#<= n * max(t1, t2) == a8n for some constant a
#overall runtime: b + a*n for some constant a and b
#runtime complexity: 0(n) for n = len(s)





def apply_it(f,arg1):
    return f(arg1)

def g(n):
    return n + 2

apply_it(g,3) #5

import time

t1 = time.time()
t2 = time.time()
print(t2-t1)

def time_it(f, arg1):
    t1 = time.time()
    f(arg1)
    t2 = time.time()
    return t2 - t1

def time_it2(f, arg1, arg2):
    t1 = time.time()
    f(arg1, arg2)
    t2 = time.time()
    return t2 - t1

times = []
s_lengths = []
for s_length in range(10,1000,100): #increase zeros in increment and limit
    s = s_length*"a" + "b"
    c = "a"
    s_lengths.append(s_length)
    times.append(time_it2(longest_run3,s,c))
    #print(times)

import matplotlib.pyplot as plt

plt.plot(s_lengths, times)
plt.show()



s = 10000*"a" + "b"
c = "a"
print(time_it2(longest_run1, s, c))

def longest_run2(s, ch):
    for longest in range(len(s),-1,-1):
        if ch*longest in s:
            return longest

def longest_run3(s, ch):
    #this function has a quadratic relationaship with n = len(s)
    for longest in range(len(s),-1,-1):
        cur_run = 0
        for i in range(len(s)):
            if s[i] == ch:
                cur_run += 1
            else:
                cur_run = 0

        if cur_run == longest:
            return longest

    return 0
    #O(n^2)
