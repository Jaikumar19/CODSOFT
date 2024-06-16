import random

print('Winning rules of the game ROCK PAPER SCISSORS are:')
print('Rock beats Scissors')
print('Scissors beat Paper')
print('Paper beats Rock')

while True:
    print('Enter your choice:')
    print('1 - Rock')
    print('2 - Paper')
    print('3 - Scissors')

    choice = int(input('Enter your choice: '))

    while choice > 3 or choice < 1:
        choice = int(input('Enter a valid choice: '))

    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

    print('User choice is:', choice_name)
    print('Now it\'s the computer\'s turn...')

    comp_choice = random.randint(1, 3)

    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'

    print('Computer choice is:', comp_choice_name)
    print(choice_name, 'vs', comp_choice_name)

    if choice == comp_choice:
        print('Its a tie!')
    elif (choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 3) or (choice == 3 and comp_choice == 1):
        print('Computer wins!')
    else:
        print('You win!')

    playagain = input('Do you wanna play again? (yes/no): ')
    if playagain.lower() != 'yes':
        break

print('Thanks for playing!')
