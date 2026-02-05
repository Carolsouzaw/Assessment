"""
This module is responsible for visualising the data using Matplotlib.
Any visualisations should be generated via functions in this module.
"""


"""Task 10"""
import matplotlib.pyplot as plt


def show_reviews_pie_chart(counts_dict):
    labels = list(counts_dict.keys())
    values = list(counts_dict.values())

    plt.figure()
    plt.pie(values, labels=labels, autopct="%1.1f%%")
    plt.title("Number of Reviews per Park")
    plt.show()

"""Task 11"""
import matplotlib.pyplot as plt


def show_top_10_locations_bar_chart(top10, park_name):
    locations = [item[0] for item in top10]
    avgs = [item[1] for item in top10]

    plt.figure()
    plt.bar(locations, avgs)
    plt.title(f"Top 10 Locations by Average Rating - {park_name}")
    plt.xlabel("Reviewer Location")
    plt.ylabel("Average Rating")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

"""Task 12"""
def show_monthly_average_bar_chart(month_data, park_name):
    month_names = {
        "01": "Jan", "02": "Feb", "03": "Mar",
        "04": "Apr", "05": "May", "06": "Jun",
        "07": "Jul", "08": "Aug", "09": "Sep",
        "10": "Oct", "11": "Nov", "12": "Dec"
    }

    months = [month_names[m[0]] for m in month_data]
    averages = [m[1] for m in month_data]

    plt.figure()
    plt.bar(months, averages)
    plt.title(f"Average Rating per Month - {park_name}")
    plt.xlabel("Month")
    plt.ylabel("Average Rating")
    plt.show()