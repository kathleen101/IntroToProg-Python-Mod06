# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# KWONG, 11.22.2021, Modified code to complete assignment 06
# KWONG, 11.26.2021, Modified code to correctly complete assignment 06 in list format
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
file_name_str = "ToDoFile.txt"  # The name of the data file
file_obj = None  # An object that represents a file
row_dic = {}  # A row of data separated into elements of a dictionary {Task,Priority}
table_lst = []  # A list that acts as a 'table' of rows
choice_str = ""  # Captures the user option selection


# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        file = open(file_name, "r")
        for line in file:
            task, priority = line.split(",")
            row = {"Task": task.strip(), "Priority": priority.strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        """ Adds new data into list of dictionary rows

        :param task: (string) you want to add to list
        :param priority: (list) you want to attach to task
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        row_dic = {"Task": task, "Priority": priority}
        list_of_rows.append(row_dic)
        print("\n Okay,", task, "added!")
        return list_of_rows

    @staticmethod
    def remove_data_from_list(task, list_of_rows):
        """ Removes data from list of dictionary rows

        :param task: (string) you want to remove from list
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        row_num = 0
        for row in list_of_rows:
            task_check, priority_check = dict(row).values()
            if task.lower() == task_check.lower():
                del list_of_rows[row_num]
                row_num += 1
                print("\n Okay,", task, "deleted!")
            else:
                row_num += 1
        return list_of_rows

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """ Removes data from list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        file_obj = open(file_name_str, "w")
        for row_dic in list_of_rows:
            file_obj.write(row_dic["Task"] + "," + row_dic["Priority"] + "\n")
        print("File saved.")
        file_obj.close()
        return list_of_rows


# Presentation (Input/Output)  -------------------------------------------- #


class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def output_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def output_current_tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current tasks ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_new_task_and_priority():
        """ Removes data from list of dictionary rows

        :param task: (string) data you want to add to file:
        :param priority: (string) you want to attach to task:
        :return: (string) of both datapoints
        """
        task = str(input("What task would you like to add? "))
        priority = str(input("What is the priority of this task? "))
        return task, priority

    @staticmethod
    def input_task_to_remove():
        """ Removes data from list of dictionary rows

        :param task: (string) data you want to remove from file:
        :return: (string)
        """
        task = str(input("Which task would you like to remove? "))
        return task


# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(file_name_str, table_lst)  # read file data

# Step 2 - Display a menu of choices to the user
while (True):
    # Step 3 Show current data
    IO.output_current_tasks_in_list(table_lst)  # Show current data in the list/table
    IO.output_menu_tasks()  # Shows menu
    choice_str = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if choice_str.strip() == '1':  # Add a new Task
        task, priority = IO.input_new_task_and_priority() # requests for data from user
        table_lst = Processor.add_data_to_list(task, priority, table_lst) # adds requested data into list
        continue  # to show the menu

    elif choice_str == '2':  # Remove an existing Task
        task = IO.input_task_to_remove() # requests for data from user
        table_lst = Processor.remove_data_from_list(task, table_lst) # removes data from list if found
        continue  # to show the menu

    elif choice_str == '3':  # Save Data to File
        table_lst = Processor.write_data_to_file(file_name_str, table_lst) # saves data to file
        continue  # to show the menu

    elif choice_str == '4':  # Exit Program
        print("Goodbye!")
        break  # and Exit
