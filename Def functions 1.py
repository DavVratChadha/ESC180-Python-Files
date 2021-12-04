def pirate_print(s):
    """Print the pirated version of s"""
    print("Ahoy! " + s + " Yarr.")
    #note: we do not need a return statement here coz return statement is to return values, and a blank retun statement makes no difference.

def pirate_transform(input_s):
    """Return the pirated version of s"""
    piratified_s = "Ahoy! " + input_s + " Yarr."
    return piratified_s

def f(x):
    return x**2

if __name__ == '__main__':
    pirate_print("I love Calculus")
    pirate_print("Praxis too!")
    pirate_transform("ESC180 too!!!")#this wouldnt print anything coz the function returns answer and not prints it
    f(20)
    ten_squad = f(10)
    print(ten_squad)











    "Ahoy"
    5 #note these two didnt do anything or give any error because python says that these are just string and int respectively and python has npthing to do with them