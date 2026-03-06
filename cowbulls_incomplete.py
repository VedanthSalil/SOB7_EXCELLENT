import random

def compare_numbers(number, user_guess):
    bulls = 0
    cows = 0
    '''
     logic for the function , it loops for the length of the number (which is 4) then we use indexing cause user guess and number are strings and we have same
     value for i in the loop so we compare both of them , if value is same at the same position (because we are indexing i) then we put a bull in bull variable
     and if any number of the user 4 digit number  matches the  accual number it adds cow using same indexing but we just index the user_guess string
     '''
    for i in range(len(number)):
        if user_guess[i] == number[i]:
            bulls += 1
        elif user_guess[i] in number:
            cows += 1
    return [cows, bulls]
  

playing = True #gotta play the game
#making the random occur from 1000 cause we need 4 digit and nothing lower than 4 so changed 'randint(0,999)' to 'randint(1000,9999)
number = str(random.randint(1000,9999)) #random 4 digit number
guesses = 0
print(number) #fixed print statement

print("Let's play a game of Cowbull!") #explanation
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("For every number that exists in the sequence but is in wrong place, you get a cow. For every one in the right place, you get a bull.")
print("The game ends when you get 4 bulls!")
print("Type exit at any prompt to exit.")

while playing:
    #changed 'raw_input' to input
    user_guess = input("Give me your best guess!")
    if user_guess == "exit":
        break
    cowbullcount = compare_numbers(number,user_guess)
    guesses+=1

    print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

    if cowbullcount[1]==4:
        playing = False
        print("You win the game after " + str(guesses) + "! The number was "+str(number))
        break #redundant exit
    else:
        print("Your guess isn't quite right, try again.")
