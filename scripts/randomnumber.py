# import random
# n = random.randrange(1,10)
# guess = int(input("entre number :"))
# while n != guess:
#     if guess < n:
#         print("too low")
#         guess = int(input("entre number :"))

#     elif guess > n:
#         print("too high")
#         guess = int(input("entre number :"))

        

#     else:
#         break

# print('you guessed the right number')

'''

------------------------version 2 ----------guessing game

'''

import random

attempts_list = []

def show_score():
    if not show_score:
        print("there's no score, its yours for the taking")
    else:
        print(f"the current high score is"
              f'{attempts_list} attempts')
        
def start_game():
    attempts = 0
    rand_num = random.randint(1, 10)
    print('Hello traveler! Welcome to the game of guesses!')
    player_name = input('What is your name? ')
    wanna_play = input(
        f'Hi, {player_name}, would you like to play '
        f'the guessing game? (Enter Yes/No): ')

    if wanna_play.lower() != 'yes':
        print('That\'s cool, Thanks!')
        exit()
    else:
        show_score()

    while wanna_play.lower() == 'yes':
        try:
            guess = int(input('Pick a number between 1 and 10: '))
            if guess < 1 or guess > 10:
                raise ValueError(
                    'Please guess a number within the given range')

            attempts += 1
            attempts_list.append(attempts)

            if guess == rand_num:
                print('Nice! You got it!')
                print(f'It took you {attempts} attempts')
                wanna_play = input(
                    'Would you like to play again? (Enter Yes/No): ')
                if wanna_play.lower() != 'yes':
                    print('That\'s cool, have a good one!')
                    break
                else:
                    attempts = 0
                    rand_num = random.randint(1, 10)
                    show_score()
                    continue
            else:
                if guess > rand_num:
                    print('It\'s lower')
                elif guess < rand_num:
                    print('It\'s higher')

        except ValueError as err:
            print('Oh no!, that is not a valid value. Try again...')
            print(err)


if __name__ == '__main__':
    start_game()


