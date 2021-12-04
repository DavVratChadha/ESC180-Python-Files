
def n_as_plus_b(s):
    """Return the maximum number of "a"s followed by a "b" in the string s"""
    for length in range(len(s),-1,-1):
        if "a" * length + "b" in s:
            return length

s = "aaabxfsaabaghgbxyaaaab"
print(n_as_plus_b(s))


def n_as_plus_b2(s):
    """Return the maximum number of "a"s followed by a "b" in the string s"""
    curr_run = 0 #number of "a"s in current run
    curr_max_run = -1 #the max number run of"a"s in an aaa....aaab sequence

    for i in range(len(s)):
        if s[i] == "b":
            curr_max_run = max(curr_max_run, curr_run)
            curr_run = 0
        elif s[i] == "a":
            curr_run += 1
        else:
            curr_run = 0
    if curr_max_run > 0:
        return curr_max_run
    else:
        return 0

s = "aaabxfsaabaghgbxyaaaab"
t = "aaaaaaaaaa"
print(n_as_plus_b2(s))
print(n_as_plus_b2(t))

##########
alpha = "abcdefghi"

#all passwords length 3

for c1 in alpha:
    for c2 in alpha:
        for c3 in alpha:
            print(c1 + c2 + c3)


code = """
b = a + 10
print(b)
"""
#to execute this string as code,
exec(code) #15

code2 = """
def f():
    return 5
    """
exec(code2)
print(f())

s = "I got {} on the calc midterm".format(12)

code3 = """
def g():
    return {}""".format(12)


#all passwords length upto N i.e. not including N

alpha = "abcdefghi"
def password_gen(N):
    code = ""
    for i in range(1, N):
        code += "for c{} in alpha:\n".format(i)
        code += "   " * (i + 1)

    code += "print("
    for i in range(1, N - 1):
        code += "c{}".format(i) + " + "
    code += "c{}".format(N - 1) + ")"
    print(code)
    exec(code)
    return

password_gen(4)