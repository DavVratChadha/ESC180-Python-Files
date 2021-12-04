#datatypes
name = "Adam" #string
age = 17 #int
footSize = 10.5 #float

#float are limited in magnitude/size, but can store fractions
c = 4.2e8000 #4.2 X 10^8000 (infinity)
d = 5.2e-1000  #5.2 X 10^-1000 (zero)

#int are unlimited in size
f = 234567890876543245678654324567876543213456786543245678

#to check the largest and smallest float in the system without going to infinity,
import sys
sys.float_info.max
sys.float_info.min

#converting float to string
rating = 7.9
phrase = str(rating)

#converting string to float
value = "8.2"
rating2 = float(value)

#converting float to integer
int(5.2) #this will give 5
int(5.9) #this will also give 5 coz int() truncates ate the decimal

#to round a float
round(5.9) #this will give 6.0
round(5.1678697678547563786970878654) #this will give 5.0
#to round this to 3 sig digits,
round(5.1678697678547563786970878654*100/100)
#to round 3 digits after the decimal,
round(5.1678697678547563786970878654, 3)

#note
int("5.2") #does not work because "5.2" is a string
#to make it work,
int(float("5.2"))