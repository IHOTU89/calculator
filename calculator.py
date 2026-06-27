import random
attempts_list = []
def show_score():
    if len(attempts_list) <= 0:
        print("i am your calulator i am  here to help you!")
    else:
        print("The current high score is {} attempts".format(min(attempts_list)))
def start_game():
    random_number = int(random.randint(1, 100))
    print("Hey There! Welcome to the calculator fun world!")
    player_name = input("Enter your name!")
    wanna_play = input("Hi, {}, would you like to  no how to caculate (Enter Yes/No) ".format(player_name))
    ## Where the  calculator_ borad function USED to be
    attempts = 0
    show_boardfunction()
    while wanna_calculate.lower() == "yes":
        try:
            press = input("Pick a number between 1 and 100")
            if int(press) < 1 or int(press) > 100:
                raise ValueError("Please  choose a number within the given range")
            if int(press) == random_number:
                print("Congrats! You guessed it right!")
                attempts += 1
                attempts_list.append(attempts)
                print("It took you {} attempts".format(attempts))
                play_again = input("Would you like to  calculate again? (Enter Yes/No) ")
                attempts = 0
                show_boardfunction()
                random_number = int(random.randint(1, 100))
                if play_again.lower() == "no":
                    print("That's cool, have a nice day!")
                    break
            elif int(press) < random_number:
                print("It's lower")
                attempts += 1
            elif int(press) > random_number:
                print("It's higher")
                attempts += 1
        except ValueError as err:
            print("Oh!, that is not a valid value. Try again...")
            print("({})".format(err))
    else:
        print("That's cool, have a nice day!")
if __name__ == '__main__':
    start_calculator()
