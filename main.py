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

    """Task 5 """
    choice = ""

    while choice != "X":
        tui.display_main_menu()
        choice = input().upper()

        """Task 6"""
        if choice == "A":
            print("You have chosen option A")
            tui.display_view_data_menu()
            sub_choice = input().upper()
            print(f"You have chosen sub-option {sub_choice}")


            """Task 7"""
            if sub_choice == "A":
                park = tui.ask_park_name()
                park_reviews = process.get_reviews_by_park(reviews, park)

                if len(park_reviews) == 0:
                    print("No reviews found for that park.")
                else:
                    for r in park_reviews:
                        print(r)

                """Task 8"""
            elif sub_choice == "B":
                park = tui.ask_park_name()
                location = tui.ask_location()

                total = process.count_reviews_by_park_and_location(reviews, park, location)

                print(f"{park} has received {total} reviews from {location}.")

                """Task 9"""

            elif sub_choice == "C":
                park = tui.ask_park_name()
                year = tui.ask_year()

                avg = process.average_rating_by_park_and_year(reviews, park, year)

                if avg is None:
                    print("No reviews found for that park in that year.")
                else:
                    print(f"The average rating for {park} in {year} is {avg}.")

        elif choice == "B":
            print("You have chosen option B")
            tui.display_visualise_menu()
            sub_choice = input().upper()
            print(f"You have chosen sub-option {sub_choice}")

        elif choice == "X":
            print("Exiting program...")

        else:
            print("Invalid menu choice. Please try again.")


if __name__ == "__main__":
    main()



