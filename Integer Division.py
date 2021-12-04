#integer division
print(7/2) #3.5 : float division

#// always rounds down
print(7//2) #3 : integer division : greatest integer function
print(7//-2)#-4 : integer division : greatest integer function
print(7%2) # gives remiander = 1
print(7%-2) # gives remiander = -1

7 == -2*(7//-2)+(7%-2)
7 == 2*(7//2) + (7%2)