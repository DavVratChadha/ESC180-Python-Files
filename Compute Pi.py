import random

N = 1000000
pts_inside = 0
for i in range(N):
    x,y = random.random(), random.random()
    if x**2 + y**2 < 1:
        pts_inside += 1

print(pts_inside/N*4)
#The higher the N, the closer you are to value of Pi
