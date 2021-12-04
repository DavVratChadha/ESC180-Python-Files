def f():
    a = 5#this a local variable a
    print(a)
    print(globals()["a"])#this is a special command to access global
    #note: using 'global a' will give an error coz a local one has been declared already

if __name__ == '__main__':
    a = 10
    f()