# ---------------------------------------- #
# Title: Assignment06
# Description: This assignment demonstrates data processing with functions.
# Change Log: Katie Debetaz, 11/14/2024, Created Script
# ---------------------------------------- #

import json

# Define Constants
MENU = """ 
---- Course Registration Program ----
Select from the following menu:  
1. Register a student for a course
2. Show current data  
3. Save data to a file
4. Exit the program
----------------------------------------- 
"""
FILE_NAME = "Enrollments.json"

# Define Variables
students: list = []
menu_choice: str = ""

class FileProcessor:
    """
    Collection of functions for processing json files.

    Katie Debetaz, 11/14/2024, Created Class
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
        This function reads the existing data from the json.

        Katie Debetaz, 11/14/2024, Created function

        :return: list of current data
        """
        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except Exception as e:
            IO.output_error_messages("There was a non-specific error", e)
        finally:
            if file and not file.closed:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
        This function writes new data to the json.

        Katie Debetaz, 11/14/2024, Created function

        :return: None
        """
        try:
            file = open(file_name, "w")
            json.dump(student_data,file)
            file.close()
            print('The following was saved to json:')
            for student in student_data:
                print(f"{student['FirstName']} {student['LastName']} is registered for {student['CourseName']}.")
        except Exception as e:
            IO.output_error_messages("There was a non-specific error", e)
        finally:
            if file and not file.closed:
                file.close()


class IO:
    """
    Collection of functions for user interaction.

    Katie Debetaz, 11/14/2024, Created Class
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        This function prints the error message if applicable.

        Katie Debetaz, 11/14/2024, Created function

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """
        This function prints the menu.

        Katie Debetaz, 11/14/2024, Created function

        :return: None
        """
        print()
        print(menu)
        print()

    @staticmethod
    def input_menu_choice():
        """
        This function asks the user to make a menu choice.

        Katie Debetaz, 11/14/2024, Created function

        :return: string of user's menu choice
        """
        menu_choice = input("Please enter your choice: ")
        return menu_choice

    @staticmethod
    def output_student_courses(student_data: list):
        """
        This function prints the current data.

        Katie Debetaz, 11/14/2024, Created function

        :return: None
        """
        print("The current data is:")
        for student in student_data:
            print(f"{student['FirstName']} {student['LastName']} is registered for {student['CourseName']}.")

    @staticmethod
    def input_student_data(student_data: list):
        """
        This function asks the user to input the first, last, and course name.

        Katie Debetaz, 11/14/2024, Created function

        :return: list of current student data
        """
        try:
            student_first_name = input("Enter student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("First name must be alphabetic, please enter student's first name.")
            student_last_name = input("Enter student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("Last name must be alphabetic, please enter student's last name.")
            course_name = input("Enter the name of the course: ")
            students = {"FirstName":student_first_name,"LastName":student_last_name,"CourseName":course_name}
            student_data.append(students)
        except ValueError as e:
            IO.output_error_messages("Value is not correct type of data", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error",e)
        return student_data

# Main program
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Processing options for menu
while True:
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    # Input for student name and course
    if menu_choice == "1":
        students = IO.input_student_data(student_data=students)

    # Print saved data as a formatted string
    elif menu_choice == "2":
        IO.output_student_courses(student_data=students)

    # Export data to json
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)

    # End program
    elif menu_choice == "4":
        print("Program ended")
        break

    # Validate input
    else:
        print("Choice invalid, please try again.")