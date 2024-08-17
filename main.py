import tkinter as tk

# using a class to encapsulate the calculator
# so oop principles can be used
class Calculator:
    def __init__(self, window):
        # GUI WINDOW
        self.window = window
        self.window.title("nrn's calculator")
        self.window.configure(bg="#fff")

        # DIMENSIONS
        self.window.geometry("500x500")
        # make the window unresizable
        self.window.resizable(False, False)

        self.display = tk.Entry(window, width=16, font=('Arial', 24), borderwidth=2, relief='solid', bg='#FFFACD')
        self.display.grid(row=0, column=0, columnspan=4)  # Place the display at the top, spanning 4 columns.

        # CREATE BUTTONS
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+",
            "(", ")", "C"
        ]

        # create the buttons and place them in a
        row_index = 1
        col_index = 0
        for button in buttons:
            self.create_btn(button, row_index, col_index)
            # move to next column
            col_index += 1

            # if column is greater than 4th one, reset to the first one
            # and move to the next row
            if col_index > 3:
                col_index = 0
                row_index += 1

        # RUN THE APPLICATION
        self.window.mainloop()

    def create_btn(self, value, row, col):
        if value == '=':
            btn = tk.Button(self.window, text=value, width=16, height=2, borderwidth=3, bg="grey")
        elif value == 'C':
            btn = tk.Button(self.window, text=value, width=16, height=2, borderwidth=3, bg="grey")
        else:
            btn = tk.Button(self.window, text=value, width=16, height=2, borderwidth=3, bg="grey")

        btn.grid(row=row, column=col)

    def btn_pressed(self, num):
        pass

    def clear_calc(self):
        pass

    def calc_result(self):
        pass

if __name__ == "__main__":
    og_window = tk.Tk()
    calc = Calculator(og_window)
    og_window.mainloop()
