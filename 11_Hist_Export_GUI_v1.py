from tkinter import *
from functools import partial# To prevent unwanted windows
import re

import random


class Convertor:
    def __init__(self, root):

        # Formatting variables
        background_color = "light blue"

         #In actual program this is blank and is populated with user calculations

        self.all_calc_list= ['0 degrees F is -17.8 degrees C',
                             '0 degrees C is 32 degrees F',
                             '100 degrees F is 37.8 degrees C',
                             '5 degrees F is -17.2 degrees F',
                             ]

        #self.all_calc_list=[]

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


        #history Button (row 1)
        self.history_button = Button(self.convertor_frame, text="History",
                                  font=("Arial", "14"),
                                  padx=10, pady=10,
                                     command=lambda: self.history(self.all_calc_list))
        self.history_button.grid(row=1)

        if len(self.all_calc_list) == 0:
            self.history_button.config(state=DISABLED)

    def history(self, calc_history):
        History(self, calc_history)

class History:
    def __init__(self, partner, calc_history):
        background="#a9ef99"           #pale green

        #disable history button
        partner.history_button.config(state=DISABLED)

        #Sets up child window (ie:history box)
        self.history_box = Toplevel()

        #if user click press at the top, closes history and releases history button
        self.history_box.protocol('WM_DELETE_WINDOW',
                                  partial(self.close_history, partner))

        #set up GUI Frame
        self.history_frame = Frame(self.history_box, bg=background)
        self.history_frame.grid()

        #set up history heading (row0)
        self.how_heading = Label(self.history_frame, text="Calculation History",
                                 font="arial 19 bold", bg=background)
        self.how_heading.grid(row=0)

        #history text (label, row 1)
        self.history_text = Label(self.history_frame, text="Here are your most recent "
                                                           "calculations. Please use the "
                                                           "export button to create a text"
                                                           "file of all your calculations for "
                                                           "this session", wrap=200,
                                   font="arial 10 italic",
                                   justify=LEFT, bg=background, fg="maroon",
                                  padx=10, pady=10)
        self.history_text.grid(row=1)

        #History Output goes here...(row2)

        #Generate string from list of calculations
        history_string=""

        if len(calc_history) > 7:
            for item in range(0,7):
                history_string += calc_history[len(calc_history)
                                               - item - 1]+"\n"

        else:
            for item in calc_history:
                history_string += calc_history[len(calc_history) -
                                               calc_history.index(item) - 1] + "\n"
                self.history_text.config(text="Here is your calculation "
                                         "history. You can use the "
                                         "export button to save this "
                                         "data to a text file if "
                                         "desired.")

        #Label ot display calculation history user
        self.calc_label = Label(self.history_frame, text=history_string,
                                bg=background, font="Arial 12", justify=LEFT)
        self.calc_label.grid(row=2)

        #Export/dismiss buttons frame (row3)
        self.export_dismiss_frame = Frame(self.history_frame)
        self.export_dismiss_frame.grid(row=3, pady=10)

        #Export Button
        self.export_button = Button(self.export_dismiss_frame, text="Export",
                                    font="Arial 12 bold",
                                    command=lambda: self.export(calc_history))
        self.export_button.grid(row=0, column=0)

        #Dismiss button
        self.dismiss_button = Button(self.export_dismiss_frame, text= "Dismiss",
                                  font="arial 12 bold",
                                  command=partial(self.close_history, partner))
        self.dismiss_button.grid(row=0, column=1)

    def close_history(self, partner):
        #put history button back to normal
        partner.history_button.config(state=NORMAL)
        self.history_box.destroy()

    def export(self, calc_history):
        Export(self, calc_history)

class Export:
    def __init__(self, partner, calc_history):

        print(calc_history)

        background="#afef99" #pale green

        #disable export button
        partner.export_button.config(state=DISABLED)

        #Sets up child window (ie:export box)
        self.export_box = Toplevel()

        #if user click press at the top, closes export and releases export button
        self.export_box.protocol('WM_DELETE_WINDOW',
                                 partial(self.close_export, partner))

        #set up GUI Frame
        self.export_frame = Frame(self.export_box, width = 300, bg=background)
        self.export_frame.grid()

        #set up Export heading (row0)
        self.how_heading = Label(self.export_frame,
                                 text="Export / Instructions",
                                 font="arial 25 bold", bg=background)
        self.how_heading.grid(row=0)

        #export text (label, row 1)
        self.export_text = Label(self.export_frame, text="Enter a file name "
                                 "in the box below "
                                 "and press the Save "
                                 "button to save your "
                                 "calculation history "
                                 "to a text file. ",
                               justify=LEFT, width=40,
                                 bg=background, wrap=250)
        self.export_text.grid(row=1)

        #Warning text(label, row 2)
        self.export_text = Label(self.export_frame, text="If the filename "
                                 "you entered below "
                                 "already exists "
                                 "its content will "
                                 "be replaced with "
                                 "your calculation "
                                 "history",
                                 justify=LEFT, bg="#ffafaf", fg="maroon",
                                 font="arial 10 italic", wrap=225, padx=10,
                                 pady=10)
        self.export_text.grid(row=2, pady=10)

        #Filename Entry Box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10)

        #Error message labels (initally blank, row4)
        self.save_error_label = Label(self.export_frame, text="", fg="maroon",
                                      bg=background)
        self.save_error_label.grid(row=4)

        #Save/Cancel Frame (row 5)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        #Save and Cancel Buttons (row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, text="Save",
                                  command=partial(lambda: self.save_history(partner, calc_history)))
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel",
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)

    def save_history(self, partner, calc_history):

        #Regular expression
        valid_char="[A-Za-z0-9_]"
        has_error="no"

        filename=self.filename_entry.get()
        print(filename)

        for letter in filename:
            if re.match(valid_char,letter):
                continue
            elif letter == "":
                problem="(no spaces allowed)"
            else:
                problem=("(no {}'s allowed)".format(letter))
            has_error="yes"
            break
        if filename=="":
            problem="can't be blank"
            has_error="yes"

        if has_error=="yes":
            #display error message
            self.save_error_label.config(text="Invalid filename - {}".format(problem))
            #Change entry box
            self.filename_entry.config(bg="#ffafaf")
            print()

        else:
            #if there are no errors, generate text file nd then close dialogue
            #add .txt suffix
            filename=filename+".txt"

            #create file to hold data
            f = open(filename, "w+")

            #add new line the end of each item
            for item in calc_history:
                f.write(item + "\n")

            #close file
            f.close()

            #close dialogue
            self.close_export(partner)


    def close_export(self, partner):
        #put export button back to normal
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Convertor(root)
    root.mainloop()
