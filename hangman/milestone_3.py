import random
def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else :
        print(f"Sorry, {guess} is not in the word. Try again.")
def ask_for_input():
    while True:
        guess = input("enter a single letter ")
        if not len(guess) > 1 :# to check the lenth of given input
            if guess.isalpha: # to check is given character is sting or not
                break
        else :
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)
word_list = ["apple","banana","grapes","watermelon","kiwi"]
choice = random.choice(word_list)
word = choice
ask_for_input()




