#!/usr/bin/env python3

# Created By: Spencer Scarlett
# Date: Oct 20, 2022
# A program which calculates if the year is a leap year ot not


def main():

    # Spacer
    print("")

    # Basic info about the program
    print("This is a program that is used for calculating a leap year.")

    # Receive the user year
    user_input_year = input("Input the year you wish to calculate: ")

    # Spacer
    print("")

    # Tries to catch any invalid inputs
    try:
        user_input_year = int(user_input_year)

    # Restarts the program is invalided input found
    except ValueError:
        print(f"Your input {user_input_year} is not valid (e.g. 2020)\n")
        return main()

    # First check if the user input can be divisible by 4
    if user_input_year % 4 == 0:

        # Second check if the user input can be divisible by 100
        if user_input_year % 100 == 0:

            # Third check if the user input can be divisible by 400
            if user_input_year % 400 == 0:
                print(f"{user_input_year} is a leap year!\n")

            # Code to be ran if the can't be divided by 400
            else:
                print(f"{user_input_year} is not a leap year!\n")

        # Code to be ran if the can't be divided by 100
        else:
            print(f"{user_input_year} is not a leap year!\n")

    # Code to be ran if the can't be divided by 4
    else:
        print(f"{user_input_year} is not a leap year!\n")


if __name__ == "__main__":
    main()
