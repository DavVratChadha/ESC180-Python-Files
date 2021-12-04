import time
import random

def game():

    prompts = ["a little girl", "its time to go", "catch me if u can", "i like water", "its time to disco", "i hate canadian food"]

    n = int((len(prompts)-1)*random.random())
    print("You have to type the following phrase:\n" + prompts[n])
    go = input("Press enter to start")
    start = time.time()
    answer = (input("Type answer here:\n")).lower().split(" ")
    end = time.time()

    prompt = prompts[n].split(" ")
    penalty = 1 #1s
    score = 0
    if len(prompt) == len(answer):
        for i in range(len(prompt)):
            if answer[i] == prompt[i]:
                score += 1
    else:
        print("You did not type complete answer. Challenge Failed!!")

    time_marks = end - start + (len(prompts) - score)*penalty
    speed = score/time_marks*60
    print("Your typing speed was " + str(speed) + " words per minute")
    print("Thanks for playing\n--------------------------------------------")
    return

if __name__ == "__main__":
    print("Welcome to the Typing game, where we check how fast u can type")
    print("You have to type the phrase given to u.")
    print("There will be a Penalty of 1s for every Incorrectly typed word.")
    print("WE WILL KNOW IF YOU COPY AND PASTE OUR PHRASE AND THUS YOU WILL BE BANNED FROM OUR GAME!!!")
    flag = 1

    while(flag == 1):
        game()
        flag = int(input("Type 1 to play again or 0 to leave game: "))