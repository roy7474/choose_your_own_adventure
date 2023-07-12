name = input('Type your name: ')
print("Welcome", name, "to this adventure!")

answer = input('You are on a dirt road, it has come to and end and you can go left or right. Which way would you like to go? ').lower

if answer == "left":
    answer = input('you come to a river, you can walk around it or swem across? Type walk around or swim to cross')

    if answer == 'swim':
        print('You swam across and were eaten by an alligator.')
    elif answer == 'walk':
        print('You walk for many miles, ran out of water and you lost the game.')

    else:
        print('Not a valid option. You lose.')
        
elif answer == 'right':
    print()

else:
    print('Not a valid option. You lose')