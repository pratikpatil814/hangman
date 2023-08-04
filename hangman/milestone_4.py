import random
class Hangman:
    def __init__(self,word_list,num_lives=5):
         # Initialize the Hangman game with a list of words and the number of lives.
        self.word_list = word_list
        word = random.choice(self.word_list)
        self.word_guessed = [word[i] for i in range(len(word))] # List to store already guessed letters
        self.output_screen = ["_" for _ in range(len(word))]  # Initialize the display of word
        self.num_letter = int(len(set(self.word_guessed) & set(self.word_guessed)))
        self.list_of_guesses = []
        self.num_lives=num_lives
    def check_guess(self,guess):
        # Check if the guessed letter is correct and update the output screen and number of lives accordingly.
        guess = guess.lower()
        if guess in self.word_guessed:
            print(f"Good guess! {guess} is in the word.")
            self.num_letter -=1
            count = 0
            for i in self.word_guessed:
                if guess == i:
                    self.output_screen[count] = guess
                count += 1
            print(self.output_screen)
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")      
            self.num_lives -= 1
        print(f'You have {self.num_lives} lives left.')
        
    def ask_for_input(self):
        # Ask the user to enter a single letter and handle the input validation.
        while True:
            guess = input("enter a single letter ")
            guess = guess.lower()
            if not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif(guess in self.list_of_guesses):
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break




