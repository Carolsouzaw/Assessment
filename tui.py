"""
TUI is short for Text-User Interface. This module is responsible for communicating with the user.
The functions in this module will display information to the user and/or retrieve a response from the user.
Each function in this module should utilise any parameters and perform user input/output.
A function may also need to format and/or structure a response e.g. return a list, tuple, etc.
Any errors or invalid inputs should be handled appropriately.
Please note that you do not need to read the data file or perform any other such processing in this module.
"""

"""Task 3"""
print("Please enter the letter which corresponds with your dessired menu choice:")
print("[A] View Data")
print("[B] Visualise Data")
print("[X] Exit")

choice=input()

"""Task 4"""
if choice=="A":
    print(f"You have chosen option {choice}")
elif choice=="B":
    print(f"You have chosen option {choice}")
elif choice=="X":
    print(f"You have chosen option {choice}")
else:
    print("Invalid option")

