import tkinter as tk

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
