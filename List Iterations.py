#Iterating over lists

L = [10,2,15,20]

for i in range(len(L)):
    print(L[i])

for e in L:
    print(e)

L = [10,2,3,2,12,4]

def has_duplicate1():
    """Return True if the list has duplicate elements"""
    for i in range(len(L)):
        if L[i] in L[(i+1):]:
            return True
    return False

def has_duplicate2():
    """Return True if the list has duplicate elements"""
    sorted_L = sorted(L)
    for i in range(0,len(sorted_L)-1):
        if sorted_L[i] == sorted_L[i+1]:
            return True
    return False



print("a", "b",12,sep = "")

engsci_str = "MAT, ESC, CIV < 3"
engsci_str[2:4]

for letter in engsci_str:
    print(letter)

"abc" + "def"

#replace ESC with PHY
engsci_str[:5] + "PHY" + engsci_str[8:]

"hello".upper()
a = "ESC".lower()

#replace() only replaces every occurance
b = engsci_str.replace("ESC", "PHY")
print(b)




#Storing tables as 2D list

square = [[2,9,4],
          [1,4,3],
          [9,7,8]]

#printing row by row
for i in range(3):
    for j in range(3):
        print(square[i][j])

for i in range(len(square)):
    for j in range(len(square[i])):
        print(square[i][j])

#printing column by column : assuming all rows are of same length
for i in range(len(square[0])):
    for j in range(len(square)):
        print(square[j][i])

