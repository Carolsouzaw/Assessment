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

"""Task 11"""

def top_10_locations_by_avg_rating_for_park(data, park_name):
    park_name = park_name.strip().lower()

    totals = {}
    counts = {}

    for row in data:
        branch = row.get("Branch", "").strip().lower()
        if branch != park_name:
            continue

        location = row.get("Reviewer_Location", "").strip()
        rating_str = row.get("Rating", "").strip()

        try:
            rating = int(rating_str)
        except ValueError:
            continue

        totals[location] = totals.get(location, 0) + rating
        counts[location] = counts.get(location, 0) + 1

    averages = []
    for location in totals:
        avg = totals[location] / counts[location]
        averages.append((location, avg))

    averages.sort(key=lambda x: x[1], reverse=True)
    return averages[:10]

"""Task 12"""

def average_rating_by_month_for_park(data, park_name):
    park_name = park_name.strip().lower()

    totals = {}
    counts = {}

    for row in data:
        branch = row.get("Branch", "").strip().lower()
        if branch != park_name:
            continue

        year_month = row.get("Year_Month", "").strip()
        rating_str = row.get("Rating", "").strip()

        try:
            rating = int(rating_str)
        except ValueError:
            continue

        if "-" in year_month:
            month = year_month.split("-")[1]
        else:
            continue

        totals[month] = totals.get(month, 0) + rating
        counts[month] = counts.get(month, 0) + 1

    month_order = ["01","02","03","04","05","06","07","08","09","10","11","12"]

    results = []
    for m in month_order:
        if m in totals:
            avg = totals[m] / counts[m]
            results.append((m, round(avg, 2)))
        else:
            results.append((m, 0))

    return results