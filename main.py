import tkinter as tk


# using a class to encapsulate the calculator
# so oop principles can be used
class Calculator:
    def __init__(self, window):
        # GUI WINDOW
        self.window = window
        self.window.title("nrn's calculator")
        self.window.configure(bg="#fff")
        self.window.geometry("500x500")
        self.window.resizable(False, False)  # make the window unresizable

        # ENTRY FIELD
        self.input = tk.Entry(window, width=16, font=("Arial", 24), borderwidth=2)
        self.input.grid(row=0, column=0, columnspan=4)

        # VALIDATE INPUT
        self.input.bind("<KeyPress>", self.on_key_press)  # bind so when a key is pressed the on_key_press func triggered

        # CREATE BUTTONS
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+",
            "(", ")", "C"
        ]

        # create the buttons and place them in a grid
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

    @staticmethod
    def on_key_press(event):
        """ trigger when a key is pressed, to check if the inputted key is valid """
        vld_chars = "0123456789+-/*.()"
        # check if the key is invalid, if so block the key press
        if event.char not in vld_chars:
            return "break"

    def create_btn(self, value, row, col):
        """ basic template to create buttons for calc """
        if value == '=':
            btn = tk.Button(self.window, text=value, width=16, height=5, borderwidth=3, bg="grey",
                            command=self.calc_result())
        elif value == 'C':
            btn = tk.Button(self.window, text=value, width=16, height=5, borderwidth=3, bg="grey",
                            command=self.clear_calc())
        else:
            btn = tk.Button(self.window, text=value, width=16, height=5, borderwidth=3, bg="grey", command=lambda:
            self.btn_pressed(value))

        btn.grid(row=row, column=col)

    def btn_pressed(self, num):
        """ handle when a button operator is pressed """
        curDis = self.input.get()

        # if the = is pressed calculate the result
        if num == "=":
            self.calc_result()

        # if clear is pressed clear the display
        elif num == "C":
            self.clear_calc()

        # otherwise a number/operator is pressed add it to the display
        else:
            # clear display and redisplay new eq
            self.input.delete(0, tk.END)
            self.input.insert(0, curDis + num)

    def clear_calc(self):
        """ clear the input"""
        self.input.delete(0, tk.END)

    def calc_result(self):
        """ calculate the result of the inputted calculation"""
        # there might be some errors (like zero division) in the maths so try to see if calc works
        # otherwise display error msg
        try:
            # using eval is not reccommended for bigger prijects bc its vulnreble
            # but this is just a calcultor, so it doesn't matter
            result = eval(self.input.get())
            self.input.delete(0, tk.END)
            self.input.insert(0, str(result))
        # also it's not recommended to use a bare except but theres too many possible errors to go create an except for
        # each of them
        except:
            self.input.delete(0, tk.END)
            self.input.insert(0, "ERROR")

# MAIN
if __name__ == "__main__":
    og_window = tk.Tk()
    calc = Calculator(og_window)
    og_window.mainloop()
