import tkinter as tk

# using a class to encapsulate the calculator
# so oop principles can be used
class Calculator:
    def __init__(self, window):
        # GUI WINDOW
        window = tk.Tk()
        window.title("nrn's calculator")

        # DIMENSIONS
        window.geometry("500x500")

        # CREATE BUTTONS
        buttons = [
            "7", "8", "9", "",
            "4", "5", "6", "",
            "1", "2", "3", "",
            "0", "", "", "",
            "(", ")", "C"
        ]

        # RUN THE APPLICATION
        window.mainloop()

    def create_btn(self, value, row, col):
        pass

    def btn_pressed(self, num):
        pass

    def clear_calc(self):
        pass

    def calc_result(self):
        pass

