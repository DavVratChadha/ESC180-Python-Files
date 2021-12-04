L2 = [1,2,3,4,5,6]
def sum_list(L):
    if len(L) == 0:
        return 0
    return L[0] + sum_list(L[1:])
print(sum_list(L2))
#runtime complexity = O(n) where n = len(L)

def sum_list2(L):
    if len(L) == 0:
        return 0
    if len(L) == 1:
        return L[0]

    mid = len(L)//2

    return sum_list(L[:mid]) + sum_list(L[mid:])
print(sum_list2(L2))


# sum_list2([12])   sum_list2([10])                                                ...               #8

#
# sum_lis2t([12, 10])   sum_list2([2, 10])     sum_list2([2, 1, ])    sum_list2([2,  3, 4])          #4

#    sum_list2([12, 10, 2, 10])                    sum_list2([2, 1, 2, 3, 4])                        #2

#                   sum_list([12, 10, 2, 10, 2, 1, 2, 3, 4])
#1

#runtime complexity = O(2^log2(n)) = O(n) where n = len(L)

