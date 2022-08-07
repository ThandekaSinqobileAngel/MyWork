# Compulsory Task 1 and Compulsory Task 2
# This program is for a small business that can help manage tasks assigned to each member of the team.
# There are two files namely user.txt and tasks.txt that are used.
# tasks.txt stores a list of all the tasks that the team is working on.
# user.txt stores the username and password for each user that has permission to use the program.
# Data manipulation in the tasks.txt and user.txt file can only be done by admin

import datetime
import re

users = {}
with open ('user.txt', 'rt')as username:
    for line in username:
        username, password = line.split(",")
        users[username.strip()] = password.strip()  # Strip removes leading/trailing whitespaces

uinput = input("Please enter your username:\n")
while uinput != "admin":  # Only the user logged in as 'admin', will be able to access this menu.
    print("Username incorrect.")
    uinput = input("Please enter a valid username:\n")

if uinput in users:
            print ("Username correct")

with open('user.txt', 'rt') as password:
    for line in password:
        username, password = line.split(",")
        users[password.strip()] = username.strip()  

uinput2 = input("Please enter your password:\n")
while uinput2 not in users:
    print("Your username is correct but your password is incorrect.") # if admin enters username that does not match password
    uinput2 = input("Please enter a valid password:\n")

if uinput2 in users:
    password2 = ("Password correct")
    print (password2)

if password2 == ("Password correct"): # After entry of accurate admin credentials, the menu then appears 
        menu = (input("\nPlease select one of the following options:\nr - register user\na - add task\nva - view all tasks\nvm - view my tasks\ns- statistics\ne - exit\n"))
        if menu == "r" or menu == "R": # the admin has permision to register a user to the tasks.txt file
                    new_user = (input("Please enter a new user name:\n"))
                    new_password = (input("Please enter a new password:\n"))
                    confirm_password = (input("Please confirm password:\n"))
                    if(new_password == confirm_password):  # If password matches confirm password, user is added on the tasks.txt file
                        with open ('user.txt', 'a')as username:
                            username.write("\n" + new_user + ", " + new_password)
                            print("New user has been successfully added")
                    else:
                        print("Please enter matching password.")
                        
        elif menu == "a" or menu == "A":  # the admin has permision to add tasks for user that is in this program
            task = input("Please enter the username of the person to whom the  task is assigned to.\n")
            while task not in username:
                task = input("Username not registered. Please enter a valid username.\n")

            else:
                task_title = input("Enter the title of the task.\n")
                task_description = input("Enter the task description.\n")
                task_due = input("Enter the due date of the task. (yyyy-mm-dd)\n")
                date = datetime.date.today()
                task_completed = False
                if task_completed == False: 
                    task_completed = "No"
                else:
                    task_completed = ("Yes")
                with open('tasks.txt', 'a') as task:
                    task.write("\nUser assigned to task:\n" + uinput + "\nTask Title :"  + "\n" + task_title + "\n" + "Task Description:\n" + task_description + "\n" + "Task Due Date:\n" + task_due + "\n" + "Date Assigned:\n" + str(date) + "\n" + "Task Completed:\n" + task_completed + "\n") 
                    print("Task details have been successfully added")
                    
        elif menu == "va" or menu == "VA": # This option displays information for each task, view all tasks
            all_tasks = open('tasks.txt', 'r')
            text = all_tasks.read()
            all_tasks.close()
            print(text)
        elif menu == "vm" or menu == "VM": # View task of the user currently logged in
            with open('tasks.txt','r') as fl:
                lst = re.findall('.*\n*User assigned to task:.*\n*(' + re.escape(uinput) + ')\n*Task Title :\n*(.*)\n*Task Description:\n*(.*)\n*Task Due Date:\n*(.*)\n*Date Assigned:\n*(.*)\nTask Completed:\n*(.*)\n*', fl.read())
                for item in lst:
                    print(f'{item[0]} Tasks Details: \nTask Title:{item[1]}\nTask description:{item[2]}\nTask Due Date:{item[3]}\nDate Assigned:{item[4]}\nDate Assigned:{item[5]}')                  
        elif menu == "e" or menu == "E":
            print("Thank you for using this program")
            exit()
        elif menu == "s" or menu == "S":
            tasks_num = 0
            users_num = 0

            with open("tasks.txt", "r") as task_file:
                for line in task_file:
                    tasks_num += 1
                total_username = tasks_num / 13  # Calculations that gives number of task
                print (f"\nTotal number of tasks: {int(total_username)}") # Displays total number of tasks

            with open("user.txt", "r") as username:
                for line in username:
                    users_num += 1
                print (f"Total number of users: {users_num}") # Displays total number of users
        else:
            print("Invalid entry choice, Please try again")
    
                   
                
            