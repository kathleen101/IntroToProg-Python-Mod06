# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# KWONG,11.23.2021,Modified code to complete assignment 06
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
file_name_str = "ToDoFile.txt"  # The name of the data file
file_obj = None  # An object that represents a file
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
        try:
            strFile = open(file_name_str, 'r')
            for row in strFile:
                lstRow = row.split(', ')
                task = lstRow[0]
                priority = lstRow[1].strip()
                list_of_rows[task] = priority
            for task, priority in dicRow.items():
                print(task, ', ', priority)
        except:
            print('No data found!')
            list_of_rows = {}
        return list_of_rows

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        """ Adds task and priority

        :param task: (string) you want to fill dictionary with task
        :param priority (string) you want to fill dictionary with priority
        :param list_of_rows (dictionary)
        :return: (dictionary) of task and priority
        """
        list_of_rows[task] = priority # sets task to priority in dictionary
        return list_of_rows

    @staticmethod
    def remove_data_from_list(task, list_of_rows):
        """ Removes data from dictionary
        :param task: (string) which task to remove from dictionary
        :param list_of_rows (dictionary) you want to fill dictionary with priority
        :return: (dictionary) of task and priority
        """
        del list_of_rows[task] # deletes task in dictionary
        print('\nOkay, I have deleted', task)
        return list_of_rows

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """ Removes task from dictionary
        :param file_name: (string) which file to write the dictionary to
        :param list_of_rows (dictionary) to write into file
        :return: (dictionary) of task and priority
        """
        with open(file_name_str, 'w') as f: # opens file and writes formatted task and priority into file
            for task, priority in list_of_rows.items():
                format_dictionary = '{tname}, {pname}\n'.format(tname = task, pname = priority)
                f.write(str(format_dictionary))
        #close file
        f.close()
        # print below message
        print('Data saved!')
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
        :param: None
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
        if list_of_rows != {}: # if dictionary is not empty, format and print out the task and priority
            for task, priority in list_of_rows.items():
                print(task,", ", priority)
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_new_task_and_priority():
        """ Requesting task and priority from user

        :param: None
        :return: task, priority
        """
        task = str(input("Which task would you like to add? ")) # requesting which task to add
        if task not in list_of_rows: # looping through dictionary and checking for task's existance
            priority = str(input("What is the priority of the task? ")) # requesting priority of task if there
            print("\nOkay", task, "has been inputted")
        else:
            print("\n", task, "is already in the list!")
            priority = None # setting priority is None
        return task, priority

    @staticmethod
    def input_task_to_remove():
        """ Requesting task and priority from user

        :param: None
        :return: task (string) to be removed
        """
        task = str(input("Which task would you like to remove? ")) # requests task
        if task not in list_of_rows: # loops through dictionary to check if task in dictionary
            print("\n", task, "does not exist!")
        return task

# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
list_of_rows = Processor.read_data_from_file(file_name_str, table_lst)  # read file data

# Step 2 - Display a menu of choices to the user
while (True):
    # Step 3 Show current data
    IO.output_current_tasks_in_list(list_of_rows)  # Show current data in the list/table
    IO.output_menu_tasks()  # Shows menu
    choice_str = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if choice_str.strip() == '1':  # Add a new Task
        task, priority = IO.input_new_task_and_priority() # set task and priority to results of function
        list_of_rows = Processor.add_data_to_list(task, priority, list_of_rows) # set list_of_rows to results of function
        continue  # to show the menu

    elif choice_str == '2':  # Remove an existing Task
        task = IO.input_task_to_remove() # which task to remove from dictionary
        list_of_rows = Processor.remove_data_from_list(task, list_of_rows) # set list of rows to results of function
        continue  # to show the menu

    elif choice_str == '3':  # Save Data to File
        Processor.write_data_to_file(file_name_str, list_of_rows) # execute function to save data
        continue  # to show the menu

    elif choice_str == '4':  # Exit Program
        print("Goodbye!")
        break  # and Exit
