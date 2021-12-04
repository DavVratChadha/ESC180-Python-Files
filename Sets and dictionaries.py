s1 = {131,12,23,4}
print(s1)
s2 = {"hi", 5}

for e in s1:
    print(e)

L1 = list(s1)

L = [4,2,4,5,6]
print(set(L)) #a set cannot have duplicate elements
#all elements in a set are arranged into a list by default
L2 = list(set(L))
print(L2)


a = {1,2,3}
a.update({0})
print(a)
#frozenset
b = frozenset(a)
print(b)
#b.update({10})#should return an error because u cannot update a frozenset
#print(b)

#getting nth elem of a set
print(list(b)[0])


def manual_get(d,k,default):
    """return value corresponding to key k in dictionary d"""
    if k in d:
        return d[k]
    else:
        return default

d = {1:2,3:4}
to_add = {5:6,7:8}
d.update(to_add)

to_add = {1:3}
d.update(to_add)

def manual_update(d,to_add):
    for k, v in to_add.items():
        d[k] = v


