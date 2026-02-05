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
import visual

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

                """Task 13"""
            elif sub_choice == "D":
                averages = process.average_score_per_park_by_location(reviews)
                for park in averages:
                    print(f"\n{park}")
                    print("-" * len(park))
                    for location in averages[park]:
                        print(f"{location}: {averages[park][location]}")

            """Task 10"""
        elif choice == "B":
            print("You have chosen option B")
            tui.display_visualise_menu()
            sub_choice = input().upper()
            print(f"You have chosen sub-option {sub_choice}")
            if sub_choice == "A":
                counts = process.count_reviews_per_park(reviews)
                visual.show_reviews_pie_chart(counts)

                """Task 11"""
            elif sub_choice == "B":
                park = tui.ask_park_name()
                top10 = process.top_10_locations_by_avg_rating_for_park(reviews, park)

                if len(top10) == 0:
                    print("No data found for that park.")
                else:
                    visual.show_top_10_locations_bar_chart(top10, park)

                """Task 12"""

            elif sub_choice == "C":
                park = tui.ask_park_name()
                month_data = process.average_rating_by_month_for_park(reviews, park)

                visual.show_monthly_average_bar_chart(month_data, park)


        elif choice == "X":
            print("Exiting program...")

        else:
            print("Invalid menu choice. Please try again.")


if __name__ == "__main__":
    main()



