L = [5,10,2,-1,50]
#selection sort (max sort)
#at iteration i, find maximum elem in L[:(n-i)] and put it at the
#location L[n-i-1]

#L = [5,10,2,-1,50]
#iteration at 0:
#50 is largest element so put it at L[n-1-0]
#L = [5,10,2,-1,50]

#iteration at 1:
#10 is largest element so put it at L[n-1-0]
#L = [5,2,-1,10,50]
#.....
#L = [-1,2,5,10,50]

def max_i(L):
    """Return the index of the largest elem in L"""
    curr_max = L[0]
    curr_max_i = 0

    for i in range(1,len(L)):
        if L[i] > curr_max:
            curr_max = L[i]
            curr_max_i = i

    return curr_max_i

def selection_sort(L):
    for j in range(len(L)):
        ind_of_max = max_i(L[:(len(L)-j)])
        L[ind_of_max],L[len(L) - j - 1] = L[len(L) - j - 1],L[ind_of_max]
#runtime complexity = O(n^2)

L1 = [2,3456,12345,1,-5,0,1000000]
selection_sort(L1)
print(L1)




#Bucket sort / counting sort
L = [1,20,1,0,0,50]

#0:2
#1:2
#20:2
#50:1
#ans = [0,0,1,1,20,50]

def counting_sort(L):
    max_L = max(L)                  #k1 * n
    counts = [0] * (max_L + 1)      #k2 * (max(L) + 1)
    for e in L:                     #k3 * n
        counts[e] += 1

    res = []
    for elem in range(len(counts)):
        count = counts[elem]
        if count > 0:
            res.extend([elem] *count)
    #    print(elem,res)
                                    #k4 * max(L)
    print(res)

counting_sort(L)
#total = (k1 + k3) * n + (k2 + k4) * max(L) + k2
#runtime complexity = O(n + m)   #n = len(L) and m = max(L)


########
#Bozosort
#Swap 2 random elems and see if list is sorted
#L = [5,2,1,2,10,1]

import random
def is_sorted_nondecreasing(L):
    '''Return True iff L is sorted in non-decreasing order'''

    # return L == sorted(L)
    for i in range(len(L) - 1):
        if L[i] > L[i+1]:
            return False
    return True

def bozosort(L):
    while not is_sorted_nondecreasing(L):
        i, j = int(len(L)*random.random()), int(len(L)*random.random())
        L[i], L[j] = L[j], L[i]


L = [10, 2, 20, 25, 2, 10, 50, 10, -2, 100, 50, 20]
bozosort(L)
print(L)

#we expect to go through each permutation of teh list atleast once
#therefore, runtime complexity  = O(n!)







