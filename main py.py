import random
words = ["teoman","car","canada","employment","business","cactus","toronto"]
chosen_word = None
chosen_word_list = []
playground = []
game_word = None
lives = 5
guess = None
continue_game = True
def randomizer():
    global chosen_word
    global chosen_word_list
    chosen_word = random.choice(words)
    for i in chosen_word:
        chosen_word_list += i


def attacher():
    global chosen_word_list
    global playground
    for i in chosen_word_list:
        playground += "_"

def update_play_word(chosen_word_list, playground, guess):
    for i in range(len(chosen_word_list)):
        if chosen_word_list[i] == guess:
            playground[i] = guess


while continue_game == True:
    randomizer()
    attacher()
    while lives > 0:
        print(f'Current Status: {playground}')
        guess = str(input("Guess the letter: ")).lower()
        if guess in playground:
            print("You already guessed this! try again")
        elif guess in chosen_word_list and guess not in playground:
            update_play_word(chosen_word_list,playground,guess)
            game_word = ''.join(playground)
            print(playground)
            if set(game_word) == set(chosen_word):
                print("Congrats! You won!")
                continue_game = False
                break
        else:
            lives -=1
            print(f'Wrong! remaining lives = {lives}')
    if lives == 0:
        print("Sorry, you lost the game!")
        break



