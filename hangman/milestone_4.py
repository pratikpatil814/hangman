import random
class Hangman:
    def __init__(self,word_list,num_lives=5):
        self.word_list = ["apple","banana"]
        choice = random.choice(self.word_list)
        word = choice
        self.word_guessed = []
        self.output_screen = []
        for i in range(len(choice)): # to sepetrate word to character 
            self.word_guessed.append(word[i])
            self.output_screen.append("_")
        self.num_letter = len(set(self.word_guessed) & set(self.word_guessed))
        self.list_of_guesses = []
        self.num_lives=num_lives
    def check_guess(self,guess):
        guess = guess.lower()
        if guess in self.word_guessed:
            print(f"Good guess! {guess} is in the word.")
            count = 0
            for i in self.word_guessed:
                if guess == i:
                    self.output_screen[count] = guess
                count += 1
            print(self.output_screen)
        else :
            print(f"Sorry, {guess} is not in the word. Try again.")      
            self.num_lives -= 1
        print(f'You have {self.num_lives} lives left.')
        
    def ask_for_input(self):
        while True:
            guess = input("enter a single letter ")
            guess = guess.lower()
            if not guess.isalpha:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif(guess in self.list_of_guesses):
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
            #if not len(guess) > 1 :# to check the lenth of given input
        #     if guess.isalpha: # to check is given character is sting or not
            #        break
            #else :
            #   print("Invalid letter. Please, enter a single alphabetical character.")


hangman = Hangman(["apple","banana"])
hangman.ask_for_input()


