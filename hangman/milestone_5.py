import milestone_4 as ml
def play_game(word_list):
    game = ml.Hangman(word_list)
    while True:
        print("_" * 30)
        if game.num_lives == 0:
            print('You lost!')
            break
        elif game.num_letter > 0:
            game.ask_for_input()
        else :
            print("Congratulations. You won the game!") 
            break
word_list = ["apple","banana","grapes","watermelon","kiwi"]
play_game(word_list)


