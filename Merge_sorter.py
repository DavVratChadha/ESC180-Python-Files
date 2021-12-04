#[10,2,3,11,21,43,20,30,1]


[1,5,7]
[2,4,10]

#1 2 4 5 7 10

def merge(L1, L2):
    """Return sorted version of L1 + L2
    L1, L2 are sorted lists of ints"""
    #return sorted(L1 + L2)
    i1 = 0 #location in L1
    i2 = 0 #location in L2
    res = []

    while i1 < len(L1) and i2 < len(L2):
        if L1[i1] < L2[i2]:
            res.append(L1[i1])
            i1 += 1
        else:
            res.append(L2[i2])
            i2 += 1

    res.extend(L1[i1:])
    res.extend(L2[i2:])
    return res
    #merge appends len(L1) + len(L2) elems to res
    #so runs in len(L1) + len(L2) iterations
    #complexity = O(len(L1) + len(L2)) = O(n) = k*n seconds per call

def merge_sort(L):
    if len(L)  <= 1:
        return L[:]

    mid = len(L) // 2
    sorted_half1 = merge_sort(L[:mid])
    sorted_half2 = merge_sort(L[mid:])
    return merge(sorted_half1, sorted_half2)  #k * len(L) seconds

print(merge_sort([10,2,3,11,21,43,20,30,1]))


#1  1  1  1   1    1   1  1 1  1 1  1 1 1       n*k*(n/n)
#.     ..     ..     .  .     .                  .
# .   .  .   .  .   .    .   .                   .
#  n/4    n/4    n/4      n/4                   4*k*(n/4)
#      n/2           n/2                        2*k*(n/2)
#              n                                k*n  seconds

#total runtime = k*n * number of levels
#              = k*n*log2(n)
#runtime complexity = O(nlog(n))


#total calls = 1 + 2 + 4 + ...... + n
#            = 2^0 + 2^1 + 2^2 + ...... 2^log2(n_
#            = (2^log2(n) +1 - 1)/(2-1)
#            = n calls





############


#what if mid = 1
def merge_sort2(L):
    if len(L)  <= 1:
        return L[:]

    mid = 1
    sorted_half1 = merge_sort(L[:mid])
    sorted_half2 = merge_sort(L[mid:])
    return merge(sorted_half1, sorted_half2)  #k * len(L) seconds

print(merge_sort([10,2,3,11,21,43,20,30,1]))


#call tree:

#                   [1]         k*(1)
#...
#       [1]    [n-3]            k*(n-3)
#   [1]    [n-2]                k*(n-2)
#[1]  [n-1]                     k*(n-1)
#   [n]                         k*(n)


