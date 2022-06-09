import random


def game():
    start_game = True
    options = ['R', 'P', 'S']
    cpu_choice = random.choice(options)
    user = input('Enter your name:\n').lower()
    user_input = input('\r "R" for rock, \n "P" for paper, \n "S" for scissors \n Enter your choice: \n').upper()

    while start_game:

        if cpu_choice == 'R':
            if user_input == 'R':
                print('It is a tie')
                user_tie_input = input('Want to play again? "y" or "n":\n').lower()
                if user_tie_input == 'y':
                    game()
                else:
                    start_game = False
            elif user_input == 'P':
                print(f'{user} wins, computer lose')
                user_tie_input = input('Want to play again? "y" or "n":\n').lower()
                if user_tie_input == 'y':
                    game()
                else:
                    start_game = False
            elif user_input == 'S':
                print(f'{user} lose, computer wins')
                user_tie_input = input('Want to play again? "y" or "n":\n').lower()
                if user_tie_input == 'y':
                    game()
                else:
                    start_game = False
            else:
                print('Invalid Input, try again')
                game()

        elif cpu_choice == 'P':
            if user_input == 'R':
                print(f'{user} lose, computer wins')
                user_tie_input = input('Want to play again? "y" or "n":\n').lower()
                if user_tie_input == 'y':
                    game()
                else:
                    start_game = False
            elif user_input == 'P':
                print('It is a tie')
                user_tie_input = input('Want to play again? "y" or "n":\n').lower()
                if user_tie_input == 'y':
                    game()
                else:
                    start_game = False
            elif user_input == 'S':
                print(f'{user} wins, computer lose')
                user_tie_input = input('Want to play again? "y" or "n":\n').lower()
                if user_tie_input == 'y':
                    game()
                else:
                    start_game = False
            else:
                print('Invalid Input, try again')
                game()

        else:
            if user_input == 'R':
                print(f'{user} wins, computer lose')
                user_tie_input = input('Want to play again? "y" or "n":\n').lower()
                if user_tie_input == 'y':
                    game()
                else:
                    start_game = False
            elif user_input == 'P':
                print(f'{user} lose, computer wins')
                user_tie_input = input('Want to play again? "y" or "n":\n').lower()
                if user_tie_input == 'y':
                    game()
                else:
                    start_game = False
            elif user_input == 'S':
                print('It is a tie')
                user_tie_input = input('Want to play again? "y" or "n":\n').lower()
                if user_tie_input == 'y':
                    game()
                else:
                    start_game = False
            else:
                print('Invalid Input, try again')
                game()


game()
