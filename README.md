# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Milestone 1

- In this project uses GitHub to track changes to the code and save it online in a GitHub repo

## milestone 2

- In this milestone i have focused on follwing stages

1.Define list of poosible wrod
2.Choose a Random word from the lis
3.ask user for an input
4.Check that the inpute is single character
5. start documenting

## Milestone 3

In this milestone, we created functions for the code written in Milestone 2. Here are the steps:

1. Create a function to randomly choose a word from the list of possible words.
2. Create a function to get user input for a single character guess.
3. Create a function to check if the guess is valid (i.e., a single alphabetical character).
4. Create a function to update the `output_screen` variable with the guessed letters.
5. Create a function to check if the game is won (i.e., all letters are guessed correctly).
6. Create a function to check if the game is lost (i.e., the player has run out of lives).
7. Create a function to display the hangman based on the number of incorrect guesses.

By creating these functions, we can better organize our code and make it more modular, which will help us manage the game logic efficiently.

## Milestone 4

In this milestone, we implemented three main classes and the `check_guess()` function, which performs the following tasks:

1. Converts the guessed letter to lowercase.
2. Checks if the guess is in the word.
3. If the guess is correct, prints a message saying "Good guess! {guess} is in the word."
4. Creates a loop to continue the game until the word is guessed or the attempts run out.
5. Asks the user to guess a letter and validates that it is a single alphabetical character.
6. Provides feedback if the guess is invalid or has already been tried.

Additionally, we implemented an `output_screen` variable to display the progress of guessed letters, and the player's lives decrease by 1 with each incorrect guess.

## Milestone 5

In this step, we included everything from the `Hangman` class, combining all the functionalities developed in previous milestones to create a fully functional Hangman game.

The main script for the Hangman game can be found in `milestone_5.py`. The game randomly selects a word from the list, and the player has to guess the word one letter at a time. The game provides feedback on correct and incorrect guesses, updates the display, and shows the hangman based on the number of incorrect attempts.

Feel free to contribute to the project or report any issues you encounter. Happy guessing!