#Alias ???
#lists are mutable
#variables are immutable
#shallow and deep copy


##########
#shallow copy
L1 = [[1,2],[3,4]]
L2 = []
for e in L1:
    L2.append(e) #Same as L2 = L1.copy()
                  # or L2 = L1[:]
                  #[:] is shorthand for calling all elements of list
                  #ie [:] means everything in the list
print(L2)
L2[0][1] = 5
print(L2)
print(L1)
#L2 is not alias of L1. Rather, elements of L2 arre aliasis of elements of L1
#This is known as shallow copy
#changing elemenets of L2's sub-lists change the corressponding elements of L1, ie it has effect on L1

#########
L1 = [[1,2],[3,4]]
L2 = []
for e in L1:
    L2.append(e)
print(L2)
L2[1] = 2 #this does not have any affect on L1
print(L2)
print(L1)

#############3
#manual deep copy
L1 = [[1,2],[3,4]]
L2 = []
for e in L1:
    elem_list = []
    for i in e:
        elem_list.append(i)
    L2.append(elem_list)

print(L2)
L2[0][1] = 5
print(L2)
print(L1)
#This would create a completely fresh list L2 changing whose elemenets of sub-lists would have no effect on L1
#this is known as deep copy

#shorthand version of deep copy
L1 = [[1,2],[3,4]]
L2 = []
for sublist in L1:
    L2.append(sublist[:])

print(L2)
L2[0][1] = 5
print(L2)
print(L1)


##############
a = 5
b = a
b = 4
print(a) #5

#######
c = 1
d = c
c = 3
print(d) #1