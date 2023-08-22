import random

class Hangman:
    """
    A class representing the Hangman game.
`
    Attributes:
    - word_list (list): A list of words from which a random word will be chosen.
    - num_lives (int): The number of lives the player has.
    - word_guessed (list): A list containing the letters of the randomly chosen word.
    - output_screen (list): A list representing the current display of the word being guessed.
    - num_letter (int): The number of unique letters in the word being guessed.
    - list_of_guesses (list): A list containing letters that have already been guessed.

    Methods:
    - __init__(self, word_list, num_lives=5): Initializes the Hangman game with a list of words and the number of lives.
    - check_guess(self, guess): Checks if the guessed letter is correct and updates the game accordingly.
    - ask_for_input(self): Asks the user to enter a single letter and handles input validation.
    """

    def __init__(self, word_list, num_lives=5):
        """
        Initialize the Hangman game with a list of words and the number of lives.

        Parameters:
        - word_list (list): A list of words to choose from.
        - num_lives (int, optional): The number of lives the player has. Defaults to 5.
        """
        self.word_list = word_list
        word = random.choice(self.word_list)

        self.word_guessed = [word[i] for i in range(len(word))]
        self.output_screen = ["_" for _ in range(len(word))]

        self.num_letter = len(set(self.word_guessed))
        self.list_of_guesses = []
        self.num_lives = num_lives

    def check_guess(self, guess):
        """
        Check if the guessed letter is correct and update the output screen and number of lives accordingly.

        Parameters:
        - guess (str): The guessed letter.

        Prints messages about the guess result and remaining lives.
        """
        guess = guess.lower()

        if guess in self.word_guessed:
            print(f"Good guess! {guess} is in the word.")
            self.num_letter -= 1
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
        """
        Ask the user to enter a single letter and handle the input validation.

        Continuously prompts the user until a valid letter is entered.
        """
        while True:
            guess = input("Enter a single letter: ")
            guess = guess.lower()

            if not guess.isalpha():
                print("Invalid letter. Please enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break
