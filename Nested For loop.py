#neumeration?


alphabet = ["a","b","c","d","e"]

for x1 in alphabet:
    for x2 in alphabet:
        for x3 in alphabet:
            print(x1, x2, x3, sep = "")
            #note: sep = "" removes the default separation of print in this style
print(x1, x2, x3) #his has 1 space betwwen characters

def missing_k(L):
    """Returns missing value in an integer list"""
    n = len(L) + 1
    for k in range(1,n+1):
        if k not in L:
            return k

L = [1,5,3,2,4,7]
print(missing_k(L))

#Infinite for loop by altering the list itself
for i in L:
    L.append(i)