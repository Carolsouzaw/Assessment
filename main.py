"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, and for visualising information.

Note:   any user input/output should be done in the module 'tui'
        any processing should be done in the module 'process'
        any visualisation should be done in the module 'visual'
"""


import tui
import process


def main():
    tui.display_title()

    reviews = process.load_dataset("disneyland_reviews.csv")

    print("Finished reading in the dataset.")
    print(f"Number of rows in the dataset: {len(reviews)}")

    tui.display_main_menu()

    choice = input().upper()


    """Task 4"""

    if choice in ["A", "B", "X"]:
        print(f"You have chosen option {choice}")
    else:
        print("Invalid menu choice. Please try again.")


if __name__ == "__main__":
    main()



