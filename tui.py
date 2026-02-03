"""
TUI is short for Text-User Interface. This module is responsible for communicating with the user.
The functions in this module will display information to the user and/or retrieve a response from the user.
Each function in this module should utilise any parameters and perform user input/output.
A function may also need to format and/or structure a response e.g. return a list, tuple, etc.
Any errors or invalid inputs should be handled appropriately.
Please note that you do not need to read the data file or perform any other such processing in this module.
"""


"""Section A"""
"""Task 1"""
def display_title():
    title= "Disneyland Review Analyzer"
    dashes= len(title)* '-'

    print(dashes)
    print(title)
    print(dashes)

"""Task 3"""

def display_main_menu():
    print("Please enter the letter which corresponds with your desired menu choice:")
    print("[A] View Data")
    print("[B] Visualise Data")
    print("[X] Exit")

"""Task 6"""

def display_view_data_menu():
    print("Please enter one of the following options:")
    print("[A] View Reviews by Park")
    print("[B] Number of Reviews by Park and Reviewer Location")
    print("[C] Average Score per year by Park")
    print("[D] Average Score per Park by Reviewer Location")


def display_visualise_menu():
    print("Please enter one of the following options:")
    print("[A] Most reviewed Parks")
    print("[B] Park Ranking by Nationality")
    print("[C] Most Popular Month by Park")

"""Task 7"""

def ask_park_name():
    print("Which park would you like to see reviews for?")
    return input().strip()







