# Author: SiriusLatte
# Date: 12/28/2021
# Version: 1.0.0
# Simple calculator application made in Python, being object-oriented starting from a class called Calculator.


# Imports
from tkinter import *
from src.utils.constants import *


# Functions
def createdisplay(obj):
    # This function will create the calculations display, where everything will be going to
    # and be showed to the user for simplicity!

    display = Frame(obj.frame, height=154, bg="#2e2e2e")
    display.pack(expand=False, fill="both")

    def createbuttons():
        # Function that create buttons
        frame = Frame(obj.frame, bg="#2b2b2b")
        frame.pack(expand=True, fill="both")

        for digit, _tuple in digits.items():
            buttoncreated = Button(
                frame,
                text=str(digit),
                font=("Arial", 24, "bold"),
                bg="#ededed",
                fg="#363636"
            )
            buttoncreated.grid(row=_tuple[0], column=_tuple[1], sticky=NSEW)

    def createlabels():
        # Function that create labels for the display when clicked buttons
        current = Label(
            display,
            text=obj.total_expression,
            anchor=E,
            pady=16,
            padx=6,
            font=("Helvetica", 14, "bold"),
            bg="#2e2e2e",
            fg="#ededed",
        )
        current.pack(expand=True, fill="both")

        total = Label(
            display,
            text=obj.total_expression,
            anchor=E,
            padx=8,
            font=("Helvetica", 33, "bold"),
            bg="#2e2e2e",
            fg="#ededed",
        )
        total.pack(expand=True, fill="both")

    # Creates button display and the label display
    createlabels()
    createbuttons()


# Calculator application
class Calculator:
    # Init method for the class, called everytime you create a new object from the Class
    def __init__(self):
        self.frame = Tk()
        self.frame.resizable()  # Not resizable
        self.frame.configure(bg="#2e2e2e")
        self.frame.geometry("292x533+200+50")  # "widthxheight"
        self.frame.title("Calculator")
        # self.frame.overrideredirect(True)  # If you want to remove borders, experimental

        # Properties
        self.total_expression = "0"
        self.current_expression = "0"

        # Creates display and buttons at the same time, kinda weird behavior if you ask me!
        createdisplay(self)

    def startapp(self):
        self.frame.mainloop()  # More about this function: https://www.educba.com/tkinter-mainloop/


if __name__ == "__main__":
    Calculator().startapp()  # Starts our new app
