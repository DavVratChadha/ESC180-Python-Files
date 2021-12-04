# alphabet = "abcdef"
# for c1 in alphabet:
#     for c2 in alphabet:
#         ......

#print all strings of length n over alphabet alphabet

def print_all(alphabet,n,start_str = ""):
    if n == 0:
        print(start_str)
        return
    for letter in alphabet:
        print_all(alphabet,n-1,start_str + letter)

print_all("abc",3)
#runtime complexity = O(k^n) where k = number of alphabets in the dictionary

def all_combs(alphabet,n,start_str = ""):

    if n == 0:
        return [start_str]

    res = []
    for letter in alphabet:
        res.extend(all_combs(alphabet,n-1,start_str + letter))

    return res
print(all_combs("abc",3))
print(all_combs("abc",1))
