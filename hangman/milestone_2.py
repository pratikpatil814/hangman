import random
word_list = ["apple","banana","grapes","watermelon","kiwi"]
choice = random.choice(word_list)
word = choice
guess = str(input("enter a single letter "))
if not len(guess) > 1 :
    print("Good guess!")
else :
    print("Oops! That is not a valid input.")