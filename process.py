"""
This module is responsible for processing the data.  It will largely contain functions that will recieve the overall dataset and 
perfrom necessary processes in order to provide the desired result in the desired format.
It is likely that most sections will require functions to be placed in this module.
"""

"""Task 2"""

import csv


def load_dataset(filename):
    data = []

    with open(filename, mode="r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    return data

"""Task 7"""

def get_reviews_by_park(data, park_name):
    results = []
    for row in data:
        if row.get("Branch", "").strip().lower() == park_name.strip().lower():
            results.append(row)
    return results

"""Task 8"""
def count_reviews_by_park_and_location(data, park_name, location):
    count = 0
    for row in data:
        if (
            row.get("Branch", "").strip().lower() == park_name.strip().lower()
            and row.get("Reviewer_Location", "").strip().lower() == location.strip().lower()
        ):
            count += 1
    return count
def average_rating_by_park_and_year(data, park_name, year):
    total = 0
    count = 0

    park_name = park_name.strip().lower()
    year = year.strip()

    for row in data:
        branch = row.get("Branch", "").strip().lower()
        year_month = row.get("Year_Month", "").strip()
        rating_str = row.get("Rating", "").strip()

        if branch == park_name and year_month.startswith(year):
            try:
                total += int(rating_str)
                count += 1
            except ValueError:
                pass

    if count == 0:
        return None

    return round(total / count, 2)

"""Task 10"""
def count_reviews_per_park(data):
    counts = {}

    for row in data:
        park = row.get("Branch", "").strip()

        if park in counts:
            counts[park] += 1
        else:
            counts[park] = 1

    return counts