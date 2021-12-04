N = 10000000

count = 0  #count will store the number of random points
           #that fell within the unit circle

for i in range(N):
    x, y = random.random(), random.random()
    if x**2 + y**2 < 1: #sqrt(1-x**2) < y

        count += 1

print(4.0*count/N)



##########
# import warnings
# warnings.filterwarnings('ignore')

import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline
def f(x):
    return np.sqrt(1-x**2)
N = 400
x = np.arange(0, 1, 0.01)
y = f(x)
x_rand = np.random.random(N)
y_rand = np.random.random(N)

ind_below = np.where(y_rand < f(x_rand))
ind_above = np.where(y_rand >= f(x_rand))

pts_below = plt.scatter(x_rand[ind_below], y_rand[ind_below], color = "green")
pts_above = plt.scatter(x_rand[ind_above], y_rand[ind_above], color = "blue")
plt.plot(x, y, color = "red")

plt.legend((pts_below, pts_above),
           ('Pts below the curve', 'Pts above the curve'),
           loc='lower left',
           ncol=3,
           fontsize=8)
#plt.show()


#############

import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline
N = 400
x0 = 1
x1 = 15
def f(x):
    return x**np.cos(x)+2

x = np.arange(1, 15, 0.01)
y = f(x)
fmax = max(y)
x_rand = x0 + (x1 - x0)*np.random.random(N)
y_rand = np.random.random(N)*fmax

ind_below = np.where(y_rand < f(x_rand))
ind_above = np.where(y_rand >= f(x_rand))

pts_below = plt.scatter(x_rand[ind_below], y_rand[ind_below], color = "green")
pts_above = plt.scatter(x_rand[ind_above], y_rand[ind_above], color = "blue")
plt.plot(x, y, color = "red")

plt.legend((pts_below, pts_above),
           ('Pts below the curve', 'Pts above the curve'),
           loc='lower left',
           ncol=3,
           fontsize=8)
#plt.show()

############

import numpy as np
import matplotlib.pyplot as plt
def definite_integral_show(f, x0, x1, N):
    """Approximate the definite integral of f(x)dx between x0 and x1 using
    N random points

    Arguments:
    f -- a function of one real variable, must be nonnegative on [x0, x1]
    N -- the number of random points to use


    """
    #First, let's compute fmax. We do that by evaluating f(x) on a grid
    #of points between x0 and x1
    #This assumes that f is generally smooth. If it's not, we're in trouble!
    x = np.arange(x0, x1, 0.01)
    y = f(x)
    f_max = max(y)


    #Now, let's generate the random points. The x's should be between
    #x0 and x1, so we first create points beterrm 0 and (x1-x0), and
    #then add x0
    #The y's should be between 0 and fmax
    #
    #                  0...(x1-x0)
    x_rand = x0 + np.random.random(N)*(x1-x0)
    y_rand = 0 +  np.random.random(N)*f_max



    #Now, let's find the indices of the poitns above and below
    #the curve. That is, for points below the curve, let's find
    #   i s.t. y_rand[i] < f(x_rand)[i]
    #And for points above the curve, find
    #   i s.t. y_rand[i] >= f(x_rand)[i]
    ind_below = np.where(y_rand < f(x_rand))
    ind_above = np.where(y_rand >= f(x_rand))


    #Finally, let's display the results
    plt.plot(x, y, color = "red")
    plt.scatter(x_rand[ind_below], y_rand[ind_below], color = "green")
    plt.scatter(x_rand[ind_above], y_rand[ind_above], color = "blue")
    plt.legend((pts_below, pts_above),
           ('Pts below the curve', 'Pts above the curve'),
           loc='lower left',
           ncol=3,
           fontsize=8)

    print("Number of pts above the curve:", len(ind_above[0]))
    print("Number of pts below the curve:", len(ind_below[0]))
    print("N. below/N.total:", len(ind_below[0])/N)
    print("Rectangle area:", f_max*(x1-x0))
    print("Area under the curve:", f_max*(x1-x0)*len(ind_below[0])/N)


def g(x):
    return x
definite_integral_show(g,0,5,500)
plt.show()

