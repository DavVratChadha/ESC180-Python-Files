for i in range(n):
    for j in range(int(n/2)):
        s += i + j
#runs n^2/2 times
#O(n^2)


#fer,at's theorem
#a^p = b^p + c^p  where a,b,c,p are poritive integers
#no solution for p > 2

def fermat(p):
    n = 1
    while True:
        for i in range(1,n):
            for j in range(1,n):
                for k in range(1,n):
                    if i**p + j**p == k**p:
                        return i,j,k
        n +=1
#runtime complexity of this cannot be dertermined because we dont know about the end. There is no mechanical way to find it. Basically, we assume it runs infinite times untill we find the solution that counters the fermat's thrm



# 98976563457869708
#+98765467890876783
#==================

#runtime complexity of adding large integers: O(n) where n = number of digits in the longer integer
# = O(log(x) + 1) where x = integer

#except of integers, all numerical variables in python are limited in magnitus

#addition, multiplication of floats: can take to be constant


# 98976563457869708
#x98765467890876783
#==================

#O(n^2) where n = number of digits in the larger number
