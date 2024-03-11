# File: CS112_A1_T2_Game2_20230408.py

# Purpose :
"""Number scrabble is played with 2 players with the list of numbers between 1 and 9. Each player takes
turns picking a number from the list. Once a number has been picked, it cannot be picked
again. If a player has picked three numbers that add up to 15, that player wins the game.
However, if all the numbers are used and no player gets exactly 15, the game is a draw."""

# Author: Moaaz Ahmed kareem

# ID: 20230408

# Printing a message to inform the two players how to play....
print("Each player takes turns picking a number between 1 and 9, inclusive. Once a number has been picked, it cannot be picked again. If a player has picked three numbers that add up to 15, that player wins the game. However, if all the numbers are used and no player gets exactly 15, the game is a draw.")

# Creating a list of numbers from 1 to 9....
num_list = list(range(1,10))  # 10 because the last number in the list is (end - 1)

# Making a list for each player to store chosen numbers....
list_1 = []
list_2 = []


def main():

    # Starting the game....
    while True:

        # Getting a number from player 1....
        num1 = valid_input("player 1")

        # Removing num1 from num_list....
        num_list.remove(num1)

        # Adding num1 to the player 1's list....
        list_1.append(num1)

        # Checking if player 1 has 3 numbers that add up to 15....
        if is_sum_15(list_1):

            # Printing a win message and terminate the game....
            print("Player 1 wins!")
            return

        # Checking if there are number in num_list to choose from....
        if len(num_list) == 0:

            # If no player won and there are no number to choose from then print draw and terminate the game....
            print("Draw!")
            return

        # Getting a number from player 2....
        num2 = valid_input("player 2")

        # Removing num2 from num_list....
        num_list.remove(num2)

        # Adding num2 to the player 2's list....
        list_2.append(num2)

        # Checking if player 2 has 3 number that add up 15....
        if is_sum_15(list_2):

            # Printing a win message and terminate the game....
            print("Player 2 wins!")
            return

        # Checking if there are number in num_list to choose from....
        if len(num_list) == 0:

            # If no player won and there are no number to choose from then print draw and terminate the game....
            print("Draw!")
            return


# Defining a function to validate user's input....
def valid_input(player_num):

    # Making a loop to re-prompt the player again for a number if the input is not correct....
    while True:
        try:
            num = int(input(f"{player_num}, Enter a number between 1 and 9 which wasn't chose before: "))
            break
        except ValueError:
            print("Please enter a number")

    # If the number provided is not in the required range or not in the list re-prompt the user recursively....
    if num not in num_list:
        print("Please enter a valid number")
        return valid_input(player_num)

    # else --> the number matches requirements, then return num....
    else:
        return num


def is_sum_15(list):
    # iterating over the list to see if there are 3 values that their sum = 15....
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            for k in range(j+1, len(list)):
                if list[i] + list[j] + list[k] == 15:
                    return True

    # If iterated over the list and didn't return True then there are no 3 values that their sum = 15, so return False....
    return False


main()