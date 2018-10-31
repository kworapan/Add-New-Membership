# Add-New-Membership
Python GUI to add new gym member to database by using tkinter and mysql-connector libraries.

This application is created for scenario of new membership registration of a gym, where an employee enters a new customer information to their database. The application uses Tkinter module to create a graphical user interface which make it easy to navigate around the application, and Even Driven Programming to perform actions on each button pressed. The data has to be entered are name, gender, weight, height, and birth year, if any invalid data was entered the application will popup a window with an error message.

There are 3 buttons on the first window.
  1. Quit button is to exit the application.
  2. Reset button is to remove (empty) all input areas.
  3. Submit button will collect all data that has been entered and popup another window for confirmation, 
      in this window will allow the user to double check the data input. 
      Then either press confirm button to save data or cancel button to go back to the first window.

After the user pressed the confirm button, the program will generate a new member id number, then save the id and all data to the database table.

DATABASE fitness
TABLE members
	member_id INT(4) <-- Primary key
	name VARCHAR(128)
	gender VARCHAR(12)
	weight INT(3)
	feet INT(2)
	inch INT(2)
	year INT(4)
