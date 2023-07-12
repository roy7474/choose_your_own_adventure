name = input('Type your name: ')
print("Welcome", name, "to this adventure!")

answer = input('You are on a dirt road, it has come to and end and you can go left or right. Which way would you like to go? ').lower()

if answer == "left":
    answer = input('you come to a river, you can walk around it or swem across? Type walk around or swim to cross')

    if answer == 'swim':
        print('You swam across and were eaten by an alligator.')
    elif answer == 'walk':
        print('You walk for many miles, ran out of water and you lost the game.')

    else:
        print('Not a valid option. You lose.')

elif answer == 'right':
    answer = input('you come to a bridge, it look wobbly, do you wan to cross it or head back? (cross/back)')

    if answer == 'back':
        print('You go back and lose')
    elif answer == 'cross':
        answer = input(' You cross the bridge and talk to a stranger. Do you talk to them ? (yes/no)')

        if answer == 'yes':
            print('You talk to the stranger and they give you gold. You win')
        elif answer == 'no':
            print('You ignore them. They get offended and you lose.')

        else:
            print('Not a valid option. You lose.')
    else:
        print('Not a valid option. You lose.')

else:
    print('Not a valid option. You lose')