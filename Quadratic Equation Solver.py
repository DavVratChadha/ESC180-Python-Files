#Quadratic equation solver

#5**2 = 25
"""#To find square root of a number,
import math
math.sqrt(25) #=5"""

import math
#ax^2 + bx + c = 0
#x = (-b +/- sqrt(b^2 - 4ac))/2a

a = 2
b = -20
c = 1
#discriminant
disc = b**2 - 4*a*c

if disc>0:
    r1 = (-b + math.sqrt(disc))/(2*a)
    r2 = (-b - math.sqrt(disc))/(2*a)
    print("The two real roots are = " + str(r1) + " and " + str(r2))

elif disc ==0:
    r1 = (-b + math.sqrt(disc))/(2*a)
    print("The only real roots is = " + str(r1))

else:
    print("No real roots exist!")

print(2*r1**2 - 20*r1 + 1) #note this is not zero because the zeros are calculated in float
print(2*r2**2 - 20*r2 + 1)
