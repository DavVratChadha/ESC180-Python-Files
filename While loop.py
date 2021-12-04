#While loop
#while<cond>:
#   <block>

#log10(n)
#n = 1000
#log10(1000) = 3

#1000
#divide by 10
#100
#divide by 10
#10
#divide by 10
#1

def my_log10(n):
    """Return log to base 10
    Note: It does not return the perfect answer because it is a rough model of a function"""
    res = 1
    i = 0
    while res<n:
        res *= 10
        i +=1

    return i

print(my_log10(0))

start = 5
end = 17
step = 2

i = start
while i<end:
    print(i)
    i += step