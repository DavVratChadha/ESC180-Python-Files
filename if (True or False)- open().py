#True or False: True
#True and False: False
#True and not False: True
#not True and False: False





lazy = False
smart = True
growthmindset = False

if not lazy and smart and growthmindset:
    print("EngSci")
elif lazy and smart:
    print("Phyisics")
elif not lazy and smart and not growthmindset:
    print("Economics")
else:
    print("Ryerson")



def has_no_roots(a,b,c):
    disc = b**2 - 4*a*c
    return not (disc>=0) #it returns false if if the function fas roots


#convert int to bool : anything tha is not zero is returned as true
bool(0)
bool(1)
bool(5)
bool(1.2)

bool("EngSci is better that Track One")


a = "abc"
if a:
    print ("It is True")


def artsie_math(arg1,arg2,op):
    """This function adds or sobtracts the two aruments given based upon the mathematical operator"""
    if op == "add":
        return arg1 + arg2
    if op == "subtract":
        return arg1 - arg2
    print("I don't recognize this complicated mathematical operation")


def artsie_math2(arg1,arg2,op): #another way to write previous function
    """This function adds or sobtracts the two aruments given based upon the mathematical operator"""
    if op != "add" and op != "subtract":
        print("I don't recognize this complicated mathematical operation")
        return #returns None
    if op == "add":
        return arg1 + arg2
    if op == "subtract":
        return arg1 - arg2


def f():
    1+2 #because this value is not being returned, the function will return special value None answer if the f() is printed

def g():
    return 1+2

if __name__ == '__main__':
    print(artsie_math(2,3,"add"))
    print(artsie_math(2,3,"multiply")) #this will return a special value None as the answer because multipy operator does not exist in the artsie_math funtion and the funtion does not return anything for mutilpy
    print(artsie_math(2,3,"add"))
    print(artsie_math(2,3,"multiply"))
    res = artsie_math(2,4,"exponent")
    if res != None:
        print(res, " from res")

    print(f(), "from f()")#returns none
    print(g(), "from g()")#returns 3


