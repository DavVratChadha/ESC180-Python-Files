def has_roots(a,b,c):
    disc = b**2 - 4*a*c
    return disc > 0 #this will return true or false


def adjust_grade():
    global grade
    grade = grade - 5
    print("New grade inside the function:", grade)

def adjust_grade2(grade):
    #global grade #note: this line would give an error because grade is alreadya parameter and can no longer be declared as a global variable
    #You cannot have a parameter declared as global variable in the same function
    grade = grade - 5
    print("New grade inside the function:", grade)

def adjust_grade3(g):
    g = g-5
    print("New grade inside the function is: ", g)

def adjust_grade4(g):
    global grade
    g = g-5

def get_adjusted_grade(grade):
    return grade - 5 #New value returned. Note: This will not change the value of grade here coz it is not being stored

if __name__ == "__main__":
    print(has_roots(2,3,4))

    grade = 95
    adjust_grade()
    print("New grade outside the funtion: ", grade)#The value of grade inside and outside the function is same because grade has been declared global inside the function

    adjust_grade2(grade)
    print("New grade outside the funtion: ", grade)#The value of the grade inside and outside the functionis different because grade has not been declared global inside the function. Istead, it has gone in as a parameter, and has not been returned

    grade = 95
    adjust_grade3(grade)
    print("New grade outside the function is: ", grade)

    grade = 95
    adjust_grade4(grade)
    print("New grade outside the function is: ", grade)

    grade = 95
    grade = get_adjusted_grade(grade) #Here grade value will be changed coz a different value is coming from a funtion and is being stored
    print("New grade outside the function is: ", grade)





#Note: Use Debug step into to debug def functions by getting into them via the command that calls them