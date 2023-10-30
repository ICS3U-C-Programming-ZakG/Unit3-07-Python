#!/usr/bin/env python3
# Created by: Zak Goneau
# Created on: Oct. 30, 2023
# This program checks the user inputted age and will tell them if they can date their grandchild using AND and OR.


def main():
    # Introduce program to user and get user age
    print(
        "This program checks the user inputted age and will tell them if they can date their grandchild\n"
    )
    user_age_str = input("Please enter an age: ")

    # Try casting user age as string to integer
    try:
        user_age_int = int(user_age_str)

        # If successfully casted to integer check if it is within valid range to date
        if (user_age_int > 25) and (user_age_int < 40):
            print("You can date our grandchild.")

        # Check if user age is too young
        elif (user_age_int < 25) and (user_age_int > 0):
            print("You are too young to date our grandchild.")

        # Check if user age is too old
        elif (user_age_int > 40) and (user_age_int < 120):
            print("You are too old to date our grandchild.")

        # tell user their number is not valid
        else:
            print("{} is not a valid age.".format(user_age_int))

    # tell user their input is not an age
    except Exception:
        print("{} is not an age.".format(user_age_str))


if __name__ == "__main__":
    main()
