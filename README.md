# Python Calculator (Tkinter)

I made a basic arithmetic python GUI calculator using `Tkinter` library. This project helped me 
understand OOP principles better as I applied the coding principles in a practical way in Python.

## OOP Principles in the Calculator 
My python calculator project follows object orientated programming principles in its code:

#### 1. Encapsulation
Encapsulation is basically about putting related data/functions into one group, called a class.
This keeps the code organised and prevents outside parts of the code from messing with
it internally.

In my calculator, the `Calculator` class groups everything it needs to work together - 
like the display, buttons, and calculation logic. All functions related to the calculator
are inside the class, keeping the code tidy.

#### 2. Abstraction
Abstraction is showing the user only important details. 

For example, in my project, the user interacts with simple functions like `calc_result()`
without needing to know how the calculations are being handled internally. 
Basically, the user presses buttons, and the calculator shows the result, but they don't
understand how the code handles it.

#### 3. Inheritence
Inheritence allows us to create new versions of a class by extending it or modifying it.

I don't use any inheritence in this project, but new features can easily be added using
inheritence.

For example, I could create a `ScientificCalculator` class that has functions like square
roots or logs. This class would inherit all the basic features of the original `Calculator`
class.


#### 4. Polymorphism
Polymorphism allows different classes to use the same function names but with different
logic. 

Again, I haven't used this in my calculator. But it could be used to change the function
of `calc_result()` to perform different types of calculations based on the class, like
for the original `Calculator` class and `ScientificCalculator`.

#### 5. Modularity
Modularity is about breaking a program into small, reusable pieces.
In this project each task (button clicking, displaying results) is handled by a different 
function. These bits of code can be reused in other projects or expanded with other features
(like maybe adding more complicated math functions) without changing the core structure.