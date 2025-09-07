# ===== Importing external modules =======
"""Task Management 
This script allows user registration, login, adding tasks, and viewing tasks.
It supports viewing all tasks or only tasks assigned to the logged-in user.
In addition, only admins are allowed to delete tasks or generate reports. 
Admin sees a different menu to non-admin
"""

import sys
from datetime import date, datetime
from tabulate import tabulate
import textwrap


# ==== Read and clean tasks file ====
try:
    with open("tasks.txt", "r") as f:
        records = f.readlines()
except FileNotFoundError:
    print("The file does not exist. Please check the file path and try again.")
    records = []

task_data = []

# Ensure every task has a task number (first column)
with open("tasks.txt", "w") as file:
    for idx, task in enumerate(records, start=1):
        partrec = [x.strip() for x in task.strip().split(",")]
        if len(partrec) == 6:  # old tasks without task number
            partrec.insert(0, str(idx))
        elif len(partrec) == 7:  # already has task_number
            pass
        else:  # malformed task
            print(f"Skipping malformed task: {partrec}")
            continue
        task_data.append(partrec)
        file.write(",".join(partrec) + "\n")

# ==== Read and clean users file ====
try:
    with open("user.txt", "r") as file:
        lines = file.readlines()
except FileNotFoundError:
    print("The file does not exist. Please check the file path and try again.")
    lines = []

with open("user.txt", "w") as file:
    for line in lines:
        part = [x.strip() for x in line.strip().split(",")]
        if len(part) == 2:
            file.write(",".join(part) + "\n")

# ==== Create users dictionary ====
users = []
with open("user.txt", "r") as file:
    for i in file:
        parts = i.strip().split(",")
        users.append({"username": parts[0].strip(), "password": parts[1].strip()})

# ==== User login ====
"""Creates a user and checks
 if the user already exists
 , if they do, user needs to try again"""
 
while True:
    user_name = input("Enter username:").strip()
    matched_user = None

    for user in users:
        if user["username"].strip().lower() == user_name.lower():
            matched_user = user
            break

    if not matched_user:
        print("Username does not exist")
        continue

    while True:
        user_password = input("Enter password:").strip()
        if matched_user["password"] == user_password:
            print("You are logged in")
            break
        else:
            print("Password incorrect")
    break


# ==== Define functions ====

def print_task(task, idx=None):
    """
    Prints tasks in a readable format.

    Parameters:
    - task (list): A task record with 7 fields:
      [task_number, assigned_to, task_title, task_description, date_assigned, due_date, task_complete]
    - idx (int, optional): Menu number or index for display purposes.
    """
    task_number, assigned_to, task_title, task_description, date_assigned, due_date, task_complete = [x.strip() for x in task]

    print("-" * 50)
    if idx is not None:
        print(f"Menu number:     {idx}")           # for selection
    print(f"Task number(ID): {task_number}")      # permanent ID
    print(f"Task:            {task_title}")
    print(f"Assigned to:     {assigned_to}")
    print(f"Date assigned:   {date_assigned}")
    print(f"Due date:        {due_date}")
    print(f"Task Complete?   {task_complete}")
    print(f"Task description:\n  {task_description}")
    print("-" * 50)


def table_tasks(tasks):
    """
   Prints out a table of tasks in a readable format.

   This function can be used in multiple contexts:
   - Admin can view tasks when deciding which task to delete.
   - Non-admin users can view their own tasks when editing or completing tasks.

   Parameters:
   - tasks (list): A list of task records. Each task should have 7 fields:
     [task_number, assigned_to, task_title, task_description, date_assigned, due_date, task_complete]

   The function automatically wraps long descriptions to fit nicely in the table.
   """
    rows = []
    for idx, task in enumerate(tasks, start =1):
        if len(task) != 7:
            print(f"Skipping malformed task: {task}")
            continue

        task_number, assigned_to, task_title, task_description, date_assigned, due_date, task_complete = [x.strip() for x in task]

        # Only keep the columns you want
        wrapped_assignedt_to = "\n".join(textwrap.wrap(assigned_to, width=5))
        wrapped_desc = "\n".join(textwrap.wrap(task_description, width=30))
        wrapped_task_completed = "\n".join(textwrap.wrap(task_complete, width=10))
        rows.append([idx, task_number, wrapped_desc, wrapped_assignedt_to, date_assigned, due_date, wrapped_task_completed])

    headers = ["Menu number","Task Number","Description", "assgigned_to","Date Assigned","Due Date","Completed?"]
    print(tabulate(rows, headers=headers, tablefmt="grid"))


def save_tasks_to_file(filename="tasks.txt"):
    """Saves the current task_data list to tasks.txt.

    Parameters:
    - filename (str): Name of the file to save tasks to. Default is 'tasks.txt'."""

    with open(filename, "w") as f:
        for task in task_data:
            line = ", ".join(task) + "\n"
            f.write(line)


def reg_user():
    """ 
        Registers a new user.
        Checks if the username already exists. 
        If not, prompts for a password and confirmation.
        Saves the new user to user.txt 
        and adds to the in-memory users list.
        
     """
    
    new_username = input("Enter new username:").strip()
    if any(user["username"].strip().lower() == new_username.lower() for user in users):
        print("Username already exists. Try a different one.")
        return

    while True:
        new_password = input("Enter new password:").strip()
        confirm_password = input("Confirm password:").strip()
        if new_password == confirm_password:
            with open("user.txt", "a") as file:
                file.write(f"{new_username},{confirm_password}\n")
            users.append({"username": new_username, "password": confirm_password})
            print("User has been successfully added")
            break
        else:
            print("Passwords do not match. Try again.")


def add_task():
    """
    Adds a new task for a user.

    Prompts for the username, task title, description, due date, and status.
    Saves the new task to tasks.txt and adds it to the in-memory task_data list.
    """
    task_status = 'no'
    enter_username = input("Enter username for task:").strip().lower()
    
    if not any(u["username"].strip().lower() == enter_username for u in users):
        print("User does not exist")
        return
    
    task_title = input("Enter Task: ").strip()
    task_description = input("Enter task description: ").strip()
    
    while True:
        task_due_date = input("Enter Due Date, example 2025-09-06: ").strip()
        try:
            datetime.strptime(task_due_date, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
    
    current_date = date.today()
    task_status_input = input("Enter task status yes/no: ").strip().lower()
    if task_status_input == 'yes':
        task_status = 'yes'
    
    # Calculate next task_number
    if task_data:
        task_number = str(int(max(task_data, key=lambda t: int(t[0]))[0]) + 1)
    else:
        task_number = "1"
    
    task_entry = [
        task_number,
        enter_username,
        task_title,
        task_description,
        task_due_date,
        current_date.isoformat(),
        task_status
    ]
    
    with open("tasks.txt", "a") as file:
        file.write(",".join(task_entry) + "\n")
    task_data.append(task_entry)

def view_all():
    """ 
    This function allows admin and non-admin to view all tasks.
    Prints out all tasks with details related to the task such as 
    date assigned, due date, assigned to, and if the task
    is completed or not.
    
    """
    for task in task_data:
        if len(task) != 7:
            print(f"Skipping malformed task: {task}")
            continue
        print_task(task, idx=None)
        

def view_mine():
    """
    Allows the user to view their tasks and manage them.
    User can mark tasks as complete or edit the assignee and due date.
    After changes are submitted, tasks.txt is updated.
    
    """
    my_tasks = [task for task in task_data if task[1].strip().lower() == matched_user["username"].lower()]

    if not my_tasks:
        print("You have no tasks assigned.")
        return

    while True:  # loop so user can make multiple edits
        print("\nYour tasks:")
        for idx, task in enumerate(my_tasks, start=1):
            if len(task) != 7:
                continue
            #print_task(task, idx)

        # Show table view
        table_tasks(my_tasks)

        try:
            selection = int(input("\nEnter menu number to manage, or -1 to return: "))
        except ValueError:
            print("Invalid input.")
            continue

        if selection == -1:
            return

        if 1 <= selection <= len(my_tasks):
            task = my_tasks[selection - 1]  # pick task by menu number
            task_number = task[0]

            print(f"\nSelected Task ID: {task_number} → {task[2]}")
            action = input("Do you want to (c)omplete or (e)dit this task? ").strip().lower()

            if action == "c":
                task[6] = "yes"
                print("Task marked as complete.")
                save_tasks_to_file()  # save changes immediately

            elif action == "e":
                if task[6].strip().lower() == "yes":
                    print("Task already complete. Cannot edit.")
                else:
                    new_user = input(f"Enter new username (or press Enter to keep '{task[1]}'): ").strip()
                    if new_user:
                        task[1] = new_user

                    new_due = input(f"Enter new due date (or press Enter to keep '{task[5]}'): ").strip()
                    if new_due:
                        task[5] = new_due

                    print("Task updated successfully.")
                    save_tasks_to_file()  # save changes immediately

            else:
                print("Invalid action. Please choose 'c' or 'e'.")
        else:
            print("Invalid selection.")


        

def view_completed():
    """
    allows users to view all their completed tasks

    
    """
    for task in task_data:
        if len(task) != 7:
            print(f"Skipping malformed task: {task}")
            continue

        task_number, assigned_to, task_title, task_description, date_assigned, due_date, task_complete = [x.strip() for x in task]
        if task_complete.lower() == "yes":
            print("-" * 50)
            print(f"Task number:      {task_number}")
            print(f"Task:            {task_title}")
            print(f"Assigned to:     {assigned_to}")
            print(f"Date assigned:   {date_assigned}")
            print(f"Due date:        {due_date}")
            print(f"Task Complete?   {task_complete}")
            print(f"Task description:\n  {task_description}")
            print("-" * 50)

def delete_task():
    """
    Only the admin is allowed to delete tasks.
    They can delete via a chosen task number
    """
    global task_data
    table_tasks(task_data)
    task_number_to_delete = input("Enter task number to be deleted: ").strip()
    task_data = [task for task in task_data if task[0].strip() != task_number_to_delete]
    save_tasks_to_file(filename="tasks.txt")
    print(f"Task {task_number_to_delete} has been deleted.")
    


def parse_date(due_str):
    """Try multiple date formats and return a date object"""
    for fmt in ("%Y-%m-%d", "%d %b %Y"):  # add more formats if needed
        try:
            return datetime.strptime(due_str.strip(), fmt).date()
        except ValueError:
            continue
    return None  # invalid date


def calculate_task_overview():
    today = date.today()
    completed_tasks = [task for task in task_data if task[6]=="yes"]
    uncompleted_tasks = [task for task in task_data if task[6]=="no"]
    overdue_tasks = [
    task for task in task_data
    if len(task) == 7
    and  parse_date(task[5]) is not None
    and parse_date(task[5]) < today
    and task[6].strip().lower() == "no"]
    total_tasks = len(task_data)
    total_overdue_tasks = len(overdue_tasks)
    percent_uncompleted_tasks = float(len(uncompleted_tasks)/total_tasks)*100.0
    percent_overdue_tasks = float(total_overdue_tasks/total_tasks)*100.0
    
    lines = [
        f"Total number of tasks:               {total_tasks}",
        f"Total number of completed tasks:     {len(completed_tasks)}",
        f"Total number of uncompleted tasks:  {len(uncompleted_tasks)}",
        f"Total overdue tasks:                {total_overdue_tasks}",
        f"% of uncompleted tasks:             {percent_uncompleted_tasks:.2f}%",
        f"% of overdue tasks:                 {percent_overdue_tasks:.2f}%"
    ]
    
    return lines
 
    

def display_task_overview():
    """Display task statistics on screen"""
    lines = calculate_task_overview()
    for line in lines:
        print(line)


def generate_task_report(filename="task_overview.txt"):
    """Write task statistics to a file"""
    lines = calculate_task_overview()
    try:
        with open(filename, "w") as f:
            for line in lines:
                f.write(line + "\n")
        print(f"Report successfully written to '{filename}'.")
    except Exception as e:
        print(f"Error writing to '{filename}': {e}")
        
        
# ==== Main menu loop ====
while True:
    if matched_user["username"].strip().lower() == "admin":
        menu = input(
            '''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
vc - view completed tasks
del - delete tasks
ds  - display statistics
gr - generate reports
e - exit
: '''
        ).lower()
    else:
        menu = input(
            '''Select one of the following options:
a - add task
va - view all tasks
vm - view my tasks
e - exit
: '''
        ).lower()

    if menu == 'r':
        reg_user()
    elif menu == 'a':
        add_task()
    elif menu == 'va':
        view_all()
    elif menu == 'vm':
        view_mine()
    elif menu == 'vc':
        view_completed()
    elif menu == 'ds':
        display_task_overview()
    elif menu == 'del':
        delete_task()
    elif menu == 'gr':
        generate_task_report()
        print("Report has been generated")
        
    elif menu == 'e':
        print('Goodbye!!!')
        sys.exit()
    else:
        print("You have entered an invalid input. Please try again")
