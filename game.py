


import random
from inputimeout import inputimeout, TimeoutOccurred


def game():
  ab = 1
  score = 0
  while ab == 1:
    
     try:
        choices = ["tim","tom"]
        choice = random.choice(choices)
        print(choice)
        user = inputimeout(prompt='>>', timeout=2)
        if user == "tim" and choice =="tom":
             print("YOU SCORED A POINT")
             score += 1
        elif user == "tom" and choice =="tim":
            print("YOU SCORED A POINT")
            score += 1
        else:
             print("YOU LOST")
             print("Your score is: {}".format(score) )
             ab = ab-1


     except TimeoutOccurred:
       print("Time up")
       print("Your score is: {}".format(score) )
       break

    
print("Welcome to Tim or tom.Type start to begin")
pick = input("Input:   ")
pick = str(pick)
if pick =="start":
    game()
