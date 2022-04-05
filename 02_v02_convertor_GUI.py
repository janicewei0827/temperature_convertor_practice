from tkinter import *
from functools import partial  # To prevent unwanted windows
import random


class Convertor:
    def __init__(self, root):
        # Formatting variables
        background_color = "light blue"

        #Initialise ist to hold calculation history
        self.all_calc_list=[]

        # Convertor Frame
        self.convertor_frame = Frame(bg=background_color,
                                     pady=10)
        self.convertor_frame.grid()

        #Temperature Conversion Heading (row 0)
        self.temp_heading_label = Label(self.convertor_frame,
                                        text="Temperature Convertor",
                                        font="Arial 16 bold",
                                        bg=background_color,
                                        padx=10, pady=10)
        self.temp_heading_label.grid(row=0)

        #User instructions (row 1)
        self.temp_instructions_label = Label(self.convertor_frame,
                                             text="Type in the amount to be "
                                                  "converted and then push "
                                                  "one of the buttons below...",
                                             font="Arial 13 italic", wrap=250,
                                             justify=LEFT, bg=background_color,
                                             padx=10, pady=10)
        self.temp_instructions_label.grid(row=1)

        #Temperature entry box (row 2)
        self.to_convert_entry = Entry(self.convertor_frame, width=20,
                                      font="Arial 13 bold")
        self.to_convert_entry.grid(row=2)

        #Conversion buttons frame (row 3), orchid | khakil
        self.conversion_buttons_frame = Frame(self.convertor_frame)
        self.conversion_buttons_frame.grid(row=3, pady=10)

        self.to_c_button = Button(self.conversion_buttons_frame,
                                  text="To Centigrade", font="Arial 10 bold",
                                  highlightbackground="Khaki1", padx=10, pady=10,
                                  command=lambda: self.temp_convert(-459))
        self.to_c_button.grid(row=0, column=0)

        self.to_f_button = Button(self.conversion_buttons_frame,
                                  text="To Fahrenheit", font="Arial 10 bold",
                                  highlightbackground="Orchid1", padx=10, pady=10,
                                  command=lambda: self.temp_convert(-273))
        self.to_f_button.grid(row=0, column=1)

        #Answer label (row 4)
        self.converted_label = Label(self.convertor_frame, font="Arial 16 bold",
                                     fg="purple", bg=background_color,
                                     pady=10, text="Conversion goes here")
        self.converted_label.grid(row=4)

        #History / Help button frame (row 5)
        self.hist_help_frame = Frame(self.convertor_frame)
        self.hist_help_frame.grid(row=5, pady=10)

        self.history_button = Button(self.hist_help_frame, font="arial 12 bold",
                                       text="Calculation History", width=15,
                                     command=lambda: self.history(self.all_calc_list))
        self.history_button.grid(row=0, column=0)

        if len(self.all_calc_list) == 0:
            self.history_button.config(state=DISABLED)

        self.help_button = Button(self.hist_help_frame, font="Arial 12 bold",
                                  text="Help", width=5)
        self.help_button.grid(row=0, column=1)

    def temp_convert(self, low):
        print(low)

        error = "#ffafaf" #pale pink background for when entry box has errors

        #Retrieve amount entered into Entry field
        to_convert=self.to_convert_entry.get()

        try:
            to_convert = float(to_convert)
            has_errors = "no"

            #check and convert to Farhrenheit
            if low == -273 and to_convert >= low:
                fahrenheit = (to_convert * 9/5) + 32
                to_convert = self.round_it(to_convert)
                fahrenheit = self.round_it(fahrenheit)
                answer = "{} degrees C is {} degrees F".format(to_convert, fahrenheit)

            #check and convert to Centigrade
            elif low == -459 and to_convert >= low:
                celsius = (to_convert - 32) * 5/9
                to_convert = self.round_it(to_convert)
                celsius = self.round_it(celsius)
                answer = "{} degrees F is {} degrees C".format(to_convert, celsius)

            else:
                #input is invalid (too cold!!)
                answer = "Too Cold!"
                has_errors = "yes"

            #display answer
            if has_errors == "no":
                self.converted_label.configure(text=answer, fg="blue")
                self.to_convert_entry.configure(bg="white")
            else:
                self.converted_label.configure(text=answer, fg="red")
                self.to_convert_entry.configure(bg=error)

        #Add Answer to list for History
            if answer != "Too cold!":
                self.all_calc_list.append(answer)
                print(self.all_calc_list)

        except ValueError:
            self.converted_label.configure(text="Enter a number!!", fg="red")
            self.to_convert_entry.configure(bg=error)

    def round_it(self, to_round):
        if to_round % 1 == 0:
            rounded = int(to_round)
        else:
            rounded = round(to_round,1)

        return rounded

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Convertor(root)
    root.mainloop()
