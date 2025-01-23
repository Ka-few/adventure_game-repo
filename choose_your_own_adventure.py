name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go either left or right: ").lower()

if answer == "left":
    answer = input("You have come to a river, you can walk around it or swim across: ")

    if answer == "swim":
        print("You did not make it across. You were eaten by a crocodile.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game")
    else: 
        print('Not a valid option. You lose.')

elif answer == "right":
    answer = input("You've come to a bridge and it looks wobbly, do you want to cross it or head back (cross/back)?: ")
    if answer == "back":
        print("Your adventure comes to an end. You lose!")
    elif answer == "cross":
        answer = input("You meet a stranger across the bridge. Do you talk to him (yes/no)?: ")
        if answer == "yes":
            print("The stranger gives you a map and you win!")
        elif answer == "no":
            print("You don't get the map and you lose!")
        else: 
            print('Not a valid option. You lose.')
    else: 
        print('Not a valid option. You lose.')
else:
    print('Not a valid option. You lose.')

print("Thank you", name, "for playing the game!")