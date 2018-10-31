# ==============================================================================
# Author: Worapan Kobbuakli
# File: NewMemberRegistration.py
# Description: Graphical User Interface Application to register Gym's new
# membership information and save it to database.
# ==============================================================================

import tkinter
from tkinter import messagebox # messagebox
import datetime # datetime.datetime.now().year
import string # .title()
import csv
import mysql.connector

# Constant Variables
CURRENT_YEAR = datetime.datetime.now().year
USERNAME = 'john'
PASSWORD = 'johnspassword'
HOST = 'localhost'
DATABASE = 'fitness'
TABLE = 'members'

# ==============================================================================
class MemberRegister():
        
    def __init__(self):   
        mainpage = tkinter.Tk()
        mainpage.title('Sloth and Snail Fitness')
        mainpage.resizable(0, 0)

        # Create all labels
        tkinter.Label(mainpage, text='New Member Registration').grid(
            row=0, column=0, columnspan=5)

        tkinter.Label(mainpage, text='Name : ').grid(
            row=1, column=1, sticky=tkinter.E)
        tkinter.Label(mainpage, text='Gender : ').grid(
            row=2, column=1, sticky=tkinter.E)
        tkinter.Label(mainpage, text='Weight : ').grid(
            row=3, column=1, sticky=tkinter.E)
        tkinter.Label(mainpage, text='Height : ').grid(
            row=4, column=1, sticky=tkinter.E)
        tkinter.Label(mainpage, text='Year of Birth : ').grid(
            row=5, column=1, sticky=tkinter.E)

        # Create Name textbox
        self.name = tkinter.StringVar()
        self.nameEntry = tkinter.Entry(mainpage, width=30, textvariable=self.name)
        self.nameEntry.grid(row=1, column=2, columnspan=4 ,sticky=tkinter.W)

        # Create Gender Radio Buttons
        self.genderList = ['Male', 'Female', 'Unspecified']
        self.gender = tkinter.StringVar()
        for i in range (len(self.genderList)):
            self.genderButton = tkinter.Radiobutton(mainpage, text=self.genderList[i],
                                variable=self.gender, value=self.genderList[i])
            self.genderButton.grid(row=2, column=i+2,sticky=tkinter.W)
        self.gender.set(self.genderList[2])
            
        # Create Weight textbox
        self.weight = tkinter.DoubleVar()
        self.weight.set('')
        self.weightBox = tkinter.Entry(mainpage, width=10, textvariable=self.weight)
        self.weightBox.grid(row=3, column=2,sticky=tkinter.E)
        tkinter.Label(mainpage, text='lbs.').grid(row=3, column=3, sticky=tkinter.W)
    
        # Create Height Drop Down menuchoice
        self.feetList = [1,2,3,4,5,6,7,8,9,10]
        self.inchesList = [0,1,2,3,4,5,6,7,8,9,10,11]
        self.feet = tkinter.IntVar()
        self.inches = tkinter.IntVar()
        self.feet.set(self.feetList[0])

        tkinter.OptionMenu(mainpage, self.feet, *self.feetList).grid(
            row=4, column=2, sticky=tkinter.E)
        tkinter.Label(mainpage, text='ft.').grid(
            row=4, column=3, sticky=tkinter.W)

        tkinter.OptionMenu(mainpage, self.inches, *self.inchesList).grid(
            row=4, column=3, sticky=tkinter.E)
        tkinter.Label(mainpage, text='inches').grid(
            row=4, column=4, sticky=tkinter.W)
        
        # Create Birth Year Drop down menuchoice
        self.yearList = [year for year in range(CURRENT_YEAR,CURRENT_YEAR-100,-1)]
        self.birthyear = tkinter.IntVar()
        self.birthyear.set(self.yearList[0])
        tkinter.OptionMenu(mainpage, self.birthyear, *self.yearList).grid(row=5, column=2, sticky=tkinter.E)

        # Create Quit Button
        tkinter.Button(mainpage, text='Quit', width=8,
                       command=mainpage.destroy).grid(row=6, column=4, pady=10)

        # Create Clear Button
        tkinter.Button(mainpage, text='Reset', width=8,
                       command=self.reset_input).grid(row=6, column=2, pady=10)

        # Create Submit Button
        tkinter.Button(mainpage, text='Submit', width=8,
                       command=self.submit).grid(row=6, column=1, pady=10)

    # ==========================================================================
    # Function to reset current data input on screen
    def reset_input(self):
        self.name.set('')
        self.gender.set(self.genderList[2])
        self.weight.set('')
        self.feet.set(self.feetList[0])
        self.inches.set(0)
        self.birthyear.set(self.yearList[0])

    # ==========================================================================
    # Function to validate the data, if invalid popup a window with error message.
    # Then popup another window for confirmation
    def submit(self):
        try:
            self.member_name = self.name.get()
            if self.member_name == '' :
                raise ValueError('Name cannot be empty.')
            
            self.member_gender = self.gender.get()
            self.member_weight = self.weight.get()
            if self.member_weight <= 0:
                raise tkinter.TclError

            self.member_feet = self.feet.get()
            self.member_inches = self.inches.get()

            self.member_year = self.birthyear.get()

            self.confirm_window()

        except ValueError as message:
            tkinter.messagebox.showinfo('Error',message)
            
        except tkinter.TclError:
            tkinter.messagebox.showinfo('Error','Weight must be positive number.')
            self.weight.set('')
            
    # ==========================================================================
    # Function to create another window, allow user to double check the data
    # input, press confirm button to save data or cancel back to main window
    def confirm_window(self):
        self.top = tkinter.Toplevel()
        self.top.title('Confirmation')
        self.top.resizable(0, 0)
        
        tkinter.Label(self.top, text='New Member Info Confirmation').grid(
            row=0,column=1)
        self.member_name = self.member_name.title()
        message =  '      Name: '+self.member_name+'\n'
        message += '    Gender: '+self.member_gender+'\n'
        message += '    Weight: '+str(self.member_weight)+'\n'
        message += '    Height: '+str(self.member_feet)
        message += '\' '+str(self.member_inches)+'\"\n'
        message += 'Birth Year: '+str(self.member_year)

        tkinter.Label(self.top, text=message).grid(row=1, column=1, columnspan=2)

        # Create Confirm and Cancel Button
        tkinter.Button(self.top, text='Confirm', width=8,
                       command=self.save_data).grid(row=2,
                                                    column=0, pady=10, padx=5)
        tkinter.Button(self.top, text='Cancel', width=8,
                       command=self.top.destroy).grid(row=2,
                                                      column=3, pady=10, padx=5)

    # ==========================================================================
    # Function to log in to database and generate id number by reading row
    # in the database. Then insert id, and all others infomation to the database
    def save_data(self):
        try:
            connect = mysql.connector.connect(host = HOST,
                                              user = USERNAME,
                                              passwd = PASSWORD,
                                              database = DATABASE)
            cursor = connect.cursor()
            
            # Generate new member id by get the last sorted member id + 1
            cursor.execute("SELECT member_id FROM members ORDER BY member_id DESC LIMIT 1")
            result_set = cursor.fetchone()
            member_id = result_set[0] + 1

            add_member = ("INSERT INTO "+TABLE+
                          "(member_id, name, gender, weight, feet, inch, year) "
                          " VALUES (%s, %s, %s, %s, %s, %s, %s)")

            data_member = (member_id,
                           self.member_name.title(),
                           self.member_gender,
                           self.member_weight,
                           self.member_feet,
                           self.member_inches,
                           self.member_year)

            cursor.execute(add_member, data_member)
            connect.commit()
            cursor.close()
            connect.close()

            tkinter.messagebox.showinfo('Congratulation!',
                                         'New member has been saved.')
            
        except:
            tkinter.messagebox.showinfo('Error',
                                         'Cannot Save New Member to Database.')

        self.top.destroy()
        self.reset_input()

        
# ==============================================================================
def main():
    #fitness = MemberRegister()
    MemberRegister()
    
# Calling main function
main()
