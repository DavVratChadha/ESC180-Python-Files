#Allowed stuff for Midterm
L = [3,9,2,3]
print(sorted(L))
L.sort()
print(L)


max(a,b)
min(a,b)

print("a", "b", 12, sep = "") #ab12
print("a","b",12) #a b 12

string.lower()
string.upper()

import random
random.random()

L = [5,6,7]
L.extend([1,2,3])
print(L)

#extending list in middle
L = [42, 43, 45]
M = [51, 52]
L[1:1] = M
print(L) #[42, 51, 52, 43, 45]


L = [42, 43, 45]
M = [51, 52]
N = L + M
print(N)

#swaping values
a = 10
b = 5
a,b=b,a
print(a)
print(b)