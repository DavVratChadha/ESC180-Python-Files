# Program to multiply two matrices using nested loops

# 3x3 matrix
M = [[1,0],
    [2,0]]

N = [[1,0],
    [0,1]]
# result is 3x4
result = [[0,0],
         [0,0]]

# iterate through rows of X
for a in range(len(M)):
   # iterate through columns of Y
   for d in range(len(N[0])):
       # iterate through rows of Y
       for index in range(len(N)):
           result[a][d] += M[a][index] * N[index][d]

for r in result:
   print(r)