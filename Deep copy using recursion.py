L1 = [[1,2],[3,4]]
L2 = L1[:]
copy = []
for e in L1:
    copy.append(e[:])


L1 = [1,2],[3,[4,5]]
L2 = L1[:]
copy = []
for e in L1:
    copy.append(e[:])

def deep_copy(obj):
    #base case
    if type(object) != list:
        return obj

    #recursive step: object is a list
    copy = []
    for elem in obj:
        copy.append(deep_copy(elem))
    return copy

print(deep_copy(L1))