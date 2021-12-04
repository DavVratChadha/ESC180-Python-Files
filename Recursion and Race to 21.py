def fact(n):
    if n == 0: #base case
        return 1
    #recursive step
    return n*fact(n-1)

print(fact(5))

#to make a recursive function:
#1) make a base case to end the recursion
#2) make a recursive step to reach to base case


def is_even(n):
    if n == 0:
        return True
    return not is_even(n-1)

print(is_even(3))

L = [12,3,5,123,1,-5]

def print_list(L):
    #base case
    if len(L) == 0:
        return
    #recursive step
    print(L[0])
    print_list(L[1:])

print_list(L)

def print_list_backward(L):
    #base case
    if len(L) == 0:
        return
    #recursive step
    # print(L[-1])
    # print_list_backward(L[:-1])
    #or
    print_list_backward(L[1:])
    print(L[0])

print_list_backward(L)



###########
#Race to 21
#start at 0
#players can alternately say +1 or +2
#first palyer to reach 21 wins

#0
#Player 1: +1 # 1
#Player 2: +1 # 2
#Player 1: +2 # 4
#Player 2: +1 # 5
#.........
#Player 1: +1 # 21

def is_win21(n):
    """Returns True if the player has any chance to win the game at all if they are at number n before their turn"""
    #base cases
    if n == 19 or n == 20:
        return True
    if n == 21:
        return False

    #recursive step
    return not is_win21(n+1) or not is_win21(n+2)

def is_win21_simple(n):
    """When each opponet can only go +1"""
    if n == 20:
        return True
    return not is_win21_simple(n+1)

import random
def move21(n):
    """returns a move that wins the race to 21 game (optimally play) if possible, otherwise return a random move"""
    if not is_win21(n+1):
        return 1
    elif not is_win21(n+2):
        return 2
    else:
        return int(2*random.random()) + 1

def game21():
    n = 0
    print("n = " + str(n))

    while True:
        user_move = int(input("Move: "))
        n += user_move
        print("n = " + str(n))
        if n == 21:
            print("User won!")
            return

        computer_move = move21(n)
        n += computer_move
        print("n = " + str(n))
        if n == 21:
            print("Computer won!")
            return

def game21_nice(cur_player):
    n = 0
    print("n = " + str(n))

    while n!=21:
        if cur_player == "USER":
            move = int(input("MOVE: "))
            cur_player = "COMPUTER"
        else:
            move = move21(n)
            cur_player = "USER"

        n += move
        print("n = " + str(n))

    if cur_player == "USER":
        print("Computer won")
    else:
        print("User won")


