##Import libraries
import random
import time

##word lists
car_brands = ["ford","audi"]
countries = ["mexico", "colombia","canada", "venezuela", "uruguay","argentina","guatemala", "panama", "ecuador"]


##Inform the player of the rules
print("Wellcome to the Jumper Game")
time.sleep(1)
print("The objective of the game is to guess the secret word letter by letter")
print("You have 5 lives, you lose a life every time you make a mistake if you run out of lives you lose")   
time.sleep(1)
print("Do you want to play with words that are car brands or country names?")
time.sleep(2)
choose = input("Choose 'C' for cars or 'P' for countries : ")

##Select word category

while True:
    if choose.lower( )=="c":
        print("Good choice!! ")
        word_secret = random.choice(car_brands)
        break
    elif choose.lower( )=="p":
        print("Good choice!! ")
        word_secret = random.choice(countries)  
        break
    else:
        print("Please select a valid category")   
        choose = input("Choose 'C' for cars or 'P' for countries : ")
        

##Declare number of lives and start the game
lifes = 5
list_guess_letters= []
print("_" *len(word_secret))

##Ask the player to guess a letter
while True:
    while True:
        guess_letter = input("Guess a letter ( a - z): ")
        if (len(guess_letter) != 1 and guess_letter.isnumeric()):
            print("That's not a letter, try a single letter")
        else:
            if guess_letter.lower() in list_guess_letters:
                print("You have already tried that letter, try another one please")
            else:
                list_guess_letters.append(guess_letter)
                if guess_letter in word_secret:
                    print("Congratulations you guessed a letter")
                else:
                    lifes = lifes - 1
                    print("You were wrong and lost a life")
                    print(f"You have {lifes} lives left")
                    break
##Verify that the player is still in play
    if lifes == 0:
        print(f"You have lost the secret word was: {word_secret}")
        break


##print game results
    actual = ""
    missing_letters = 0

    for letter in word_secret:
        if letter in list_guess_letters:
            actual = actual + letter
 
        else:
            actual = actual + "_"
            missing_letters = missing_letters + 1

    print(actual)
##Logic to determine if the player won
    if missing_letters == 0:
        print("Congrats you win!!")
        print(f"La palabra secreta es: {word_secret}")
        break


