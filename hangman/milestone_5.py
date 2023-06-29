import milestone_4 as ml
def play_game(word_list):
    num_lives = 5
    game = ml.Hangman(word_list,num_lives)
    while True:
        print("----------------------------------")
        if game.num_of_lives() == 0:
            print('You lost!')
            break
        elif game.num_of_letter() > 0:
            game.ask_for_input()
        else :
            print("Congratulations. You won the game!") 
            break
word_list = ["apple","banana","grapes","watermelon","kiwi"]
play_game(word_list)


