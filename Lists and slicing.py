for i in range(2,15,3):
    print(i)

list(range(2,15,3))

L = [9,8,7,12,14,10,3,2,111,90]

#slicing
L[1:8:2]
#list[start,limit,step] #This returns the element s in the list

#These 2 are same:
L[1:8]
L[1:8:1]

L[1::2] #limit = right end because step is positive
#Start = 1, go till end, in steps of two

L[4::-1]
#Start = 4, go till left end in steps of 1 i.e. it goes in reverse order
#Note: because step is a negative number, it will go to left side from the starting element

L[::-1]
#Here, because there is no start and the step is negative, it returns the list in reverse order with step = 10




#################

def manual_slice(L, i, j, step):
    """Returns the list L[i:j:step],
    without using slicing."""

    res = []
    # [L[i], L[i+step],.....]
    for ind in range(i,j,step):
        res.append(L[ind])

    return res

def manual_slice2(L,i,j,step):
    #This functin is limited to answering some questions and cannot return answer for negative i
    #I.e it cannot return result similar to L[-1:0:-2]
    res = [] #res is empty list
    ind = i
    if step > 0:
        while ind<j:
            res.append(L[ind])
            ind += step
    elif step < 0:
        while ind>j:
            res.append(L[ind])
            ind += step
    return res


if __name__ == "__main__":
    L = [5,6,7,8,9,10,11,12]
    print(manual_slice(L,1,5,2))
    print(manual_slice2(L,1,5,2))
    print(manual_slice2(L,4,0,-2))
    print(L[-1:0:-2])

L = [5,6,10]
M = [2,3]


#List Concatination
L.extend(M)
print(L)
L.extend(M)
print(L)
L.extend([4,5,6,7])
print(L)
L = L + M
print(L)