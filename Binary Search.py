#Binary Search
#task: given asorted list, determine if e is in the list

L = [1,2,12,20,25,1000,100230]
#is e smaller than the middle elemment of L?
#is yes, just search in the first half of L
#if no, search in the sevond half in L
def binary_search(L,e):
    low = 0 #low index of list L
    high = len(L)-1

    #currently looking at L[low:high+1]

    while high - low >= 2:
        mid = (low + high)//2
        if L[mid] > e:
            high = mid - 1
        elif L[mid] < e:
            low = mid + 1
        else: #L[mid] == e
            return mid

    #high - low < 2
    if L[low] == e:
        return low
    elif L[high] == e:
        return high
    return None

print(binary_search(L,22))
print(binary_search(L,1000))
#keep track of high - low
#intitially: high - low = n-1
#2nd iteration: high - low < (n-1)/2
#3rd iteration: high - low < (n-1)/4
#4th iteration: high - low < (n-1)/8
#.........
#stop when (high - low) < 2
#1,2,4,8........,(n-1)
#{..... log2(n-1) .......} number of steps to reach (n-1)


#runtime complexity = O(log(n))

def find_i(L,e):
    "Return index if e present in the list L"
    for i in range(len(L)): #1 operation for computing range(len(L)
        if L[i] == e:       #2 operation for finding L[i] and then comparrison
            return i        #1 operation for retuning i

    return None             #1 operation

#runtime complexity is = O(2n + 2) roughly = O(n)
#where n = length of list L


#runtime complexity is the worst case scenerio

#f(n) is O(g(n)) if f(n) does not grow faster than g(n)
#i.e. g(n) must grow slower than g(n)

#f(n) is O(g(n)) if lim        sup f(n)/g(n) < infty
#                   N->infty   n>=N
#where sup => max => least upper bound




#2n+1 is O(n)
#0.5 n is O(n^2) but we want to say its O(n)
#sqrt(100000000*n) is O(n)  (also O(sqrt(n))

#usually we want to give a tight asymptotis bound on the worst case runtime
#complexity (meaning f(n) is O(g(n)), where g(n) grows as slowly as possiple)

#n is not O(sqrt(n))
#2^n is not O(n^2)
