from tkinter import *
from functools import partial  # To prevent unwanted windows
import random


class Convertor:
    def __init__(self, root):
        # Formatting variables
        background_color = "light blue"

        # Converter main screen GUI
        self.convertor_frame = Frame(width=600, height=600, bg=background_color,
                                     pady=10)
        self.convertor_frame.grid()

        #Temperature Conversion Heading (rov 0)
        self.temp_convertor_label = Label(self.convertor_frame, text="Temperature Convertor",
                                          font=("Arial", "25", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_convertor_label.grid(row=0)

        #Help Button (row 1)
        self.help_button = Button(self.convertor_frame, text="Help",
                                  font=("Arial", "14"),
                                  padx=10, pady=10, command=self.help)
        self.help_button.grid(row=1)

    def help(self):
        print("You asked for help.")
        get_help = Help(self)
        get_help.help_text.configure(text="Help text goes here")

class Help:
    def __init__(self, partner):
        background="orange"

        #disable help button
        partner.help_button.config(state=DISABLED)

        #Sets up child window (ie:help box)
        self.help_box = Toplevel()

        #if user click press at the top, closes help and releases help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        #set up GUI Frame
        self.help_frame = Frame(self.help_box, bg=background)
        self.help_frame.grid()

        #set up Help heading (row0)
        self.how_heading = Label(self.help_frame, text="Help / Instructions",
                                 font="arial 25 bold", bg=background)
        self.how_heading.grid(row=0)

        #help text (label, row 1)
        self.help_text = Label(self.help_frame, text="",
                               justify=LEFT, width=40, bg=background, wrap=250)
        self.help_text.grid(row=1)

        #Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text= "Dismiss",
                                  width=10, bg="orange", font="arial 10 bold",
                                  command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        #put help button back to normal
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Convertor(root)
    root.mainloop()
