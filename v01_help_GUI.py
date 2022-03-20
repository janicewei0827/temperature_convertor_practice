from tkinter import *
from functools import partial  # To prevent unwanted windows
import random


class Convertor:
    def __init__(self, root):
        # Formatting variables
        background_color = "light blue"

        # Converter main screen GUI
        self.convertor_frame = Frame(width=600, height=600, bg=background_color)
        self.convertor_frame.grid()

        #Temperature COnversion Heading (rov 0)
        self.temp_converter_label = Label(text="Temperature Converter",
                                          font=("Arial", "30", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_converter_label.grid(row=0)

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Convertor(root)
    root.mainloop()
